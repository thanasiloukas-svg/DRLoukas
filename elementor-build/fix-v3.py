#!/usr/bin/env python3
"""
Fix pass #3 — Major visual overhaul to match Manus reference design.

Key design principles from the reference:
1. White backgrounds for most sections (clean, not dark everywhere)
2. Teal (#18C6B3) section headings with short underline bars
3. Full-width teal CTA banner instead of dark trust strip
4. Dark navy cards ONLY for specific card elements (not section bgs)
5. Cleaner, more spacious layout with better photo presentation
6. Stats on white/light background with teal accent numbers
7. Section headings centered with decorative underline
"""
import json

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


# ══════════════════════════════════════════════════════════════
# 1. HERO — Match Manus: left-aligned text, reception desk bg,
#    teal eyebrow, large heading with teal accent, clean buttons
# ══════════════════════════════════════════════════════════════

hero = find_by_id(data, "3oond57")
if hero:
    s = hero["settings"]
    # Darken the overlay slightly more for text readability
    s["background_overlay_color"] = "rgba(6,32,45,0.15)"
    s["background_overlay_color_b"] = "rgba(6,32,45,0.70)"
    # Left-align content on mobile, center on desktop
    s["flex_align_items"] = "flex-start"
    s["flex_justify_content"] = "center"
    # More breathing room
    s["min_height"] = {"size": 70, "unit": "vh"}
    s["padding"] = {"unit": "px", "top": "120", "right": "40", "bottom": "100", "left": "40", "isLinked": False}
    s["padding_mobile"] = {"unit": "px", "top": "60", "right": "20", "bottom": "60", "left": "20", "isLinked": False}
    # Better mobile bg position — show reception desk area
    s["background_position_mobile"] = "center 70%"

# Glass card — make it more subtle, not so heavy
glass = find_by_id(data, "gckvbho")
if glass:
    s = glass["settings"]
    # Lighter, more elegant overlay — dark but not opaque
    s["background_color"] = "rgba(6,32,45,0.55)"
    s["custom_css"] = "selector{backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,.12);border-radius:16px}"
    s["padding"] = {"unit": "px", "top": "40", "right": "36", "bottom": "40", "left": "36", "isLinked": False}
    s["padding_mobile"] = {"unit": "px", "top": "28", "right": "20", "bottom": "28", "left": "20", "isLinked": False}
    s["gap"] = {"size": 14, "unit": "px"}

# Eyebrow — "PARK RIDGE, IL — ACCEPTING NEW PATIENTS" (matching Manus)
eyebrow = find_by_id(data, "h3r0eyb")
if eyebrow:
    eyebrow["settings"]["editor"] = '<p style="text-transform:uppercase;letter-spacing:3px;font-size:12px;color:#18C6B3;margin-bottom:0;font-weight:600">PARK RIDGE, IL &mdash; ACCEPTING NEW PATIENTS</p>'

# H1 — Larger, bolder, with teal accent for location
h1 = find_by_id(data, "ohgi1jn")
if h1:
    s = h1["settings"]
    s["title"] = "Your Family Dentist in Park Ridge"
    s["title_color"] = "#FFFFFF"
    s["typography_font_size"] = {"size": 44, "unit": "px"}
    s["typography_font_size_mobile"] = {"size": 32, "unit": "px"}
    s["typography_font_weight"] = "700"
    s["typography_line_height"] = {"size": 1.15, "unit": "em"}
    s["align"] = "left"
    s["align_mobile"] = "left"

# Description
desc = find_by_id(data, "yt7rpwh")
if desc:
    desc["settings"]["editor"] = '<p style="font-size:16px;line-height:1.6;color:rgba(255,255,255,.88);max-width:520px">Two generations of dental excellence. Drs. Thanasi &amp; Maria Loukas have been caring for Park Ridge families for over 40 years &mdash; from first cleanings to dental implants, Invisalign, and complete smile transformations.</p>'

