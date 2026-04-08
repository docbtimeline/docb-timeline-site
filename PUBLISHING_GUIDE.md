# HOW TO PUBLISH AN ARTICLE ON DOCBTIMELINE.COM
## Permanent reference — save to /home/docb/docb-timeline-site/PUBLISHING_GUIDE.md

**READ THIS EVERY TIME BEFORE PUBLISHING. DO NOT DEVIATE.**

We publish on our OWN website. NOT Substack. NOT any other platform.
- Website: https://docbtimeline.com
- Hosted: GitHub Pages
- Built with: Hugo (static site generator)
- Repo: /home/docb/docb-timeline-site/

---

## STEP 1: Create the article markdown file

Create a new file at:
```
/home/docb/docb-timeline-site/content/posts/SLUG.md
```

The SLUG is a short URL-friendly version of the title. Rules:
- All lowercase
- Hyphens instead of spaces
- No special characters, no apostrophes, no colons
- Short: 3-6 words
- Example: "Every Machine in China's Battery Line Is Chinese" → `every-machine-chinas-battery-line`

## STEP 2: Add Hugo front matter

Every article MUST start with this front matter block. Nothing publishes without it.

```yaml
---
title: "The Full Article Title Here"
description: "One-sentence subtitle/dek that appears in article cards and search results"
date: 2026-04-08
draft: false
tags: ["energy", "geopolitics", "shipping"]
author: "DocB"
showToc: true
TocOpen: false
---
```

### Front matter rules:
- **title**: The full headline. Use straight quotes, not curly.
- **description**: The subtitle/dek. One sentence. This appears on the homepage card, in RSS, and in search results. Make it count.
- **date**: YYYY-MM-DD format. Use today's date.
- **draft**: Must be `false` to publish. Set to `true` if you want to preview without publishing.
- **tags**: Lowercase, from this approved list. Use 2-4 tags per article:
  - `energy`, `shipping`, `iran`, `china`, `semiconductors`, `ai`, `defense`, `manufacturing`, `critical-minerals`, `batteries`, `eu`, `geopolitics`, `export-controls`, `infrastructure`
  - New tags are OK if genuinely needed, but prefer existing ones.
- **author**: Always `"DocB"` (not "Doc B", not "DocB — Timeline")
- **showToc**: `true` — readers can optionally expand a table of contents
- **TocOpen**: `false` — TOC starts collapsed

## STEP 3: Add the article body

After the front matter closing `---`, paste the full article text in markdown.

### Formatting rules:
- Use `##` for section headings (H2). Never H1 — the title is H1.
- Use `**bold**` sparingly for key actors or numbers on first mention.
- Use `*italic*` for emphasis in prose.
- Blockquotes (`>`) for key predictions or the "What to Watch" section.
- Sources go at the bottom under a `## Sources` heading.
- Source format: `*Source label:* [Display Name](URL)` — one per line.
- NO pipeline internals in the article text. No "Cluster 1", "convergence score", "tournament winner".
- NO "Subscribe to our newsletter" or CTA text in the article body — the site template handles this.

### Example article structure:
```markdown
---
title: "The Title"
description: "The subtitle"
date: 2026-04-08
draft: false
tags: ["energy", "shipping"]
author: "DocB"
showToc: true
TocOpen: false
---

Opening paragraph with a specific person, place, or price...

## Section heading

Body paragraphs...

## Another section

More body...

## What to Watch

> **Prediction 1 (by DATE):** Specific falsifiable claim. Kill signal: what would prove this wrong.

> **Prediction 2 (by DATE):** Another specific claim.

## Sources

*Energy markets:* [Reuters](https://url), [Bloomberg](https://url)

*Shipping data:* [FreightWaves](https://url), [Lloyd's List](https://url)
```

## STEP 4: Build the site

```bash
cd /home/docb/docb-timeline-site
hugo
```

**VERIFY:** Output says "Built in XXms" with NO error lines.
**VERIFY:** The page count increased by at least 1 from last build.

If there are errors, the most common cause is bad front matter YAML (missing quotes, wrong indentation, tab characters). Fix and rebuild.

## STEP 5: Preview locally (optional but recommended)

```bash
hugo server -D
```
Then open http://localhost:1313 in a browser. Check:
- Article appears in the list
- Title and description look correct
- Tags are clickable
- Body text renders properly
- Sources are linked

Press Ctrl+C to stop the preview server.

## STEP 6: Push to GitHub (deploys to live site)

```bash
cd /home/docb/docb-timeline-site
git add -A
git commit -m "Publish: Article Title Here"
git push
```

**VERIFY:** `git push` returns no errors.

The site goes live within 2-5 minutes after push (GitHub Pages rebuild time).

**VERIFY after 3 minutes:** Open `https://docbtimeline.com/posts/SLUG/` in a browser and confirm the article is live.

## STEP 7: Send email notification via Buttondown

See separate file: `EMAIL_NOTIFICATION_GUIDE.md`

## STEP 8: Promote on X

This is a separate manual step or uses `tools/promote_article.py`. Not covered here.

---

## COMMON MISTAKES — DO NOT MAKE THESE

1. **Publishing to Substack** — Substack is SUSPENDED. We do NOT use it. Ever.
2. **Forgetting front matter** — Hugo will not render the page correctly without the YAML block.
3. **Wrong path** — Articles go in `/home/docb/docb-timeline-site/content/posts/` NOT in the pipeline directory.
4. **Forgetting to run `hugo`** — The `git push` deploys what's in the `docs/` folder. If you don't run `hugo` first, you push stale content.
5. **Wrong date format** — Must be `YYYY-MM-DD`. Not `DD/MM/YYYY`. Not spelled out.
6. **Tabs in YAML** — YAML uses spaces only. Tabs break everything.
7. **Duplicate slug** — Check `ls content/posts/` before creating. Don't overwrite existing articles.

---

## FILE LOCATIONS

| What | Where |
|------|-------|
| Site repo root | `/home/docb/docb-timeline-site/` |
| Articles | `/home/docb/docb-timeline-site/content/posts/` |
| Static images | `/home/docb/docb-timeline-site/static/images/` |
| Hugo config | `/home/docb/docb-timeline-site/hugo.toml` |
| CSS overrides | `/home/docb/docb-timeline-site/assets/css/extended/` |
| Built site (deployed) | `/home/docb/docb-timeline-site/docs/` |
| Pipeline output | `/home/docb/.openclaw/workspace/polymarket-agents/doc-b-this-timeline/logs/runs/*/` |
| Pipeline final article | `[run dir]/publish/final_article.md` or `[run dir]/final_article.md` |
