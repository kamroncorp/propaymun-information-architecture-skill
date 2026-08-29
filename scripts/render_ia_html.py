#!/usr/bin/env python3
"""Render a semantic IA JSON file as a standalone accessible HTML document."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from typing import Any

from validate_ia_model import validate_model


def e(value: Any) -> str:
    return html.escape(str(value), quote=True)


def render_tree(nodes: list[dict[str, Any]]) -> str:
    children: dict[str | None, list[dict[str, Any]]] = {}
    for node in nodes:
        children.setdefault(node.get("parent_id"), []).append(node)
    for values in children.values():
        values.sort(key=lambda item: str(item.get("label", "")).casefold())

    def branch(parent: str | None, active: set[str]) -> str:
        items: list[str] = []
        for node in children.get(parent, []):
            node_id = str(node["id"])
            if node_id in active:
                continue
            child_html = branch(node_id, active | {node_id})
            purpose = node.get("purpose") or node.get("summary")
            purpose_html = f"<span class='purpose'>{e(purpose)}</span>" if purpose else ""
            items.append(
                f"<li><div class='node' data-evidence='{e(node.get('evidence_status', 'Unknown'))}'>"
                f"<span class='label'>{e(node.get('label', node_id))}</span>"
                f"<span class='type'>{e(node.get('type', 'item'))}</span>"
                f"{purpose_html}"
                f"</div>{child_html}</li>"
            )
        return f"<ul>{''.join(items)}</ul>" if items else ""

    return branch(None, set())


def render_list(title: str, items: list[Any]) -> str:
    if not items:
        return ""
    rows = "".join(f"<li>{e(item if not isinstance(item, dict) else json.dumps(item, ensure_ascii=False))}</li>" for item in items)
    return f"<section><h2>{e(title)}</h2><ul class='plain'>{rows}</ul></section>"


def render_document(data: dict[str, Any]) -> str:
    meta = data["meta"]
    direction = meta.get("direction", "ltr")
    nodes = data.get("nodes", [])
    node_labels = {str(item.get("id")): str(item.get("label", item.get("id"))) for item in nodes}
    relationships = data.get("relationships", [])
    relationship_rows = "".join(
        "<li class='relationship'>"
        f"<strong>{e(node_labels.get(str(item.get('from')), item.get('from')))}</strong>"
        f"<span class='relation-type'>{e(item.get('label') or item.get('type'))}</span>"
        f"<strong>{e(node_labels.get(str(item.get('to')), item.get('to')))}</strong>"
        + (f"<p>{e(item.get('meaning'))}</p>" if item.get("meaning") else "")
        + "</li>"
        for item in relationships
    )
    relation_section = ""
    if relationship_rows:
        relation_section = (
            "<section><h2>Key connections</h2>"
            f"<ul class='relationships'>{relationship_rows}</ul></section>"
        )

    return f"""<!doctype html>
<html lang="{e(meta.get('language', 'en'))}" dir="{e(direction)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(meta['title'])}</title>
<style>
:root{{--ink:#19172b;--muted:#666278;--line:#dcd9ea;--paper:#fbfaff;--brand:#5b4bdb;--soft:#efedff}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:1100px;margin:auto;padding:48px 24px 80px}} header{{border-bottom:1px solid var(--line);padding-bottom:24px;margin-bottom:32px}}
h1{{font-size:clamp(2rem,5vw,4rem);line-height:1.05;margin:0 0 16px}} h2{{margin-top:40px}} .meta{{display:flex;flex-wrap:wrap;gap:8px}}
.pill,.type{{display:inline-block;border-radius:999px;padding:3px 9px;font-size:.78rem}} .pill{{background:var(--soft)}} .type{{background:#f1f0f5;color:var(--muted)}}
.node{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;background:white;border:1px solid var(--line);border-inline-start:4px solid var(--brand);border-radius:10px;padding:10px 12px;box-shadow:0 4px 18px #2d245b0a}}
.purpose{{flex-basis:100%;color:var(--muted);font-size:.9rem}}
.tree ul{{list-style:none;margin:10px 0;padding-inline-start:26px;border-inline-start:1px solid var(--line)}} .tree li{{margin:10px 0}} .label{{font-weight:650}}
.plain{{padding-inline-start:20px}} .relationships{{display:grid;gap:10px;padding:0;list-style:none}} .relationship{{display:grid;grid-template-columns:minmax(8rem,1fr) auto minmax(8rem,1fr);align-items:center;gap:12px;background:white;border:1px solid var(--line);border-radius:10px;padding:12px}} .relationship strong:last-of-type{{text-align:end}} .relationship p{{grid-column:1/-1;margin:0;color:var(--muted)}} .relation-type{{color:var(--brand);text-align:center;font-size:.9rem}}
footer{{margin-top:48px;color:var(--muted);font-size:.9rem}} @media print{{body{{background:white}}main{{max-width:none;padding:20px}}.node{{box-shadow:none}}}}
@media (max-width:640px){{.relationship{{grid-template-columns:1fr}}.relationship strong:last-of-type{{text-align:start}}.relation-type{{text-align:start}}}}
</style>
</head>
<body><main>
<header><p>ProPaymun Information Architecture</p><h1>{e(meta['title'])}</h1>
<div class="meta"><span class="pill">{e(meta.get('status'))}</span><span class="pill">v{e(meta.get('version'))}</span><span class="pill">{e(meta.get('scope'))}</span></div></header>
<section><h2>Information structure</h2><div class="tree" role="tree" aria-label="Information architecture hierarchy">{render_tree(nodes)}</div></section>
{relation_section}
{render_list('Assumptions', data.get('assumptions', []))}
{render_list('Unknowns', data.get('unknowns', []))}
{render_list('Validation', data.get('validation', []))}
<footer>Generated from one editable semantic IA model. Evidence and unresolved decisions remain available in the source model.</footer>
</main></body></html>"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.model.read_text(encoding="utf-8"))
    errors, _warnings = validate_model(data)
    if errors:
        raise SystemExit("Cannot render invalid model:\n- " + "\n- ".join(errors))
    output = args.output or args.model.with_suffix(".html")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_document(data), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