# Phone number — bigger, bolder
phone = find_by_id(data, "h3r0phn")
if phone:
    phone["settings"]["editor"] = '<p><a href="tel:8476961919" style="color:#18C6B3;font-size:22px;font-weight:700;text-decoration:none;letter-spacing:0.5px">(847) 696-1919</a></p>'

# CTA buttons — match Manus style
call_btn = find_by_id(data, "6nnyfx4")
if call_btn:
    s = call_btn["settings"]
    s["text"] = "Call (847) 696-1919"
    s["link"] = {"url": "tel:8476961919"}
    s["button_text_color"] = "#06202D"
    s["background_color"] = "#FFFFFF"
    s["border_radius"] = {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True}
    s["typography_font_weight"] = "600"
    s["typography_font_size"] = {"size": 15, "unit": "px"}

gallery_btn = find_by_id(data, "m8t1qoj")
if gallery_btn:
    s = gallery_btn["settings"]
    s["text"] = "View Our Gallery"
    s["button_text_color"] = "#FFFFFF"
    s["background_color"] = "transparent"
    s["border_border"] = "solid"
    s["border_width"] = {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True}
    s["border_color"] = "rgba(255,255,255,.5)"
    s["border_radius"] = {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True}
    s["typography_font_weight"] = "600"


# ══════════════════════════════════════════════════════════════
# 2. TRUST STRIP → TEAL CTA BANNER
#    Replace dark navy trust strip with full-width teal banner
# ══════════════════════════════════════════════════════════════

trust = find_by_id(data, "tr5tstr")
if trust:
    s = trust["settings"]
    s["background_color"] = "#18C6B3"
    s["flex_direction"] = "row"
    s["flex_justify_content"] = "center"
    s["flex_align_items"] = "center"
    s["padding"] = {"unit": "px", "top": "16", "right": "20", "bottom": "16", "left": "20", "isLinked": False}
    s["padding_mobile"] = {"unit": "px", "top": "14", "right": "16", "bottom": "14", "left": "16", "isLinked": False}
    s["gap"] = {"size": 0, "unit": "px"}

    # Replace child containers with a single CTA text
    # Remove existing children and replace
    trust["elements"] = [{
        "id": "ctabn01",
        "elType": "widget",
        "widgetType": "text-editor",
        "settings": {
            "editor": '<p style="margin:0;text-align:center"><a href="tel:8476961919" style="color:#FFFFFF;font-size:18px;font-weight:700;text-decoration:none;letter-spacing:0.5px">call us today! (847) 696-1919</a></p>',
            "align": "center"
        },
        "elements": []
    }]


# ══════════════════════════════════════════════════════════════
# 3. SERVICES SECTION — White background, teal heading
# ══════════════════════════════════════════════════════════════

svc = find_by_id(data, "66rgciq")
if svc:
    s = svc["settings"]
    s["background_background"] = "classic"
    s["background_color"] = "#FFFFFF"
    s["gap"] = {"size": 36, "unit": "px"}

# Services heading — teal color with underline
svc_heading = find_by_id(data, "92ogqee")
if svc_heading:
    s = svc_heading["settings"]
    s["title_color"] = "#18C6B3"
    s["typography_font_size"] = {"size": 36, "unit": "px"}
    s["typography_font_size_mobile"] = {"size": 28, "unit": "px"}
    s["typography_font_weight"] = "700"
    s["align"] = "center"

# Services description text
svc_desc = find_by_id(data, "q4zp8gj")
if svc_desc:
    s = svc_desc["settings"]
    s["editor"] = '<p style="text-align:center;color:#365F6F;font-size:16px;line-height:1.6;max-width:600px;margin:0 auto">From dental implants to Invisalign to aesthetic treatments, we offer a full range of services to keep your smile healthy and beautiful.</p>'

