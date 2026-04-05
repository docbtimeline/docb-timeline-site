# Doc B Editorial Image System
## Specification for pipeline integration

---

## The Goal

One distinctive, consistent editorial illustration per article. Automatically generated at pipeline Stage 10 using DALL-E 3. Zero manual effort after setup. Images that help readers remember the mechanism and make the homepage scannable.

Reference aesthetic: The Atlantic, Foreign Affairs, Palladium Magazine — not New Yorker (too handcrafted), not tech blog (too literal), not Substack (too generic).

---

## Why DALL-E 3, Not Midjourney

- Same OpenAI API key the pipeline already uses
- Programmatic — called from Python, no browser, no clicking
- Fixed prompt → consistent style
- Cost: ~$0.04 per image at 1792×1024 (landscape, ideal for og:image)
- Quality is sufficient for editorial thumbnails at web resolution

---

## Three Image Modes

**Mode 1 — Constraint Metaphor** (default)
A single symbolic image representing the binding constraint or its relocation.
Use when: the mechanism is abstract or institutional.
Examples:
- Insurance clause closes a strait → a gate made of contract paper across a waterway
- Export controls optimise what they restrict → a wall that turns into a funnel
- Rare earths running out → a mineral seam visible behind a military silhouette

**Mode 2 — Consequence Portrait**
Shows the actor absorbing the consequence — stylised, symbolic, not literal.
Use when: the human/operational element is the emotional core.
Examples:
- Procurement manager rationing helium allocations → a figure at a desk with dwindling resource icons
- Farmer facing fertiliser costs → agricultural geometry under economic pressure

**Mode 3 — Data/Map Visual**
Simple geographic or quantitative illustration.
Use when: the argument is fundamentally geographic or numerical.
Examples:
- 21% of global oil through a 21-mile strait → minimal map with proportional overlay
- 2,600 GW waiting for transformers → grid diagram with queue visualisation

**Selection rule:** The pipeline LLM (Stage 10) selects the mode based on the article's dominant mechanism. If uncertain, default to Mode 1.

---

## Fixed Style Brief (Append to Every Prompt)

```
Style requirements (non-negotiable):
- Editorial illustration quality, suitable for a serious analytical publication
- Flat design with subtle depth, not photorealistic, not 3D rendered
- Muted, restrained palette: maximum 3-4 colours, no neon, no bright primaries
- Warm light or neutral background — cream, off-white, or pale grey
- Clean composition readable at 300x200px thumbnail
- No text, no numbers, no logos, no faces recognisable as specific people
- No corporate vector infographic look
- No AI slop aesthetics (lens flares, excessive glow, generic tech imagery)
- Inspired by editorial illustration in Foreign Affairs, The Atlantic, Palladium Magazine
- Single dominant visual idea — not a collage
```

---

## Full Prompt Template

```python
IMAGE_PROMPT_TEMPLATE = """
Editorial illustration for an analytical publication called Doc B's Timeline.

Article mechanism: {mechanism_one_sentence}
Constraint type: {constraint_type}
Core image concept: {image_concept}

Style requirements (non-negotiable):
- Editorial illustration quality, suitable for a serious analytical publication
- Flat design with subtle depth, not photorealistic, not 3D rendered
- Muted, restrained palette: maximum 3-4 colours, no neon, no bright primaries
- Warm light or neutral background — cream, off-white, or pale grey
- Clean composition readable at 300x200px thumbnail
- No text, no numbers, no logos, no faces recognisable as specific people
- No corporate vector infographic look
- No AI slop aesthetics (lens flares, excessive glow, generic tech imagery)
- Inspired by editorial illustration in Foreign Affairs, The Atlantic, Palladium Magazine
- Single dominant visual idea — not a collage
"""
```

The LLM generates `image_concept` from the article's `provisional_mechanism.json` before calling the image API.

---

## Pipeline Integration: Stage 10b

Add to `10_package.py` (or new `10b_image_generate.py`):

