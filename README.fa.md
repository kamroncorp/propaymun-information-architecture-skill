# معماری اطلاعات پروپیمان

[![Version](https://img.shields.io/badge/version-0.4.0-5B4BDB)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT--0-2F855A)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-ready-111827)](SKILL.md)

توضیحات عادی محصول را به یک معماری اطلاعات روشن، شواهدمحور و قابل‌تصمیم‌گیری تبدیل می‌کند؛ حتی اگر کاربر اصطلاحات IA را نداند.

**پروپیمان** یعنی کامل و پُر. کامل‌بودن اینجا یعنی معماری قابل‌فهم، آماده تصمیم و صادق درباره مجهولات؛ نه یک سند طولانی و غیرضروری.

[English](README.md)

## بسته مناسب را انتخاب کنید

| بسته | مناسب برای | دریافت |
|---|---|---|
| **بسته Agent Skill** | Claude.ai Skills و فقط محیط‌هایی که مستندات خودشان سازگاری با بستهٔ Agent Skill را تأیید کرده‌اند | [دانلود ZIP](packages/agent-skill/propaymun-information-architecture.zip) |
| **کیت Workspace** | ChatGPT Projects، Claude Projects، Gemini Gemهایی که دستی ساخته می‌شوند و محیط‌هایی با Instructions پایدار و فایل Knowledge | [فایل دانش](packages/workspace-kit/propaymun-ia-workspace-kit.md) + [دستور Workspace](packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md) |

هر دو بسته از یک رفتار اصلی ساخته می‌شوند. فعال‌شدن خودکار، ماندگاری، ابزارها و محدودیت Context به سرویس میزبان وابسته است.

## نصب در Claude.ai

1. **[بسته Agent Skill](packages/agent-skill/propaymun-information-architecture.zip)** را دانلود کنید.
2. در Claude.ai، قابلیت **Settings → Capabilities → Code execution and file creation** را فعال کنید.
3. وارد **Customize → Skills** شوید.
4. مسیر **+ → Create skill → Upload a skill** را انتخاب کنید.
5. فایل ZIP را بدون Extract کردن آپلود و Skill را فعال کنید.

لینک مخزن GitHub فایل قابل‌آپلود Claude.ai نیست؛ از ZIP بالا استفاده کنید.

## راه‌اندازی در Workspaceهای وب

برای محیطی که صریحاً هم Instructions پایدار و هم فایل Knowledge دارد:

1. فایل [`propaymun-ia-workspace-kit.md`](packages/workspace-kit/propaymun-ia-workspace-kit.md) را به دانش Workspace اضافه کنید؛
2. متن [`WORKSPACE_INSTRUCTIONS.md`](packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md) را در دستور Project، Gem، Workspace یا Custom Agent قرار دهید؛
3. محصول را طبیعی توضیح دهید.

این مسیر «تنظیم با دانش پروژه» است و نباید به‌اشتباه نصب Native Skill نامیده شود.

### Gemini وب

Gemini وب این بسته را به‌صورت Native Skill نصب نمی‌کند؛ باید یک Gem دستی بسازید:

1. مسیر **Explore Gems → New Gem** را باز کنید؛
2. متن [`WORKSPACE_INSTRUCTIONS.md`](packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md) را در Instructions قرار دهید؛
3. فایل [`propaymun-ia-workspace-kit.md`](packages/workspace-kit/propaymun-ia-workspace-kit.md) را زیر **Knowledge** اضافه کنید؛
4. Gem را Save کنید.

### استفادهٔ یک‌باره با فایل

اگر یک سرویس فقط فایل را داخل چت می‌پذیرد، Workspace Kit را پیوست و متن کوتاه Workspace Instructions را همراه اولین پیام Paste کنید. این «استفادهٔ موقت از فایل» است؛ نه نصب، نه تنظیم پایدار و نه تضمین فعال‌شدن خودکار.

## محیط‌های دیگرِ Agent Skill

فقط وقتی از بستهٔ Agent Skill استفاده کنید که مستندات خود همان سرویس، فرمت بسته و روش نصب آن را تأیید کرده باشد. این مخزن عمداً دستور نصب CLI تأییدنشده ارائه نمی‌دهد.

## نقشه نصب قابل‌اسکن برای AI

```yaml
product: ProPaymun Information Architecture
skill_id: propaymun-information-architecture
canonical_entrypoint: SKILL.md
native_package: packages/agent-skill/propaymun-information-architecture.zip
native_package_verified_for: [claude.ai-skills]
workspace_knowledge: packages/workspace-kit/propaymun-ia-workspace-kit.md
workspace_instructions: packages/workspace-kit/WORKSPACE_INSTRUCTIONS.md
workspace_requires: [persistent-instructions, file-knowledge]
gemini_web: create-a-new-gem-manually
one_off_file_use: attach-workspace-kit-and-paste-instructions
do_not_claim: [native-installation, persistent-behavior, automatic-triggering, unverified-cli-support]
package_manifest: packages/manifest.json
semantic_schema: schema/semantic-ia.schema.json
visual_builder_exporter: scripts/export_builder_handoff.py
legacy_download_paths: preserved
release_state: v0.4.0-published
```

یک AI Installer باید فقط بسته متناسب با محیط را انتخاب کند، محتویات بسته را حفظ کند و آپلود فایل دانش را نصب Native معرفی نکند.

## مهارت چه کاری انجام می‌دهد؟

- قبل از سؤال، بریف، فایل‌ها، گفتگو و منابع مجاز را بررسی می‌کند؛
- در تمام مسیر کفایت اطلاعات را دوباره می‌سنجد و به یک دور سؤال ابتدایی محدود نیست؛
- فقط وقتی پاسخ می‌تواند تصمیم بعدی معماری را تغییر دهد سؤال می‌پرسد و خودش متوقف می‌شود؛
- مثل یک منتور ارشد محصول، تصمیم‌های IA را برای کاربر غیرمتخصص به پیامدهای روشن محصول تبدیل می‌کند؛
- اجازه نمی‌دهد حافظهٔ میزبان بی‌اجازه Scope، شواهد یا نوع خروجی همین گفتگو را تغییر دهد؛
- با Deltaهای کوتاه، Progressive Disclosure و یک نمایش در هر مرحله مصرف Context را مدیریت می‌کند؛
- زبان را از جغرافیا، قوانین، فرهنگ و مدل عملیاتی جدا می‌کند؛
- پیش از تعیین عمق مدل، تشخیص می‌دهد مسئله Content/Taxonomy، Object/Operation یا Hybrid است؛
- Domainها، Itemهای اصلی، سلسله‌مراتب، روابط، Taxonomy، برچسب‌ها، Metadata، یافت‌پذیری، دسترسی، چرخه عمر و Governance را مدل می‌کند؛
- واقعیت، مشاهده، تأیید، استنباط، پیشنهاد، تعارض و مجهول را مخلوط نمی‌کند؛
- در صورت اثرگذاری و وجود قابلیت، از منابع عمومی جاری استفاده می‌کند؛
- Sitemap، User Flow، UI محصول، API و Database Design را وارد این مهارت نمی‌کند.

## رفتار تطبیقی

کاربر Mode یا Checkpoint انتخاب نمی‌کند:

```text
بررسی اطلاعات
→ مدل‌سازی لایه بعدی
→ کشف ابهام معماری‌ساز
→ پرسیدن کوچک‌ترین سؤال لازم و توقف
→ ادامه پس از پاسخ
→ سنجش آمادگی پیش از ساخت خروجی
```

اگر کاربر پاسخ را نداند، مهارت می‌تواند چند الگوی قابل‌فهم پیشنهاد و یک پیش‌فرض موقت را با برچسب روشن توصیه کند. زبان یا کلیشه فرهنگی هیچ‌وقت به‌تنهایی قانون محصول نمی‌شود.

## هندآف به ابزارهای سازنده

Figma Make، Lovable و ابزارهای مشابه محیط پایین‌دستی‌اند، نه محل تصمیم‌گیری IA. هر Handoff باید یک هدف روشن داشته باشد: **نمای قابل‌بررسی معماری اطلاعات** یا **نمونهٔ اولیه محصول که به IA متعهد است**.

پس از آماده‌شدن معماری برای هدف موردنظر بنویسید:

```text
از این معماری اطلاعات یک Visual Builder Handoff برای Figma Make بساز.
```

هندآف دو بخش دارد:

1. فایل Markdown خودبسنده شامل مشخصات کامل ساخت؛
2. متن بسیار کوتاه و آماده کپی برای باکس توضیحات ابزار.

این متن کوتاه ضروری است، چون بعضی ابزارها پرامپت بلند را فایل تلقی می‌کنند و تا چیزی در باکس نوشته نشود دکمه Generate فعال نمی‌شود.

خروجی قطعی:

```bash
python scripts/export_builder_handoff.py path/to/ia.json --target figma-make --intent ia-blueprint -o build-spec.md
python scripts/export_builder_handoff.py path/to/ia.json --target lovable --intent product-prototype -o prototype-spec.md
```

نمای اول باید Domainها، Itemهای متصل، سلسله‌مراتب و روابط بین‌دامنه‌ای را نشان دهد و نباید به Dashboard، Sitemap، User Flow، Wireframe، UI، API یا Database Schema تبدیل شود.

## Semantic IA 2.0

قرارداد مستقل از Renderer در [`schema/semantic-ia.schema.json`](schema/semantic-ia.schema.json) قرار دارد و شامل این موارد است:

- اتصال صریح هر Item به Domain؛
- یک فهرست اصلی Itemها؛
- سلسله‌مراتب اصلی و روابط معنادار؛
- نقش‌های مستقل و Permissionهای متصل به Item؛
- وضعیت‌ها و انتقال‌های چرخه عمر؛
- Context محلی همراه با وضعیت شواهد؛
- نوع غالب مسئله و ردگیری نیازهای اطلاعاتی اولویت‌دار؛
- آمادگی هندآف و مجهولات مسدودکننده.

اعتبارسنجی و رندر:

```bash
python scripts/validate_ia_model.py path/to/ia.json
python scripts/render_ia_html.py path/to/ia.json -o ia.html
```

## نقشه مخزن

```text
SKILL.md                     رفتار اصلی
agents/                      Metadata نمایشی Skill
references/                  راهنمای شرطی IA
schema/                      قرارداد Semantic IA 2.0
scripts/                     اعتبارسنجی، رندر، بسته‌بندی و Export
packages/                    بسته‌های حرفه‌ای نصب و راه‌اندازی
install/                     مسیرهای سازگاری برای لینک‌های قبلی
evals/                       سناریوها و معیارهای رفتاری
tests/                       تست‌های قطعی
```

## توسعه و اعتبارسنجی

```bash
python scripts/build_packages.py
python -m unittest discover -s tests -v
python /path/to/skill-creator/scripts/quick_validate.py .
```

GitHub Actions بسته‌ها را بازسازی، برابری بایت‌به‌بایت را بررسی، Fixture مدل معنایی را اعتبارسنجی و تمام تست‌ها را اجرا می‌کند.

## نسخه‌بندی و سازگاری

پروژه از Semantic Versioning و [مجوز MIT No Attribution](LICENSE) استفاده می‌کند. نسخهٔ ۰.۴.۰ اختیار گفتگوی جاری، نقش منتور محصول، مدیریت توکن، مسائل Content-led، اثر تغییرات و Handoffهای سازنده را تقویت می‌کند.

لینک‌های قبلی `install/claude-ai` و `install/universal-web` به‌عنوان Alias سازگار و همگام حفظ می‌شوند؛ مستندات جدید از نام‌های حرفه‌ای بالا استفاده می‌کنند.