# Service tiles — keep image tiles but improve styling
tile_ids = ["5zh3yik", "52t7j5o", "pn5myy8", "i4moeta", "00qtww1", "pnu8vk1"]
for tid in tile_ids:
    tile = find_by_id(data, tid)
    if tile:
        s = tile["settings"]
        s["border_radius"] = {"unit": "px", "top": "10", "right": "10", "bottom": "10", "left": "10", "isLinked": True}
        s["min_height"] = {"size": 260, "unit": "px"}
        s["min_height_mobile"] = {"size": 200, "unit": "px"}
        s["width"] = {"size": 31, "unit": "%"}
        s["width_mobile"] = {"size": 100, "unit": "%"}
        # Stronger gradient for text readability
        s["background_overlay_color"] = "rgba(6,32,45,0.05)"
        s["background_overlay_color_b"] = "rgba(6,32,45,0.85)"
        s["custom_css"] = "selector{transition:transform .3s ease,box-shadow .3s ease;box-shadow:0 4px 20px rgba(0,0,0,.12)}selector:hover{transform:scale(1.02);box-shadow:0 8px 32px rgba(0,0,0,.2)}"

# Service tile headings — larger, bolder
tile_heading_ids = ["zoplxxl", "1cp8js6", "xvkyv9y", "gxgxx05", "ly0g2ph", "1hadlu8"]
for hid in tile_heading_ids:
    h = find_by_id(data, hid)
    if h:
        s = h["settings"]
        s["title_color"] = "#FFFFFF"
        s["typography_font_size"] = {"size": 20, "unit": "px"}
        s["typography_font_size_mobile"] = {"size": 18, "unit": "px"}
        s["typography_font_weight"] = "700"
        # Add text shadow for readability
        s["text_shadow_text_shadow"] = {"horizontal": 0, "vertical": 2, "blur": 8, "color": "rgba(0,0,0,0.5)"}
        s["text_shadow_text_shadow_type"] = "yes"

# Service tile descriptions — better readability
tile_desc_ids = ["st5zh3y", "st52t7j", "stpn5my", "sti4moe", "st00qtw", "stpnu8v"]
for did in tile_desc_ids:
    d = find_by_id(data, did)
    if d:
        # Get current text, make it cleaner
        s = d["settings"]
        current = s.get("editor", "")
        # Update the style inline
        if "font-size:13px" in current:
            s["editor"] = current.replace("font-size:13px", "font-size:14px").replace("rgba(255,255,255,.75)", "rgba(255,255,255,.85)")

# Tiles container gap
tiles_container = find_by_id(data, "ju6n37r")
if tiles_container:
    s = tiles_container["settings"]
    s["gap"] = {"size": 16, "unit": "px"}
    s["gap_mobile"] = {"size": 14, "unit": "px"}


# ══════════════════════════════════════════════════════════════
# 4. ABOUT SECTION — White bg, teal heading with underline bar
# ══════════════════════════════════════════════════════════════

about = find_by_id(data, "zw1vmbm")
if about:
    s = about["settings"]
    s["background_color"] = "#FFFFFF"
    s["gap"] = {"size": 50, "unit": "px"}
    s["gap_mobile"] = {"size": 30, "unit": "px"}

# About eyebrow
about_eyebrow = find_by_id(data, "abt0eyb")
if about_eyebrow:
    about_eyebrow["settings"]["editor"] = '<p style="text-transform:uppercase;letter-spacing:3px;font-size:11px;color:#18C6B3;margin-bottom:4px;font-weight:600">ABOUT OUR PRACTICE</p>'

# About heading — teal with underline bar
about_heading = find_by_id(data, "alrm0ut")
if about_heading:
    s = about_heading["settings"]
    s["title"] = "The Loukas Dentistry Difference"
    s["title_color"] = "#18C6B3"
    s["typography_font_size"] = {"size": 34, "unit": "px"}
    s["typography_font_size_mobile"] = {"size": 26, "unit": "px"}
    s["typography_font_weight"] = "700"
    # Add custom CSS for underline bar
    s["_css_classes"] = "teal-underline"

