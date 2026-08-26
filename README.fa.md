# مهارت معماری اطلاعات ProPaymun

یک Agent Skill برای کمک به مدیران محصول، طراحان محصول، پژوهشگران، بنیان‌گذاران و تیم‌های محصول تا با کمک AI معماری اطلاعات حرفه‌ای، شواهدمحور و قابل‌اعتبارسنجی بسازند.

**ProPaymun — پروپیمان** در فارسی یعنی کامل، پُر و لبریز. هدف پروژه این است که خروجی تا جای ممکن کامل و قابل‌استفاده باشد، بدون اینکه مجهولات را به‌جای واقعیت نشان دهد.

[English](README.md)

## قابلیت‌ها

این مهارت برای طراحی از صفر، بازطراحی و درخواست‌های محدود به یک خروجی قابل‌استفاده است:

- تعریف و ممیزی IA
- مدل اشیا و دامنه
- Taxonomy و سیستم برچسب‌گذاری
- Navigation و Search
- نقش‌ها، مجوزها و Visibility
- گزینه‌های معماری و دلیل انتخاب
- برنامه اعتبارسنجی، سنجه‌ها و Governance
- مدل معنایی JSON، Mermaid، HTML و راهنمای خروجی Draw.io یا Excalidraw

مهارت دو مسیر پیش‌فرض دارد:

- **Guided:** کشف مرحله‌ای با نقاط تأیید انسانی؛
- **Quick Draft:** نسخهٔ اولیهٔ سریع با فرض‌ها و مجهولات مشخص.

کاربر می‌تواند ترتیب، سؤال‌ها، نقاط توقف، عمق و فرمت خروجی را آزادانه تغییر دهد یا فقط یک artifact بخواهد.

## نصب سریع

### نصب عمومی

```bash
npx skills add https://github.com/kamroncorp/propaymun-information-architecture-skill
```

### Claude Code

مخزن را در مسیر زیر clone یا copy کنید:

```text
~/.claude/skills/propaymun-information-architecture/
```

### Codex

```text
~/.codex/skills/propaymun-information-architecture/
```

### Gemini CLI

```bash
gemini skills install https://github.com/kamroncorp/propaymun-information-architecture-skill
```

### Figma agent و Figma Make

فایل زیر را به‌عنوان Custom Skill آپلود کنید:

```text
adapters/figma-make/propaymun-information-architecture.md
```

Figma در آپلود مستقیم Custom Skill فقط فایل Markdown واحد را می‌پذیرد؛ به همین دلیل نسخهٔ مخصوص Figma همهٔ منابع لازم را داخل یک فایل قرار می‌دهد.

## مثال استفاده

```text
با Guided Mode برای یک پلتفرم آموزشی چندنقشی معماری اطلاعات کامل طراحی کن.
```

```text
این ساختار فعلی و خلاصه Search Log ماست. IA را ممیزی کن و دو گزینه جایگزین بده.
```

```text
فقط Taxonomy و سیستم برچسب‌گذاری این inventory را بساز. خروجی Markdown و Mermaid باشد.
```

## رفتار پیش‌فرض

اگر کاربر فرمت تعیین نکند، خروجی سریع و حرفه‌ای `Markdown + Mermaid` است. در صورت درخواست می‌توان HTML مستقل، Draw.io، Excalidraw، SVG، PNG یا PDF نیز تولید کرد؛ البته در صورتی که محیط عامل ابزار لازم را داشته باشد.

مهارت میان این وضعیت‌ها تفاوت می‌گذارد:

- Provided
- Observed
- Confirmed
- Inferred
- Proposed
- Unknown

خروجی تولیدشده توسط AI بدون پژوهش کاربر «فرضیه معماری» است، نه IA اعتبارسنجی‌شده.

## توسعه و تست

```bash
python -m unittest discover -s tests -v
python scripts/validate_ia_model.py path/to/ia.json
python scripts/render_ia_html.py path/to/ia.json -o ia.html
python scripts/package_figma.py
```

## مجوز

این پروژه تحت مجوز Apache License 2.0 منتشر می‌شود.

