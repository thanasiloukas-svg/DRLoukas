#!/usr/bin/env python3
"""
Fix pass #2 — addresses user feedback from mobile screenshots:
1. Hero: ceiling tiles visible → reposition bg for mobile, use dark glass card
2. Dental Crowns tile: clinical B&A with watermark → swap image
3. B&A implant image: too clinical (abutment visible) → swap image
4. Dead space on mobile: reduce section gaps + tile gaps
5. Colors: washed-out glass card → dark frosted glass, richer overall feel
6. Service tiles on mobile: make them full-width single column for readability
"""
import json, copy

INPUT = "elementor-compact.json"

with open(INPUT) as f:
    data = json.load(f)

def find_by_id(elements, target_id):
    for el in elements:
        if el.get("id") == target_id:
            return el
        found = find_by_id(el.get("elements", []), target_id)
        if found:
            return found
    return None

def find_all_by_type(elements, widget_type):
    results = []
    for el in elements:
        if el.get("widgetType") == widget_type:
            results.append(el)
        results.extend(find_all_by_type(el.get("elements", []), widget_type))
    return results

# ─── 1. HERO: Fix background position for mobile ───
hero = find_by_id(data, "3oond57")
if hero:
    s = hero["settings"]
    # Show reception desk on mobile, not ceiling tiles
    s["background_position_mobile"] = "center 80%"
    # Reduce hero height on mobile to be tighter
    s["min_height_mobile"] = {"size": 0, "unit": "px"}
    # Reduce top padding on mobile (less dead space above glass card)
    s["padding_mobile"] = {"unit": "px", "top": "30", "right": "16", "bottom": "40", "left": "16", "isLinked": False}

# ─── 2. GLASS CARD: Dark frosted glass instead of washed-out white ───
glass = find_by_id(data, "gckvbho")
if glass:
    s = glass["settings"]
    # Dark navy frosted glass — much more premium than white
    s["background_color"] = "rgba(6,32,45,0.65)"
    s["custom_css"] = "selector{backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);border:1px solid rgba(255,255,255,.15)}"
    # Tighter padding on mobile
    s["padding_mobile"] = {"unit": "px", "top": "24", "right": "16", "bottom": "24", "left": "16", "isLinked": False}
    # Smaller gap
    s["gap"] = {"size": 12, "unit": "px"}

# ─── 3. HERO: Adjust text elements for dark glass ───
# "PARK RIDGE, ILLINOIS" eyebrow — brighter on dark glass
eyebrow = find_by_id(data, "h3r0eyb")
if eyebrow:
    eyebrow["settings"]["editor"] = '<p style="text-transform:uppercase;letter-spacing:4px;font-size:11px;color:rgba(255,255,255,.7);margin-bottom:0">PARK RIDGE, ILLINOIS</p>'

# H1 — slightly smaller on mobile to reduce card height
h1 = find_by_id(data, "ohgi1jn")
if h1:
    h1["settings"]["typography_font_size_mobile"] = {"size": 24, "unit": "px"}

# Description — slightly smaller to reduce card height
desc = find_by_id(data, "yt7rpwh")
if desc:
    desc["settings"]["editor"] = '<p style="font-size:15px;line-height:1.5;color:rgba(255,255,255,.85)">Advanced implants, Invisalign, cosmetic dentistry &amp; facial aesthetics — personalized care with 20+ years of experience.</p>'

# Phone — keep prominent
phone = find_by_id(data, "h3r0phn")
if phone:
    phone["settings"]["editor"] = '<p><a href="tel:8476961919" style="color:#18C6B3;font-size:20px;font-weight:700;text-decoration:none;letter-spacing:0.5px">(847) 696-1919</a></p>'

# ─── 4. SERVICE TILES: Full-width on mobile (single column), reduce gap ───
tiles_container = find_by_id(data, "ju6n37r")
if tiles_container:
    s = tiles_container["settings"]
    s["gap_mobile"] = {"size": 12, "unit": "px"}

# Each service tile: full width on mobile for readability
tile_ids = ["5zh3yik", "52t7j5o", "pn5myy8", "i4moeta", "00qtww1", "pnu8vk1"]
for tid in tile_ids:
    tile = find_by_id(data, tid)
    if tile:
        s = tile["settings"]
        # Full width single column on mobile — much more readable
        s["width_mobile"] = {"size": 100, "unit": "%"}
        s["min_height_mobile"] = {"size": 180, "unit": "px"}

# ─── 5. DENTAL CROWNS TILE: Swap image ───
crowns_tile = find_by_id(data, "00qtww1")
if crowns_tile:
    s = crowns_tile["settings"]
    # Use the Instagram porcelain crowns result — polished, no watermark
    s["background_image"] = {
        "url": "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-instagram-porcelain-crowns-result.webp",
        "id": 2621
    }

# ─── 6. B&A DENTAL IMPLANT: Swap clinical image ───
implant_ba = find_by_id(data, "hy9ap7k")
if implant_ba:
    # Find the image widget inside
    for child in implant_ba.get("elements", []):
        if child.get("widgetType") == "image":
            child["settings"]["image"] = {
                "url": "https://www.drloukas.com/wp-content/uploads/2026/06/dental-implants-before-after-loukas-dentistry-park-ridge.jpg",
                "id": 2732
            }
            break