# About body text — richer content matching Manus
about_text = find_by_id(data, "wuofvbb")
if about_text:
    about_text["settings"]["editor"] = '<p style="color:#365F6F;font-size:16px;line-height:1.7">When you visit our Park Ridge dental practice, you can expect a complete range of general dentistry treatments in a comfortable setting. We are among the best Chicago dentists and use the latest dental equipment and technology.</p><p style="color:#365F6F;font-size:16px;line-height:1.7;margin-top:16px">Both Dr. Thanasi Loukas and Dr. Maria Loukas have received extensive hands-on training in a wide variety of dental services including placing and restoring dental implants, children\'s dentistry, Invisalign clear orthodontics, and periodontal care.</p><p style="color:#365F6F;font-size:16px;line-height:1.7;margin-top:16px">We also pride ourselves on using the latest technology &mdash; from digital x-rays to intraoral cameras &mdash; to help provide accurate diagnoses and precision treatment.</p>'

# About credential cards — make them stat cards like Manus (20+, 5★, 1000+)
cred_cards = [
    ("crd000", "crd000t", '<p style="margin:0;text-align:center"><span style="font-size:32px;font-weight:700;color:#18C6B3;display:block;line-height:1.2">20+</span><span style="font-size:13px;color:#365F6F;display:block;margin-top:2px">Years Experience</span></p>'),
    ("crd001", "crd001t", '<p style="margin:0;text-align:center"><span style="font-size:32px;font-weight:700;color:#18C6B3;display:block;line-height:1.2">5★</span><span style="font-size:13px;color:#365F6F;display:block;margin-top:2px">Google Rating</span></p>'),
    ("crd002", "crd002t", '<p style="margin:0;text-align:center"><span style="font-size:32px;font-weight:700;color:#18C6B3;display:block;line-height:1.2">1000+</span><span style="font-size:13px;color:#365F6F;display:block;margin-top:2px">Happy Patients</span></p>'),
    ("crd003", "crd003t", '<p style="margin:0;text-align:center"><span style="font-size:32px;font-weight:700;color:#18C6B3;display:block;line-height:1.2">40+</span><span style="font-size:13px;color:#365F6F;display:block;margin-top:2px">Years Family Legacy</span></p>'),
]

for card_id, text_id, html in cred_cards:
    card = find_by_id(data, card_id)
    if card:
        s = card["settings"]
        s["background_color"] = "#F8F9FA"
        s["border_border"] = "solid"
        s["border_width"] = {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True}
        s["border_color"] = "#E8ECEF"
        s["border_radius"] = {"unit": "px", "top": "10", "right": "10", "bottom": "10", "left": "10", "isLinked": True}
        s["padding"] = {"unit": "px", "top": "20", "right": "12", "bottom": "20", "left": "12", "isLinked": False}
    text = find_by_id(data, text_id)
    if text:
        text["settings"]["editor"] = html

# About CTA button
about_btn = find_by_id(data, "mi1fpzp")
if about_btn:
    s = about_btn["settings"]
    s["text"] = "Meet Our Doctors"
    s["button_text_color"] = "#FFFFFF"
    s["background_color"] = "#18C6B3"
    s["border_radius"] = {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True}


# ══════════════════════════════════════════════════════════════
# 5. B&A SECTION — White bg, teal heading
# ══════════════════════════════════════════════════════════════

ba = find_by_id(data, "gtxdea4")
if ba:
    s = ba["settings"]
    s["background_background"] = "classic"
    s["background_color"] = "#F8F9FA"

# B&A heading — teal
ba_heading = find_by_id(data, "swqfles")
if ba_heading:
    s = ba_heading["settings"]
    s["title_color"] = "#18C6B3"
    s["typography_font_size"] = {"size": 36, "unit": "px"}
    s["typography_font_size_mobile"] = {"size": 28, "unit": "px"}
    s["typography_font_weight"] = "700"

# B&A description
ba_desc = find_by_id(data, "wvcu2um")
if ba_desc:
    ba_desc["settings"]["editor"] = '<p style="text-align:center;color:#365F6F;font-size:16px;line-height:1.6;max-width:600px;margin:0 auto">Real patients, real results. See what advanced dentistry can do for your smile.</p>'

