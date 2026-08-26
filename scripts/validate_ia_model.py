#!/usr/bin/env python3
"""Validate structural invariants in a ProPaymun semantic IA JSON file."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


EVIDENCE_STATES = {
    "Provided",
    "Observed",
    "Confirmed",
    "Inferred",
    "Proposed",
    "Unknown",
}


def _required_mapping(value: Any, name: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{name} must be an object")
        return {}
    return value


def _required_list(value: Any, name: str, errors: list[str]) -> list[Any]:
    if not isinstance(value, list):
        errors.append(f"{name} must be an array")
        return []
    return value


def validate_model(data: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    root = _required_mapping(data, "document", errors)
    meta = _required_mapping(root.get("meta"), "meta", errors)
    nodes = _required_list(root.get("nodes"), "nodes", errors)
    relationships = _required_list(root.get("relationships"), "relationships", errors)

    for field in ("title", "version", "status", "language", "scope"):
        if not isinstance(meta.get(field), str) or not meta[field].strip():
            errors.append(f"meta.{field} must be a non-empty string")
    if meta.get("direction") not in {"ltr", "rtl"}:
        errors.append("meta.direction must be 'ltr' or 'rtl'")

    node_ids: set[str] = set()
    parent_by_id: dict[str, str | None] = {}
    for index, raw_node in enumerate(nodes):
        node = _required_mapping(raw_node, f"nodes[{index}]", errors)
        node_id = node.get("id")
        if not isinstance(node_id, str) or not node_id.strip():
            errors.append(f"nodes[{index}].id must be a non-empty string")
            continue
        if node_id in node_ids:
            errors.append(f"duplicate node id: {node_id}")
        node_ids.add(node_id)
        parent = node.get("parent_id")
        if parent is not None and not isinstance(parent, str):
            errors.append(f"node {node_id} parent_id must be a string or null")
        parent_by_id[node_id] = parent
        for field in ("label", "type"):
            if not isinstance(node.get(field), str) or not node[field].strip():
                errors.append(f"node {node_id} {field} must be a non-empty string")
        state = node.get("evidence_status")
        if state not in EVIDENCE_STATES:
            errors.append(f"node {node_id} has invalid evidence_status: {state!r}")

    for node_id, parent_id in parent_by_id.items():
        if parent_id is not None and parent_id not in node_ids:
            errors.append(f"node {node_id} references missing parent: {parent_id}")

    for start in node_ids:
        seen: set[str] = set()
        current: str | None = start
        while current is not None and current in parent_by_id:
            if current in seen:
                errors.append(f"hierarchy cycle detected at node: {current}")
                break
            seen.add(current)
            current = parent_by_id[current]

    relationship_ids: set[str] = set()
    for index, raw_relationship in enumerate(relationships):
        relationship = _required_mapping(raw_relationship, f"relationships[{index}]", errors)
        relationship_id = relationship.get("id")
        if not isinstance(relationship_id, str) or not relationship_id.strip():
            errors.append(f"relationships[{index}].id must be a non-empty string")
            continue
        if relationship_id in relationship_ids:
            errors.append(f"duplicate relationship id: {relationship_id}")
        relationship_ids.add(relationship_id)
        for endpoint in ("from", "to"):
            value = relationship.get(endpoint)
            if value not in node_ids:
                errors.append(
                    f"relationship {relationship_id} references missing {endpoint} node: {value!r}"
                )
        if not isinstance(relationship.get("type"), str) or not relationship["type"].strip():
            errors.append(f"relationship {relationship_id} type must be a non-empty string")
        state = relationship.get("evidence_status")
        if state not in EVIDENCE_STATES:
            errors.append(
                f"relationship {relationship_id} has invalid evidence_status: {state!r}"
            )
        if not relationship.get("label"):
            warnings.append(f"relationship {relationship_id} has no explanatory label")

    if nodes and not any(parent is None for parent in parent_by_id.values()):
        warnings.append("hierarchy has no root node")
    if not nodes:
        warnings.append("model contains no nodes")

    return sorted(set(errors)), sorted(set(warnings))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path, help="Path to semantic IA JSON")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable results")
    args = parser.parse_args()

    try:
        data = json.loads(args.model.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: file not found: {args.model}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid JSON: {exc}", file=sys.stderr)
        return 2

    errors, warnings = validate_model(data)
    if args.json:
        print(json.dumps({"valid": not errors, "errors": errors, "warnings": warnings}, indent=2))
    else:
        for warning in warnings:
            print(f"WARNING: {warning}")
        for error in errors:
            print(f"ERROR: {error}")
        print("VALID" if not errors else "INVALID")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())

