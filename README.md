# Data Extraction & Validation with Regex (README)

## Overview

This project demonstrates **data extraction** using regular expressions and **defensive input validation** using Python. The goal is **not** to build a full security system, but to show awareness of **adversarial input**, malformed data, and realistic constraints.

The workflow is intentionally split into two phases:

1. **Extraction** — find _candidates_ in raw text using regex
2. **Validation** — decide which candidates are _plausible_ and safe

This mirrors real-world systems where pattern matching alone is insufficient.

---

## Why Separate Extraction and Validation?

Regex is good at answering:

> “Does this text _look like_ a thing?”

Validation is good at answering:

> “Does this _make sense_ as a real thing?”

Example:

- `8-888-888-888` **matches** a phone-like pattern
- Validation rejects it as unrealistic

This separation demonstrates **defensive thinking**, as required by the assignment.

---

## What Is Extracted?

The program scans input text and extracts:

- Times (12h / 24h formats)
- URLs
- Hashtags
- Phone numbers
- Currency amounts
- HTML tags

Each category has:

- A **regex extractor**
- A **validator function** (where needed)

---

## Time Extraction

Supported formats:

- `23:59`
- `11:30 AM`
- `09:05 pm`

Validation is mostly handled by the regex itself:

- Hours constrained (0–23 or 1–12)
- Minutes constrained (00–59)

This avoids invalid times like `25:99`.

---

## URL Extraction & Validation

Extraction focuses on structure:

- Must start with `http://` or `https://`
- Excludes spaces and dangerous characters (`< > "`)

Validation adds realism:

- Rejects URLs that are too short to be plausible

Example:

- `https://a.co` → valid
- `http://x` → rejected

> Note: `www.example.com` is _not_ treated as a URL here because it lacks a scheme.

---

## Hashtags

Extraction:

- `#` followed by letters, numbers, or `_`

Validation:

- Rejects excessively long hashtags

This prevents abuse like:

```
#aaaaaaaaaaaaaaaaaaaaaa...
```

---

## Phone Numbers

Extraction:

- Allows digits, spaces, dashes, optional `+`

Validation:

- Normalizes to digits only
- Enforces realistic length (8–15 digits)
- Rejects:
  - Repeated digits (`1111111111`)
  - Simple sequences (`1234567890`)

- Masks output for privacy

Example output:

```
********1234
```

---

## Currency Amounts

Extraction allows flexible formats:

- `$12.50`
- `12,000€`
- `₹ 1,234.00`

Validation rejects malformed numbers:

- Multiple commas in wrong positions (`12,3,4`)
- Multiple decimal points (`12..87`)

This prevents partial or misleading matches.

---

## HTML Tags

HTML tags are extracted **as plain text only**.

They are **not parsed or executed**.

Reason:

- Prevent accidental execution
- Demonstrate awareness of **XSS (Cross-Site Scripting)** risks

Treating HTML as plain text is a safe default in extraction tasks.

---

## Output

Validated results are written to `outputs.txt`, grouped by category.

This makes the pipeline clear:

```
Input Text → Extraction → Validation → Output File
```

---

## Key Takeaway

This project shows:

- Regex alone is not enough
- Validation logic must be explicit
- Adversarial input is expected
- Safe handling matters more than perfect matching

That is exactly what the assignment asks for.

---

## Final Note

The system does **not** claim data is real.
It only claims:

> “This looks plausible enough to keep.”

That distinction is the heart of defensive programming.