```python
import openai
import requests
from pathlib import Path

def generate_article_image(
    mechanism: str,
    constraint_type: str,
    article_slug: str,
    site_images_dir: str = "/home/docb/docb-timeline-site/static/images"
) -> str | None:
    """
    Generate editorial illustration for article.
    Returns local path to saved image, or None on failure.
    """
    
    # Step 1: Ask LLM to write the image concept
    concept_prompt = f"""
    Article mechanism: {mechanism}
    
    Write a single sentence describing a symbolic, non-literal visual 
    concept for an editorial illustration of this mechanism. 
    The concept should be abstract and memorable, not a literal depiction.
    Do not include any text, logos, or specific people.
    Output only the concept sentence, nothing else.
    """
    
    concept_response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": concept_prompt}],
        max_tokens=100
    )
    image_concept = concept_response.choices[0].message.content.strip()
    
    # Step 2: Build full prompt
    prompt = IMAGE_PROMPT_TEMPLATE.format(
        mechanism_one_sentence=mechanism,
        constraint_type=constraint_type,
        image_concept=image_concept
    )
    
    # Step 3: Call DALL-E 3
    try:
        response = openai_client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1792x1024",   # landscape, 1.75:1 ratio
            quality="standard", # "hd" costs 2x, not needed
            n=1
        )
        image_url = response.data[0].url
        
        # Step 4: Download and save
        img_path = Path(site_images_dir) / f"{article_slug}.jpg"
        img_path.parent.mkdir(parents=True, exist_ok=True)
        
        img_data = requests.get(image_url, timeout=30).content
        img_path.write_bytes(img_data)
        
        return str(img_path)
        
    except Exception as e:
        print(f"Image generation failed: {e}")
        return None


def add_cover_to_frontmatter(article_path: str, article_slug: str):
    """Add cover.image to article front matter after image is generated."""
    with open(article_path, 'r') as f:
        content = f.read()
    
    cover_line = f'cover:\n  image: "/images/{article_slug}.jpg"\n  alt: ""\n  relative: false\n'
    
    # Insert after opening --- 
    content = content.replace('---\n', f'---\n{cover_line}', 1)
    
    with open(article_path, 'w') as f:
        f.write(content)
```

---

## Cost Per Run

- Image concept (GPT-4o-mini): ~$0.001
- DALL-E 3 image (1792×1024, standard): $0.040
- **Total per article: ~$0.041**
- Monthly at 3 articles/week: ~$0.52/month

Negligible. Add to the pipeline's cost meter.

---

## Hugo Front Matter

After image is generated and saved to `static/images/ARTICLE-SLUG.jpg`, the article front matter gets:

```yaml
cover:
  image: "/images/every-machine-chinas-battery-line.jpg"
  alt: ""
  relative: false
```

PaperMod will then show the cover image on the homepage article list and at the top of the article page.

---

## Human Veto Rule

The pipeline saves the image path to a staging file: `publish/pending_image_SLUG.jpg`

Before `git push`, Doc reviews the image. If it's wrong:
- Delete the file
- Pipeline flags the article as "image pending"
- Next run regenerates with a revised concept prompt

This keeps the human in the loop without adding friction to the normal publish flow.

---

## Retroactive Application to Existing 12 Articles

Run as a one-off script after Stage 10b is built. Feed each article's mechanism description manually or from the mechanism JSON files in the pipeline's run directories. Takes ~5 minutes, costs ~$0.50 total.

---

## What This Solves

1. **Homepage visual hierarchy** — articles with cover images immediately look different from text-only entries. The featured/latest article naturally stands out.
2. **Social sharing** — the cover image becomes the og:image for X cards. Articles shared from X show the illustration, not a blank card.
3. **Brand consistency** — same prompt template, same style brief, same look every time.
4. **Video pipeline alignment** — when Remotion generates scene frames, those can replace or supplement the DALL-E images. Same Hugo cover mechanism, different source.

---

## Implementation Sequence

1. Website improvements deployed (current session)
2. Next pipeline session: build `10b_image_generate.py`
3. Test on one article (the battery article — best content, worth the image)
4. Run retroactively on all 12 existing articles
5. Enable as automatic step in tournament pipeline