# B&A cards — clean white cards with subtle shadow
ba_card_ids = ["6zp7l9v", "hy9ap7k", "5vh91lq"]
for cid in ba_card_ids:
    card = find_by_id(data, cid)
    if card:
        s = card["settings"]
        s["background_color"] = "#FFFFFF"
        s["border_radius"] = {"unit": "px", "top": "10", "right": "10", "bottom": "10", "left": "10", "isLinked": True}
        s["custom_css"] = "selector{box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden}"

# B&A card headings — dark navy
ba_heading_ids = ["ld5wipq", "qr9dauw", "1ndjsj9"]
for hid in ba_heading_ids:
    h = find_by_id(data, hid)
    if h:
        s = h["settings"]
        s["title_color"] = "#06202D"
        s["typography_font_size"] = {"size": 18, "unit": "px"}
        s["typography_font_weight"] = "600"

# B&A "See More Results" button
ba_btn = find_by_id(data, "h71ke0z")
if ba_btn:
    s = ba_btn["settings"]
    s["text"] = "View Full Gallery"
    s["button_text_color"] = "#FFFFFF"
    s["background_color"] = "#18C6B3"
    s["border_radius"] = {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True}


# ══════════════════════════════════════════════════════════════
# 6. TEAM SECTION — White bg, teal heading
# ══════════════════════════════════════════════════════════════

team = find_by_id(data, "y9np516")
if team:
    s = team["settings"]
    s["background_color"] = "#FFFFFF"

# Team heading — teal
team_heading = find_by_id(data, "q7aiv4n")
if team_heading:
    s = team_heading["settings"]
    s["title_color"] = "#18C6B3"
    s["typography_font_size"] = {"size": 36, "unit": "px"}
    s["typography_font_size_mobile"] = {"size": 28, "unit": "px"}
    s["typography_font_weight"] = "700"

# Team cards — clean white with subtle border
team_card_ids = ["vlml3b3", "e7dsiuh", "k0emfkj"]
for cid in team_card_ids:
    card = find_by_id(data, cid)
    if card:
        s = card["settings"]
        s["background_color"] = "#FFFFFF"
        s["border_border"] = "solid"
        s["border_width"] = {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True}
        s["border_color"] = "#E8ECEF"
        s["border_radius"] = {"unit": "px", "top": "10", "right": "10", "bottom": "10", "left": "10", "isLinked": True}
        s["custom_css"] = "selector{box-shadow:0 2px 10px rgba(0,0,0,.06);overflow:hidden}"

# Team name headings — dark navy
team_name_ids = ["anyd2ip", "s6is9hx", "4jxys5t"]
for nid in team_name_ids:
    h = find_by_id(data, nid)
    if h:
        s = h["settings"]
        s["title_color"] = "#06202D"
        s["typography_font_weight"] = "700"

# Team role headings — teal
team_role_ids = ["25c3541", "fupubh6", "isypscj"]
for rid in team_role_ids:
    h = find_by_id(data, rid)
    if h:
        s = h["settings"]
        s["title_color"] = "#18C6B3"
        s["typography_font_weight"] = "500"
        s["typography_font_size"] = {"size": 14, "unit": "px"}


# ══════════════════════════════════════════════════════════════
# 7. TESTIMONIALS — Light gray bg, clean cards
# ══════════════════════════════════════════════════════════════

test = find_by_id(data, "m09c307")
if test:
    s = test["settings"]
    s["background_color"] = "#F8F9FA"

# Testimonials heading — teal
test_heading = find_by_id(data, "6ixrk29")
if test_heading:
    s = test_heading["settings"]
    s["title_color"] = "#18C6B3"
    s["typography_font_size"] = {"size": 36, "unit": "px"}
    s["typography_font_size_mobile"] = {"size": 28, "unit": "px"}
    s["typography_font_weight"] = "700"

# Testimonial cards — white with subtle shadow
test_card_ids = ["04tavme", "x7j79mc", "otjpn4m"]
for cid in test_card_ids:
    card = find_by_id(data, cid)
    if card:
        s = card["settings"]
        s["background_color"] = "#FFFFFF"
        s["border_radius"] = {"unit": "px", "top": "10", "right": "10", "bottom": "10", "left": "10", "isLinked": True}
        s["custom_css"] = "selector{box-shadow:0 2px 10px rgba(0,0,0,.06)}"

