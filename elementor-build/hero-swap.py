#!/usr/bin/env python3
"""
hero-swap.py
------------
Reads the current Elementor page data, replaces the hero container (id 3oond57)
with a new container housing the 3D hero HTML widget, and writes the result.

Input files:
  - Elementor JSON: tool-results/toolu_01CaMZqTMTA9dHU8HmWyr96k.json
    (JSON array with one element whose "text" field holds the double-escaped
     Elementor data string)
  - Hero HTML: /home/user/DRLoukas/hero-3d.html

Output:
  - /home/user/DRLoukas/elementor-build/hero-swap-data.json
    (The parsed list of Elementor containers as clean JSON)
"""

import json
import re
import os

# ── Paths ──────────────────────────────────────────────────────────────────────
ELEMENTOR_SOURCE = (
    "/root/.claude/projects/-home-user-DRLoukas/"
    "b93e6ed3-77fd-5a2b-b0f3-898bb442bd92/"
    "tool-results/toolu_01CaMZqTMTA9dHU8HmWyr96k.json"
)
HERO_HTML_PATH = "/home/user/DRLoukas/hero-3d.html"
OUTPUT_PATH = "/home/user/DRLoukas/elementor-build/hero-swap-data.json"

HERO_CONTAINER_ID = "3oond57"


def load_elementor_data(path):
    """Parse the wrapper JSON and extract the Elementor container list."""
    with open(path, "r", encoding="utf-8") as f:
        wrapper = json.load(f)
    # wrapper is [{type: "text", text: "<escaped JSON string>"}]
    text_val = wrapper[0]["text"]
    # text_val is a JSON-encoded string, so one json.loads gives us the raw
    # Elementor JSON string, and a second gives us the Python list.
    inner_str = json.loads(text_val)
    return json.loads(inner_str)


def load_hero_html(path):
    """Read the hero HTML and strip the <title> tag and below-fold section."""
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Remove the <title>...</title> tag
    html = re.sub(r"<title>.*?</title>\s*", "", html, flags=re.DOTALL)

    # Remove .below-fold CSS rules from the <style> block
    # Matches ".below-fold {" or ".below-fold h2 {" etc. through closing "}"
    html = re.sub(
        r"\s*\.below-fold[^{]*\{[^}]*\}\s*", "\n", html, flags=re.DOTALL
    )

    # Remove <div class="below-fold"> and everything after it (the HTML element)
    below_fold_pattern = r'\s*<div\s+class="below-fold"[^>]*>.*'
    html = re.sub(below_fold_pattern, "", html, flags=re.DOTALL)

    # Trim trailing whitespace
    html = html.rstrip()

    return html


def make_hero_container(hero_html):
    """Build the replacement Elementor container with an HTML widget."""
    return {
        "id": HERO_CONTAINER_ID,
        "elType": "container",
        "settings": {
            "content_width": "full",
            "padding": {
                "unit": "px",
                "top": "0",
                "right": "0",
                "bottom": "0",
                "left": "0",
                "isLinked": True,
            },
            "margin": {
                "unit": "px",
                "top": "0",
                "right": "0",
                "bottom": "0",
                "left": "0",
                "isLinked": True,
            },
        },
        "elements": [
            {
                "id": "hero3d_html",
                "elType": "widget",
                "settings": {
                    "html": hero_html,
                },
                "elements": [],
                "widgetType": "html",
            }
        ],
        "isInner": False,
    }


def main():
    # 1. Load the current Elementor data
    elementor_data = load_elementor_data(ELEMENTOR_SOURCE)
    print(f"Loaded {len(elementor_data)} top-level containers")

    # 2. Find the hero container index
    hero_idx = None
    for i, container in enumerate(elementor_data):
        if container.get("id") == HERO_CONTAINER_ID:
            hero_idx = i
            break

    if hero_idx is None:
        raise ValueError(
            f"Could not find container with id '{HERO_CONTAINER_ID}' "
            f"in the Elementor data"
        )
    print(f"Found hero container at index {hero_idx} (id={HERO_CONTAINER_ID})")

    # 3. Load and clean the hero HTML
    hero_html = load_hero_html(HERO_HTML_PATH)
    print(f"Loaded hero HTML ({len(hero_html)} chars, title and below-fold removed)")

    # 4. Build the replacement container
    new_container = make_hero_container(hero_html)

    # 5. Swap it in
    elementor_data[hero_idx] = new_container
    print(f"Replaced container at index {hero_idx}")

    # 6. Write the output
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(elementor_data, f, indent=2, ensure_ascii=False)

    output_size = os.path.getsize(OUTPUT_PATH)
    print(f"Wrote {OUTPUT_PATH} ({output_size:,} bytes)")
    print("Done.")


if __name__ == "__main__":
    main()