# ─── 7. REDUCE DEAD SPACE: Tighten section padding on mobile ───
sections_to_tighten = {
    "66rgciq": {"top": "40", "right": "16", "bottom": "40", "left": "16"},  # Services
    "zw1vmbm": {"top": "40", "right": "16", "bottom": "40", "left": "16"},  # About
    "gtxdea4": {"top": "40", "right": "16", "bottom": "40", "left": "16"},  # B&A
    "y9np516": {"top": "40", "right": "16", "bottom": "40", "left": "16"},  # Team
    "m09c307": {"top": "40", "right": "16", "bottom": "40", "left": "16"},  # Testimonials
    "ey91tlh": {"top": "40", "right": "16", "bottom": "40", "left": "16"},  # FAQ
    "37h56k3": {"top": "40", "right": "16", "bottom": "40", "left": "16"},  # Contact
}
for sec_id, padding in sections_to_tighten.items():
    sec = find_by_id(data, sec_id)
    if sec:
        sec["settings"]["padding_mobile"] = {
            "unit": "px", "isLinked": False,
            **padding
        }

# Also reduce the gap between elements within sections on mobile
sections_with_gap = ["66rgciq", "gtxdea4", "y9np516", "m09c307", "ey91tlh"]
for sec_id in sections_with_gap:
    sec = find_by_id(data, sec_id)
    if sec:
        sec["settings"]["gap_mobile"] = {"size": 24, "unit": "px"}

# ─── 8. SERVICES SECTION: Reduce heading gap ───
services_section = find_by_id(data, "66rgciq")
if services_section:
    s = services_section["settings"]
    s["gap"] = {"size": 30, "unit": "px"}

# ─── 9. B&A CARDS: Tighter layout on mobile ───
ba_container = find_by_id(data, "2o2adqd")
if ba_container:
    ba_container["settings"]["gap_mobile"] = {"size": 16, "unit": "px"}

# ─── 10. TEAM CARDS: Tighter mobile gap ───
team_container = find_by_id(data, "hw1caep")
if team_container:
    team_container["settings"]["gap_mobile"] = {"size": 16, "unit": "px"}

# ─── 11. TESTIMONIALS: Tighter mobile gap ───
test_container = find_by_id(data, "e3cm887")
if test_container:
    test_container["settings"]["gap_mobile"] = {"size": 16, "unit": "px"}

# ─── 12. TRUST STRIP: Tighter padding ───
trust = find_by_id(data, "tr5tstr")
if trust:
    s = trust["settings"]
    s["padding"] = {"unit": "px", "top": "0", "right": "20", "bottom": "0", "left": "20", "isLinked": False}

# ─── 13. COMMUNITIES SECTION: Tighter ───
comm = find_by_id(data, "z7y7ann")
if comm:
    s = comm["settings"]
    s["padding"] = {"unit": "px", "top": "30", "right": "20", "bottom": "30", "left": "20", "isLinked": False}
    s["padding_mobile"] = {"unit": "px", "top": "20", "right": "16", "bottom": "70", "left": "16", "isLinked": False}

# ─── 14. ABOUT SECTION: Tighter gap on mobile ───
about = find_by_id(data, "zw1vmbm")
if about:
    about["settings"]["gap_mobile"] = {"size": 24, "unit": "px"}

# ─── Write output ───
with open(INPUT, "w") as f:
    json.dump(data, f, separators=(",", ":"), ensure_ascii=False)

print(f"Fix-v2 complete: {len(data)} sections")
print(f"File size: {len(json.dumps(data, separators=(',',':'), ensure_ascii=False)):,} bytes")

# Verify
checks = [
    ("Hero bg position mobile", lambda: find_by_id(data, "3oond57")["settings"].get("background_position_mobile") == "center 80%"),
    ("Dark glass card", lambda: "6,32,45,0.65" in find_by_id(data, "gckvbho")["settings"]["background_color"]),
    ("Glass blur 24px", lambda: "blur(24px)" in find_by_id(data, "gckvbho")["settings"]["custom_css"]),
    ("Service tiles full-width mobile", lambda: find_by_id(data, "5zh3yik")["settings"]["width_mobile"]["size"] == 100),
    ("Crowns tile new image", lambda: "porcelain-crowns-result" in find_by_id(data, "00qtww1")["settings"]["background_image"]["url"]),
    ("B&A implant new image", lambda: "dental-implants-before-after-loukas" in str(find_by_id(data, "hy9ap7k"))),
    ("Services gap reduced", lambda: find_by_id(data, "66rgciq")["settings"]["gap"]["size"] == 30),
    ("Mobile padding tightened", lambda: find_by_id(data, "66rgciq")["settings"]["padding_mobile"]["top"] == "40"),
    ("Tile gap mobile", lambda: find_by_id(data, "ju6n37r")["settings"]["gap_mobile"]["size"] == 12),
    ("Trust strip tighter", lambda: find_by_id(data, "tr5tstr")["settings"]["padding"]["right"] == "20"),
]

for label, check in checks:
    try:
        ok = check()
        print(f"  {'OK' if ok else 'FAIL'}: {label}")
    except Exception as e:
        print(f"  FAIL: {label} — {e}")