# Testimonial names — dark navy
test_name_ids = ["3wvz8vu", "fgdo5tn", "8x18ttf"]
for nid in test_name_ids:
    h = find_by_id(data, nid)
    if h:
        h["settings"]["title_color"] = "#06202D"

# "See All Reviews" button
review_btn = find_by_id(data, "rv4gogl")
if review_btn:
    s = review_btn["settings"]
    s["button_text_color"] = "#18C6B3"
    s["background_color"] = "transparent"
    s["border_border"] = "solid"
    s["border_width"] = {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True}
    s["border_color"] = "#18C6B3"
    s["border_radius"] = {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True}


# ══════════════════════════════════════════════════════════════
# 8. FAQ SECTION — White bg, teal heading
# ══════════════════════════════════════════════════════════════

faq = find_by_id(data, "ey91tlh")
if faq:
    s = faq["settings"]
    s["background_background"] = "classic"
    s["background_color"] = "#FFFFFF"

faq_heading = find_by_id(data, "qx1rzhb")
if faq_heading:
    s = faq_heading["settings"]
    s["title_color"] = "#18C6B3"
    s["typography_font_size"] = {"size": 36, "unit": "px"}
    s["typography_font_size_mobile"] = {"size": 28, "unit": "px"}
    s["typography_font_weight"] = "700"


# ══════════════════════════════════════════════════════════════
# 9. CONTACT — Keep dark navy (looks good), but refine
# ══════════════════════════════════════════════════════════════

contact = find_by_id(data, "37h56k3")
if contact:
    s = contact["settings"]
    s["background_color"] = "#06202D"

contact_heading = find_by_id(data, "ciwi9fi")
if contact_heading:
    s = contact_heading["settings"]
    s["title_color"] = "#18C6B3"
    s["typography_font_size"] = {"size": 36, "unit": "px"}
    s["typography_font_size_mobile"] = {"size": 28, "unit": "px"}

# Contact form card — white
form_card = find_by_id(data, "m6iaqg8")
if form_card:
    s = form_card["settings"]
    s["border_radius"] = {"unit": "px", "top": "10", "right": "10", "bottom": "10", "left": "10", "isLinked": True}

form_heading = find_by_id(data, "rvtw2r8")
if form_heading:
    s = form_heading["settings"]
    s["title_color"] = "#06202D"


# ══════════════════════════════════════════════════════════════
# 10. COMMUNITIES — Tighter, teal heading
# ══════════════════════════════════════════════════════════════

comm = find_by_id(data, "z7y7ann")
if comm:
    s = comm["settings"]
    s["background_color"] = "#F8F9FA"
    s["padding"] = {"unit": "px", "top": "40", "right": "20", "bottom": "40", "left": "20", "isLinked": False}
    s["padding_mobile"] = {"unit": "px", "top": "30", "right": "16", "bottom": "70", "left": "16", "isLinked": False}

comm_heading = find_by_id(data, "ngymkxx")
if comm_heading:
    s = comm_heading["settings"]
    s["title_color"] = "#18C6B3"
    s["typography_font_size"] = {"size": 24, "unit": "px"}
    s["typography_font_size_mobile"] = {"size": 20, "unit": "px"}
    s["typography_font_weight"] = "700"


# ══════════════════════════════════════════════════════════════
# 11. GLOBAL: Add custom CSS for underline bars under headings
#     and teal CTA bar styling via the hero section's custom CSS
# ══════════════════════════════════════════════════════════════

# We'll add page-level custom CSS via the hero container
# (Elementor applies custom_css from any element)
hero = find_by_id(data, "3oond57")
if hero:
    existing_css = hero["settings"].get("custom_css", "")
    page_css = """selector .teal-underline{position:relative;padding-bottom:16px}
selector .teal-underline::after{content:'';display:block;width:60px;height:3px;background:#18C6B3;margin-top:12px}"""
    # Don't overwrite existing, append
    if "teal-underline" not in existing_css:
        hero["settings"]["custom_css"] = existing_css + "\n" + page_css if existing_css else page_css


