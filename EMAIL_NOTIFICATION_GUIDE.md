# HOW TO SEND EMAIL NOTIFICATIONS VIA BUTTONDOWN
## Permanent reference — save to /home/docb/docb-timeline-site/EMAIL_NOTIFICATION_GUIDE.md

After publishing an article to docbtimeline.com, send an email to all subscribers via Buttondown API.

**Buttondown account:** docb
**Buttondown email:** docb1985@outlook.com
**API docs:** https://api.buttondown.email/v1/

---

## OPTION A: API (preferred — Einy can automate this)

### Setup (one time only)

Get the API key from Buttondown:
1. Log into buttondown.com
2. Go to Settings → API
3. Copy the API key
4. Store it:
```bash
echo 'BUTTONDOWN_API_KEY=your-key-here' >> /home/docb/.openclaw/workspace/polymarket-agents/doc-b-this-timeline/.env
```

### Send an email notification

Use this curl command. Replace the variables.

```bash
curl -X POST https://api.buttondown.email/v1/emails \
  -H "Authorization: Token YOUR_BUTTONDOWN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "ARTICLE_TITLE",
    "body": "EMAIL_BODY_MARKDOWN",
    "status": "draft"
  }'
```

**IMPORTANT:** Set `"status": "draft"` first so Doc can review before sending. Change to `"status": "published"` only after Doc approves, OR Doc can send manually from the Buttondown UI.

### Email body template

The email body is markdown. Use this template:

```markdown
# ARTICLE TITLE

ARTICLE SUBTITLE/DEK

---

FIRST TWO PARAGRAPHS OF THE ARTICLE (copy from the published markdown, approximately 150-200 words — enough to hook, not enough to satisfy)

**[Read the full analysis →](https://docbtimeline.com/posts/SLUG/)**

---

## What to Watch

> COPY THE FIRST PREDICTION from the article's "What to Watch" section — the most specific, falsifiable one.

**[Read the full analysis with all predictions and sources →](https://docbtimeline.com/posts/SLUG/)**

---

*DocB — Timeline: Constraint intelligence for a world where the bottleneck keeps moving.*

*[docbtimeline.com](https://docbtimeline.com) · [@DocbFuture](https://x.com/DocbFuture)*
```

### Example for a real article

```bash
curl -X POST https://api.buttondown.email/v1/emails \
  -H "Authorization: Token $BUTTONDOWN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Every Machine in China'\''s Battery Line Is Chinese",
    "body": "# Every Machine in China'\''s Battery Line Is Chinese\n\nGotion'\''s solid-state battery hits 90% yield while Northvolt, Cellforce, and ACC collapse in sixty days. The chemistry breakthrough arrived in Hefei. The factory didn'\''t.\n\n---\n\nA procurement manager at Volkswagen'\''s Wolfsburg headquarters is sourcing cells for the next ID-series platform. The most competitive bids on her desk come from China — and the gap is widening. Not because European batteries don'\''t exist as a concept, but because every factory that was supposed to make them is now bankrupt, shuttered, or repurposed.\n\n**[Read the full analysis →](https://docbtimeline.com/posts/every-machine-chinas-battery-line/)**\n\n---\n\n*DocB — Timeline: Constraint intelligence for a world where the bottleneck keeps moving.*\n\n*[docbtimeline.com](https://docbtimeline.com) · [@DocbFuture](https://x.com/DocbFuture)*",
    "status": "draft"
  }'
```

### Python script alternative

If curl escaping is too painful, use this Python script:

```python
#!/usr/bin/env python3
"""Send Buttondown email notification for a new article."""
import os
import sys
import json
import requests
from pathlib import Path

def send_notification(title, subtitle, slug, first_paragraphs, prediction=None):
    api_key = os.environ.get('BUTTONDOWN_API_KEY')
    if not api_key:
        print("❌ BUTTONDOWN_API_KEY not set in environment")
        sys.exit(1)
    
    article_url = f"https://docbtimeline.com/posts/{slug}/"
    
    # Build email body
    body_parts = [
        f"# {title}",
        f"",
        f"{subtitle}",
        f"",
        f"---",
        f"",
        first_paragraphs,
        f"",
        f"**[Read the full analysis →]({article_url})**",
        f"",
        f"---",
    ]
    
    if prediction:
        body_parts.extend([
            f"",
            f"## What to Watch",
            f"",
            f"> {prediction}",
            f"",
            f"**[Read the full analysis with all predictions and sources →]({article_url})**",
            f"",
            f"---",
        ])
    
    body_parts.extend([
        f"",
        f"*DocB — Timeline: Constraint intelligence for a world where the bottleneck keeps moving.*",
        f"",
        f"*[docbtimeline.com](https://docbtimeline.com) · [@DocbFuture](https://x.com/DocbFuture)*",
    ])
    
    body = "\n".join(body_parts)
    
    response = requests.post(
        "https://api.buttondown.email/v1/emails",
        headers={
            "Authorization": f"Token {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "subject": title,
            "body": body,
            "status": "draft",  # ALWAYS draft first
        }
    )
    
    if response.status_code in (200, 201):
        print(f"✅ Email draft created: '{title}'")
        print(f"   Go to buttondown.com/emails to review and send")
    else:
        print(f"❌ Failed: {response.status_code}")
        print(f"   {response.text}")

if __name__ == "__main__":
    # Example usage — replace with actual article content
    send_notification(
        title="Article Title Here",
        subtitle="The subtitle/dek",
        slug="article-slug-here",
        first_paragraphs="First paragraph of article...\n\nSecond paragraph...",
        prediction="By Q3 2026, specific thing will happen. Kill signal: if X occurs instead."
    )
```

Save as `/home/docb/docb-timeline-site/tools/send_email.py`

---

## OPTION B: Manual (fallback — Doc does this in browser)

1. Go to buttondown.com → Emails → New Email
2. Subject: Article title
3. Body: Paste the email template above (with article content filled in)
4. Preview → Send

---

## EMAIL DESIGN RULES

- **Subject line:** The article title only. No "[DocB-Timeline]" prefix, no emoji, no "New post:" — just the title.
- **Body structure:** Title → subtitle → first 2 paragraphs → link → prediction teaser → link → footer
- **Tone:** The email is a teaser, not the full article. Give the reader enough to understand the mechanism, then drive them to the site.
- **Length:** 200-300 words max in the email body (excluding the article excerpt). The article is on the website.
- **Footer:** Always includes docbtimeline.com link and @DocbFuture.
- **Never:** Include the full article in the email. The point is to drive traffic to the website.
- **Never:** Use Substack. It is suspended and we do not use it.

---

## FULL PUBLISHING CHECKLIST

After the pipeline produces an article and Doc approves it:

```
□ 1. Create content/posts/SLUG.md with front matter
□ 2. Run: hugo (verify no errors)
□ 3. Run: git add -A && git commit -m "Publish: Title" && git push
□ 4. Wait 3 min, verify live at docbtimeline.com/posts/SLUG/
□ 5. Send Buttondown email draft via API or tools/send_email.py
□ 6. Doc reviews email draft at buttondown.com, hits Send
□ 7. Promote on X (separate step)
```
