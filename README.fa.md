# مهارت معماری اطلاعات ProPaymun

یک مهارت تخصصی و فقط مخصوص معماری اطلاعات که کاربر را از توضیح طبیعی محصول تا یک IA حرفه‌ای و شواهدمحور همراهی می‌کند؛ حتی اگر کاربر اصطلاحات معماری اطلاعات را نداند.

**ProPaymun — پروپیمان** یعنی کامل و پُر. کامل‌بودن اینجا یعنی «آمادهٔ تصمیم‌گیری»، نه تولید سند طولانی و غیرضروری.

[English](README.md)

## چه کاری انجام می‌دهد؟

- قبل از پرسیدن سؤال، بریف و منابع در دسترس را بررسی می‌کند؛
- فقط سؤال‌هایی را می‌پرسد که پاسخشان می‌تواند معماری را تغییر دهد و خودش منتظر پاسخ می‌ماند؛
- حوزه‌های اطلاعاتی، اشیا و محتوا، سلسله‌مراتب، روابط معنادار، Taxonomy، برچسب‌ها، Metadata، یافت‌پذیری، دسترسی، چرخهٔ عمر و Governance را مدل می‌کند؛
- دادهٔ ارائه‌شده، مشاهده، استنباط، پیشنهاد، تأیید و مجهول را با هم مخلوط نمی‌کند؛
- زبان و عمق پاسخ را با کاربر و توانایی واقعی محیط هماهنگ می‌کند؛
- در صورت نیاز و وجود قابلیت، از جست‌وجوی وب برای اطلاعات جاری و اثرگذار استفاده می‌کند؛
- Sitemap، User Flow، UI، API و Database Design را وارد این مهارت نمی‌کند.

## دو بستهٔ هماهنگ

هیچ روش نصب یک‌کلیکی واقعی وجود ندارد که میان همهٔ هوشواره‌ها مشترک باشد. به همین دلیل ProPaymun دو بستهٔ هم‌زمان دارد:

1. **Native Agent Skill** — فایل [`SKILL.md`](SKILL.md) و منابع همراه برای Claude.ai، Claude Code، Codex، Gemini CLI، ZCode و محیط‌های سازگار با Agent Skills.
2. **Universal Web** — یک فایل Markdown خودبسنده برای Project، Gem، Custom Agent یا چت‌هایی که Native Skill بارگذاری نمی‌کنند.

آپلود فایل در Project با نصب Native Skill یکسان نیست. رفتار IA مشترک می‌ماند، اما فعال‌شدن خودکار، ماندگاری، ابزارها و محدودیت Context به سرویس میزبان بستگی دارد.

## نصب یا راه‌اندازی

### Claude.ai وب — نصب واقعی Skill، حتی پلن Free

فایل آمادهٔ [`propaymun-information-architecture.zip`](install/claude-ai/propaymun-information-architecture.zip) را دانلود کنید. سپس در Claude.ai:

1. در **Settings → Capabilities** گزینهٔ **Code execution and file creation** را فعال کنید؛
2. وارد **Customize → Skills** شوید؛
3. مسیر **+ → Create skill → Upload a skill** را انتخاب کنید؛
4. فایل ZIP را آپلود و Skill را فعال کنید.

لینک مخزن گیت‌هاب نصب‌کنندهٔ Claude.ai نیست؛ Claude.ai بستهٔ ZIP مهارت را می‌خواهد.

### Claude Projects — مسیر Universal

یک Project بسازید، فایل [`propaymun-information-architecture.md`](install/universal-web/propaymun-information-architecture.md) را به دانش پروژه اضافه کنید و متن [`PROJECT_INSTRUCTIONS.md`](install/universal-web/PROJECT_INSTRUCTIONS.md) را در Project Instructions قرار دهید.

### ChatGPT وب

یک Project بسازید، فایل Universal Web را آپلود و متن Project Instructions را در دستورهای پروژه Paste کنید. سپس فقط محصول و نیازتان را طبیعی توضیح دهید. این مسیر پیشنهادی بدون ترمینال برای ChatGPT شخصی است.

### Gemini وب

یک Gem بسازید، متن Project Instructions را در Instructions قرار دهید و فایل Universal Web را به Knowledge اضافه کنید. برای استفادهٔ یک‌باره نیز می‌توانید فایل را به چت پیوست کنید و بخواهید آن را به‌عنوان دستور کار اجرا کند.

### Kimi وب