# ══════════════════════════════════════════════════════════════
# 12. MOBILE CTA BAR — Match Manus sticky bottom bar
# ══════════════════════════════════════════════════════════════

mobile_cta = find_by_id(data, "m0b1cta")
if mobile_cta:
    s = mobile_cta["settings"]
    s["background_background"] = "classic"
    s["background_color"] = "#06202D"
    s["padding"] = {"unit": "px", "top": "10", "right": "12", "bottom": "10", "left": "12", "isLinked": False}

# Call button in sticky bar
call_sticky = find_by_id(data, "m0b1bt1")
if call_sticky:
    s = call_sticky["settings"]
    s["background_color"] = "transparent"
    s["button_text_color"] = "#FFFFFF"

# Book button in sticky bar
book_sticky = find_by_id(data, "m0b1bt2")
if book_sticky:
    s = book_sticky["settings"]
    s["background_color"] = "#18C6B3"
    s["button_text_color"] = "#FFFFFF"
    s["border_radius"] = {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True}


# ─── Write output ───
with open(INPUT, "w") as f:
    json.dump(data, f, separators=(",", ":"), ensure_ascii=False)

print(f"Fix-v3 complete: {len(data)} top-level sections")
print(f"File size: {len(json.dumps(data, separators=(',',':'), ensure_ascii=False)):,} bytes")

# Verify
checks = [
    ("Teal CTA banner", lambda: find_by_id(data, "tr5tstr")["settings"]["background_color"] == "#18C6B3"),
    ("CTA banner text", lambda: "call us today" in find_by_id(data, "ctabn01")["settings"]["editor"]),
    ("Services white bg", lambda: find_by_id(data, "66rgciq")["settings"]["background_color"] == "#FFFFFF"),
    ("Services heading teal", lambda: find_by_id(data, "92ogqee")["settings"]["title_color"] == "#18C6B3"),
    ("About white bg", lambda: find_by_id(data, "zw1vmbm")["settings"]["background_color"] == "#FFFFFF"),
    ("About heading teal", lambda: find_by_id(data, "alrm0ut")["settings"]["title_color"] == "#18C6B3"),
    ("B&A heading teal", lambda: find_by_id(data, "swqfles")["settings"]["title_color"] == "#18C6B3"),
    ("Team white bg", lambda: find_by_id(data, "y9np516")["settings"]["background_color"] == "#FFFFFF"),
    ("Team heading teal", lambda: find_by_id(data, "q7aiv4n")["settings"]["title_color"] == "#18C6B3"),
    ("FAQ heading teal", lambda: find_by_id(data, "qx1rzhb")["settings"]["title_color"] == "#18C6B3"),
    ("Contact heading teal", lambda: find_by_id(data, "ciwi9fi")["settings"]["title_color"] == "#18C6B3"),
    ("Stat cards updated", lambda: "20+" in find_by_id(data, "crd000t")["settings"]["editor"]),
    ("Hero H1 updated", lambda: find_by_id(data, "ohgi1jn")["settings"]["title"] == "Your Family Dentist in Park Ridge"),
    ("Eyebrow teal", lambda: "#18C6B3" in find_by_id(data, "h3r0eyb")["settings"]["editor"]),
    ("Glass card refined", lambda: "0.55" in find_by_id(data, "gckvbho")["settings"]["background_color"]),
    ("Hero CTA white bg", lambda: find_by_id(data, "6nnyfx4")["settings"]["background_color"] == "#FFFFFF"),
    ("Communities lighter bg", lambda: find_by_id(data, "z7y7ann")["settings"]["background_color"] == "#F8F9FA"),
]

passed = 0
for label, check in checks:
    try:
        ok = check()
        status = "OK" if ok else "FAIL"
        if ok: passed += 1
        print(f"  {status}: {label}")
    except Exception as e:
        print(f"  FAIL: {label} — {e}")

print(f"\n{passed}/{len(checks)} checks passed")