یک Kimi Project بسازید، فایل Universal Web را به فایل‌های پروژه اضافه و متن Project Instructions را در دستورهای پروژه قرار دهید. Kimi Agent سازندهٔ Skill اختصاصی هم دارد، اما مسیر Project راه‌اندازی قابل‌حمل و بدون ترمینال ماست.

### Z.AI / GLM وب و سایر دستیارها

اگر سرویس Project، Custom Agent، Knowledge Base یا Persistent Instructions دارد، فایل Universal و متن دستور پروژه را همان‌جا اضافه کنید. در غیر این صورت فایل را به چت پیوست کنید و صریحاً بخواهید در همان گفتگو آن را به‌عنوان دستور کار اجرا کند. تا وقتی سرویس تأیید نکرده، نباید ادعا کنیم Native Skill به‌صورت پایدار نصب شده است.

### Claude Code، Codex، Gemini CLI، ZCode و محیط‌های سازگار

```bash
npx skills add https://github.com/kamroncorp/propaymun-information-architecture-skill
```

یا مخزن را در پوشهٔ Skills همان Agent قرار دهید. برای Gemini CLI:

```bash
gemini skills install https://github.com/kamroncorp/propaymun-information-architecture-skill
```

## استفاده

کافی است طبیعی بنویسید:

```text
برای محصولم یک معماری اطلاعات حرفه‌ای می‌خواهم. این هم بریف اولیه...
```

کاربر لازم نیست Mode، Checkpoint، روش توقف یا اصطلاحات IA را بداند. مهارت خودش تشخیص می‌دهد چه زمانی اطلاعات کافی دارد و چه زمانی باید سؤال بپرسد و منتظر بماند.

## خروجی‌ها

خروجی پیش‌فرض، گفت‌وگوی کوتاه و آمادهٔ تصمیم‌گیری است. فایل، JSON معنایی، Mermaid، HTML، PDF یا دیاگرام حرفه‌ای فقط در صورت درخواست و پشتیبانی محیط ساخته می‌شود. همهٔ خروجی‌ها باید نمایی از یک مدل معنایی واحد IA باشند.

ابزارهای مکمل دیاگرام اختیاری‌اند و بدون اجازه نصب نمی‌شوند:

- [Draw.io Skill](https://github.com/Agents365-ai/drawio-skill) برای هندآف دقیق و ویرایش‌پذیر؛
- [Excalidraw Diagram Skill](https://github.com/coleam00/excalidraw-diagram-skill) برای ورک‌شاپ و توضیح مفهومی.

## Figma Make یک خروجی پس از IA است

Figma Make دیگر محل نصب مهارت یا محیط اصلی تصمیم‌گیری IA نیست. پس از اینکه معماری اطلاعات به ثبات کافی رسید، از همان هوشواره بخواهید:

```text
از این معماری اطلاعات تأییدشده، یک پرامپت کامل و خودبسنده برای Figma Make بساز.
```

مهارت مدل اصلی IA، سلسله‌مراتب، روابط، دسترسی، زبان، مجهولات، محدودیت‌ها و معیارهای پذیرش را وارد پرامپت می‌کند. وظیفهٔ Figma Make نمایش معماری است، نه اختراع آن. در محیط دارای Python:

```bash
python scripts/export_figma_make_prompt.py path/to/ia.json -o figma-make-prompt.md
```

## مدل معنایی قابل‌حمل

```bash
python scripts/validate_ia_model.py path/to/ia.json
python scripts/render_ia_html.py path/to/ia.json -o ia.html
```

محیط فقط‌چت منبع درخواستی را مستقیم می‌دهد و ادعا نمی‌کند اسکریپتی اجرا شده است.

## توسعه و ارزیابی

```bash
python scripts/package_distributions.py
python -m unittest discover -s tests -v
python /path/to/skill-creator/scripts/quick_validate.py .
```

بسته‌های Universal Web و Claude.ai با منبع اصلی همگام و تست می‌شوند. فایل [`adapters/manifest.json`](adapters/manifest.json) بسته‌ها و خروجی‌های پایین‌دستی را ثبت می‌کند.

## نسخه‌بندی و مجوز

پروژه از Semantic Versioning و Apache License 2.0 استفاده می‌کند. این تغییرات فعلاً فقط زیر بخش [Unreleased](CHANGELOG.md) هستند و تا تأیید تست، Tag یا Release جدیدی ساخته نمی‌شود.
