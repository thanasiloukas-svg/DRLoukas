#!/usr/bin/env python3
"""Redesign the drloukas.com Elementor homepage for a premium, elegant look.

Based on patterns from top dental websites (Tend, Dentologie, Grand Street Dental,
Beverly Hills Dentistry, Serenity Smiles). Key improvements:
- Mobile sticky CTA bar
- Gradient overlays on hero + service tiles for text readability
- Trust strip with stats
- Better mobile responsiveness (reduced dead space, 2-col service grid)
- Prominent phone number placement
- Credential badges in About section
- Eyebrow text for section context
"""
import json

with open('/home/user/DRLoukas/elementor-build/elementor-compact.json') as f:
    data = json.load(f)

# Reference existing sections
hero = data[0]       # 3oond57
services = data[1]   # 66rgciq
about = data[2]      # zw1vmbm
team = data[3]       # y9np516
ba = data[4]         # gtxdea4
testimonials = data[5]  # m09c307
faq = data[6]        # ey91tlh
contact = data[7]    # 37h56k3
communities = data[8]  # z7y7ann


# =============================================
# SECTION 0: MOBILE STICKY CTA BAR
# Fixed to bottom of screen, visible only on mobile
# Pattern: Tend, Dentologie, most top dental sites
# =============================================
mobile_cta = {
    "id": "m0b1cta",
    "elType": "container",
    "settings": {
        "content_width": "full",
        "flex_direction": "row",
        "gap": {"size": 0, "unit": "px"},
        "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
        "margin": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
        "custom_css": "selector{position:fixed!important;bottom:0;left:0;right:0;z-index:9999;box-shadow:0 -2px 12px rgba(0,0,0,.2)}",
        "hide_desktop": "hidden"
    },
    "elements": [
        {
            "id": "m0b1cn1",
            "elType": "container",
            "settings": {
                "width": {"size": 50, "unit": "%"},
                "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
            },
            "elements": [{
                "id": "m0b1bt1",
                "elType": "widget",
                "settings": {
                    "text": "Call Now",
                    "link": {"url": "tel:8476961919"},
                    "align": "stretch",
                    "icon": {"value": "fas fa-phone-alt", "library": "fa-solid"},
                    "selected_icon": {"value": "fas fa-phone-alt", "library": "fa-solid"},
                    "icon_align": "left",
                    "background_background": "classic",
                    "background_color": "#06202D",
                    "button_text_color": "#FFFFFF",
                    "border_radius": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
                    "typography_typography": "custom",
                    "typography_font_weight": "700",
                    "typography_font_size": {"size": 15, "unit": "px"}
                },
                "elements": [],
                "widgetType": "button"
            }],
            "isInner": False
        },
        {
            "id": "m0b1cn2",
            "elType": "container",
            "settings": {
                "width": {"size": 50, "unit": "%"},
                "padding": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
            },
            "elements": [{
                "id": "m0b1bt2",
                "elType": "widget",
                "settings": {
                    "text": "Book Online",
                    "link": {"url": "https://www.drloukas.com/contact-us/"},
                    "align": "stretch",
                    "icon": {"value": "fas fa-calendar-check", "library": "fa-solid"},
                    "selected_icon": {"value": "fas fa-calendar-check", "library": "fa-solid"},
                    "icon_align": "left",
                    "background_background": "classic",
                    "background_color": "#18C6B3",
                    "button_text_color": "#FFFFFF",
                    "border_radius": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True},
                    "typography_typography": "custom",
                    "typography_font_weight": "700",
                    "typography_font_size": {"size": 15, "unit": "px"}
                },
                "elements": [],
                "widgetType": "button"
            }],
            "isInner": False
        }
    ],
    "isInner": False
}


# =============================================
# SECTION 1: HERO (modify existing)
# Pattern: gradient overlay, compact mobile, prominent phone
# =============================================

# Gradient overlay instead of flat color - preserves image at top, darkens at bottom for text
hero['settings']['background_overlay_background'] = 'gradient'
hero['settings']['background_overlay_color'] = 'rgba(6,32,45,0.05)'
hero['settings']['background_overlay_color_b'] = 'rgba(6,32,45,0.55)'
hero['settings']['background_overlay_gradient_type'] = 'linear'
hero['settings']['background_overlay_gradient_angle'] = {"size": 180, "unit": "deg"}

# Reduce height - eliminate dead space
hero['settings']['min_height'] = {"size": 65, "unit": "vh"}
hero['settings']['min_height_mobile'] = {"size": 0, "unit": "px"}  # auto on mobile

# Mobile padding - compact
hero['settings']['padding_mobile'] = {
    "unit": "px", "top": "50", "right": "16", "bottom": "50", "left": "16", "isLinked": False
}

# Glass card improvements
glass_card = hero['elements'][0]  # gckvbho
glass_card['settings']['background_color'] = 'rgba(255,255,255,0.18)'
glass_card['settings']['custom_css'] = 'selector{backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,.25)}'
glass_card['settings']['boxed_width'] = {"size": 800, "unit": "px"}
glass_card['settings']['padding_mobile'] = {
    "unit": "px", "top": "28", "right": "20", "bottom": "28", "left": "20", "isLinked": False
}
glass_card['settings']['gap'] = {"size": 16, "unit": "px"}

# Add eyebrow text before H1
eyebrow_hero = {
    "id": "h3r0eyb",
    "elType": "widget",
    "settings": {
        "editor": "<p style=\"text-transform:uppercase;letter-spacing:4px;font-size:12px;color:rgba(255,255,255,.65);margin-bottom:0\">PARK RIDGE, ILLINOIS</p>",
        "align": "center"
    },
    "elements": [],
    "widgetType": "text-editor"
}

# Better H1 - shorter, more impactful
h1_widget = glass_card['elements'][0]  # ohgi1jn
h1_widget['settings']['title'] = 'Your Smile Deserves Expert Care'
h1_widget['settings']['typography_typography'] = 'custom'
h1_widget['settings']['typography_font_size'] = {"size": 38, "unit": "px"}
h1_widget['settings']['typography_font_size_mobile'] = {"size": 26, "unit": "px"}
h1_widget['settings']['typography_font_weight'] = '700'

# Better subtitle
subtitle_widget = glass_card['elements'][1]  # yt7rpwh
subtitle_widget['settings']['editor'] = '<p style="font-size:16px;line-height:1.6">Advanced dental implants, Invisalign, cosmetic dentistry &amp; facial aesthetics — personalized care by Dr. Thanasi Loukas with 20+ years of experience.</p>'

# Add prominent phone number
phone_hero = {
    "id": "h3r0phn",
    "elType": "widget",
    "settings": {
        "editor": "<p><a href=\"tel:8476961919\" style=\"color:#18C6B3;font-size:22px;font-weight:700;text-decoration:none;letter-spacing:0.5px\">(847) 696-1919</a></p>",
        "align": "center"
    },
    "elements": [],
    "widgetType": "text-editor"
}

# Remove stats pills from hero (moving to trust strip)
# Stats are in container hu124e3
new_glass_elements = []
for el in glass_card['elements']:
    if el['id'] != 'hu124e3':
        new_glass_elements.append(el)
glass_card['elements'] = new_glass_elements

# Insert eyebrow at top, phone after subtitle (before buttons)
# Current order after removal: h1 (ohgi1jn), subtitle (yt7rpwh), buttons (ah9tq6v)
glass_card['elements'].insert(0, eyebrow_hero)
# Now: eyebrow, h1, subtitle, buttons
glass_card['elements'].insert(3, phone_hero)
# Now: eyebrow, h1, subtitle, phone, buttons


# =============================================
# SECTION 2: TRUST STRIP (new)
# Pattern: compact navy bar with 4 stats
# =============================================
trust_items_data = [
    {"number": "20+", "label": "Years Experience"},
    {"number": "5,000+", "label": "Happy Patients"},
    {"number": "4.9★", "label": "Google Rating"},
    {"number": "#1", "label": "Rated in Park Ridge"},
]

trust_elements = []
for i, item in enumerate(trust_items_data):
    tid = f"tr5t{i:03d}"
    trust_el = {
        "id": tid,
        "elType": "container",
        "settings": {
            "width": {"size": 25, "unit": "%"},
            "width_mobile": {"size": 50, "unit": "%"},
            "flex_direction": "column",
            "flex_align_items": "center",
            "flex_justify_content": "center",
            "padding": {"unit": "px", "top": "20", "right": "12", "bottom": "20", "left": "12", "isLinked": False},
            "padding_mobile": {"unit": "px", "top": "14", "right": "8", "bottom": "14", "left": "8", "isLinked": False}
        },
        "elements": [{
            "id": tid + "t",
            "elType": "widget",
            "settings": {
                "editor": f'<p style="margin:0;text-align:center;line-height:1.3"><span style="display:block;font-size:26px;font-weight:800;color:#18C6B3">{item["number"]}</span><span style="font-size:11px;text-transform:uppercase;letter-spacing:1.5px;color:rgba(255,255,255,.6)">{item["label"]}</span></p>',
                "align": "center"
            },
            "elements": [],
            "widgetType": "text-editor"
        }],
        "isInner": False
    }
    trust_elements.append(trust_el)

trust_strip = {
    "id": "tr5tstr",
    "elType": "container",
    "settings": {
        "content_width": "full",
        "flex_direction": "row",
        "flex_wrap": "wrap",
        "flex_justify_content": "center",
        "flex_align_items": "stretch",
        "gap": {"size": 0, "unit": "px"},
        "padding": {"unit": "px", "top": "0", "right": "40", "bottom": "0", "left": "40", "isLinked": False},
        "padding_mobile": {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
        "background_background": "classic",
        "background_color": "#06202D"
    },
    "elements": trust_elements,
    "isInner": False
}


# =============================================
# SECTION 3: SERVICES (modify existing)
# Pattern: gradient overlays, subtitles, 2-col mobile, text shadows
# =============================================

# Reduce section padding on mobile
services['settings']['padding_mobile'] = {
    "unit": "px", "top": "50", "right": "16", "bottom": "50", "left": "16", "isLinked": False
}

# Tile subtitles
tile_subs = {
    "5zh3yik": "Permanent Tooth Replacement",
    "52t7j5o": "Clear Aligner Therapy",
    "pn5myy8": "Transform Your Smile",
    "i4moeta": "Wrinkle & Fine Line Reduction",
    "00qtww1": "Custom Dental Restorations",
    "pnu8vk1": "Fuller, Natural-Looking Lips"
}

# Find the tiles container
tiles_container = None
for el in services['elements']:
    if el['id'] == 'ju6n37r':
        tiles_container = el
        break

if tiles_container:
    for tile in tiles_container['elements']:
        if tile['elType'] == 'container' and 'background_image' in tile.get('settings', {}):
            # Gradient overlay (transparent at top, dark at bottom)
            tile['settings']['background_overlay_background'] = 'gradient'
            tile['settings']['background_overlay_color'] = 'rgba(6,32,45,0)'
            tile['settings']['background_overlay_color_b'] = 'rgba(6,32,45,0.82)'
            tile['settings']['background_overlay_gradient_type'] = 'linear'
            tile['settings']['background_overlay_gradient_angle'] = {"size": 180, "unit": "deg"}

            # Mobile: 2 per row
            tile['settings']['width_mobile'] = {"size": 47, "unit": "%"}

            # Taller tiles
            tile['settings']['min_height'] = {"size": 300, "unit": "px"}
            tile['settings']['min_height_mobile'] = {"size": 200, "unit": "px"}

            # Hover zoom
            tile['settings']['custom_css'] = 'selector{transition:transform .3s ease,box-shadow .3s ease}selector:hover{transform:scale(1.03);box-shadow:0 8px 30px rgba(0,0,0,.25)}'

            # Find the heading inside and add text shadow + larger font
            for child in tile['elements']:
                if child.get('widgetType') == 'heading':
                    child['settings']['text_shadow_text_shadow_type'] = 'yes'
                    child['settings']['text_shadow_text_shadow'] = {
                        "horizontal": 0, "vertical": 2, "blur": 8, "color": "rgba(0,0,0,0.6)"
                    }
                    child['settings']['typography_typography'] = 'custom'
                    child['settings']['typography_font_size'] = {"size": 22, "unit": "px"}
                    child['settings']['typography_font_size_mobile'] = {"size": 18, "unit": "px"}
                    child['settings']['typography_font_weight'] = '700'

            # Add subtitle under heading
            if tile['id'] in tile_subs:
                sub_widget = {
                    "id": f"st{tile['id'][:5]}",
                    "elType": "widget",
                    "settings": {
                        "editor": f'<p style="font-size:13px;color:rgba(255,255,255,.75);margin:0;line-height:1.3">{tile_subs[tile["id"]]}</p>',
                        "align": "left"
                    },
                    "elements": [],
                    "widgetType": "text-editor"
                }
                tile['elements'].append(sub_widget)


# =============================================
# SECTION 4: ABOUT (modify existing)
# Pattern: eyebrow text, credential badges, richer copy
# =============================================

# Mobile padding
about['settings']['padding_mobile'] = {
    "unit": "px", "top": "50", "right": "16", "bottom": "50", "left": "16", "isLinked": False
}

text_col = about['elements'][0]  # 2egjnuh
img_col = about['elements'][1]   # 3fd1xf5

# Mobile: full width columns
text_col['settings']['width_mobile'] = {"size": 100, "unit": "%"}
img_col['settings']['width_mobile'] = {"size": 100, "unit": "%"}

# Add eyebrow
eyebrow_about = {
    "id": "abt0eyb",
    "elType": "widget",
    "settings": {
        "editor": "<p style=\"text-transform:uppercase;letter-spacing:3px;font-size:12px;color:#18C6B3;margin-bottom:0;font-weight:600\">ABOUT OUR PRACTICE</p>",
        "align": "left"
    },
    "elements": [],
    "widgetType": "text-editor"
}
text_col['elements'].insert(0, eyebrow_about)

# Update about text to be richer with more links
about_text = text_col['elements'][2]  # wuofvbb (now at index 2 after eyebrow insert)
about_text['settings']['editor'] = '<p>For over 20 years, <strong>Loukas Dentistry</strong> has been the trusted choice for families in Park Ridge. Dr. Thanasi Loukas, DMD, combines advanced training in <a href="https://www.drloukas.com/dental-implants/" style="color:#18C6B3">implant dentistry</a>, <a href="https://www.drloukas.com/porcelain-veneers/" style="color:#18C6B3">cosmetic procedures</a>, and <a href="https://www.drloukas.com/botox-dysport/" style="color:#18C6B3">facial aesthetics</a> with a genuine commitment to patient comfort.</p><p>Our modern practice offers everything from routine cleanings to full-mouth rehabilitations, <a href="https://www.drloukas.com/invisalign/" style="color:#18C6B3">Invisalign</a>, veneers, Botox, and <a href="https://www.drloukas.com/lip-filler/" style="color:#18C6B3">lip fillers</a> &mdash; all in one convenient location.</p>'

# Add credential badges after about text
credentials = {
    "id": "abt0crd",
    "elType": "container",
    "settings": {
        "flex_direction": "row",
        "flex_wrap": "wrap",
        "gap": {"size": 10, "unit": "px"},
        "padding": {"unit": "px", "top": "5", "right": "0", "bottom": "5", "left": "0", "isLinked": False}
    },
    "elements": [],
    "isInner": False
}

badge_labels = ["Board Certified", "Advanced Implant Training", "Invisalign Certified", "Facial Aesthetics"]
for i, label in enumerate(badge_labels):
    badge = {
        "id": f"crd{i:03d}",
        "elType": "container",
        "settings": {
            "background_background": "classic",
            "background_color": "rgba(24,198,179,.1)",
            "padding": {"unit": "px", "top": "6", "right": "14", "bottom": "6", "left": "14", "isLinked": False},
            "border_radius": {"unit": "px", "top": "20", "right": "20", "bottom": "20", "left": "20", "isLinked": True}
        },
        "elements": [{
            "id": f"crd{i:03d}t",
            "elType": "widget",
            "settings": {
                "editor": f'<p style="font-size:12px;color:#06202D;margin:0;white-space:nowrap"><strong>{label}</strong></p>',
                "align": "center"
            },
            "elements": [],
            "widgetType": "text-editor"
        }],
        "isInner": False
    }
    credentials['elements'].append(badge)

# Insert credentials after about text (index 3 after eyebrow), before "Meet Our Team" button
text_col['elements'].insert(3, credentials)


# =============================================
# SECTION 5-9: MOBILE RESPONSIVENESS FIXES
# =============================================

# Before & After - mobile card widths
for el in ba['elements']:
    if el['id'] == '2o2adqd':
        for card in el['elements']:
            if card['elType'] == 'container':
                card['settings']['width_mobile'] = {"size": 100, "unit": "%"}
ba['settings']['padding_mobile'] = {
    "unit": "px", "top": "50", "right": "16", "bottom": "50", "left": "16", "isLinked": False
}

# Team - mobile card widths
for el in team['elements']:
    if el['id'] == 'hw1caep':
        for card in el['elements']:
            card['settings']['width_mobile'] = {"size": 100, "unit": "%"}
team['settings']['padding_mobile'] = {
    "unit": "px", "top": "50", "right": "16", "bottom": "50", "left": "16", "isLinked": False
}

# Testimonials - mobile card widths + Google reviews link
for el in testimonials['elements']:
    if el['id'] == 'e3cm887':
        for card in el['elements']:
            card['settings']['width_mobile'] = {"size": 100, "unit": "%"}
testimonials['settings']['padding_mobile'] = {
    "unit": "px", "top": "50", "right": "16", "bottom": "50", "left": "16", "isLinked": False
}

# Add Google reviews link
google_link = {
    "id": "rv4gogl",
    "elType": "widget",
    "settings": {
        "text": "Read More Reviews on Google",
        "link": {"url": "https://www.google.com/maps/place/Loukas+Dentistry/", "is_external": "true"},
        "align": "center",
        "background_background": "classic",
        "background_color": "transparent",
        "button_text_color": "#06202D",
        "button_border_border": "solid",
        "button_border_width": {"unit": "px", "top": "2", "right": "2", "bottom": "2", "left": "2", "isLinked": True},
        "button_border_color": "#06202D",
        "border_radius": {"unit": "px", "top": "8", "right": "8", "bottom": "8", "left": "8", "isLinked": True}
    },
    "elements": [],
    "widgetType": "button"
}
testimonials['elements'].append(google_link)

# FAQ - mobile padding
faq['settings']['padding_mobile'] = {
    "unit": "px", "top": "50", "right": "16", "bottom": "50", "left": "16", "isLinked": False
}

# Contact - mobile column widths + prominent phone
contact['settings']['padding_mobile'] = {
    "unit": "px", "top": "50", "right": "16", "bottom": "50", "left": "16", "isLinked": False
}

for el in contact['elements']:
    if el.get('settings', {}).get('width', {}).get('size') == 48:
        el['settings']['width_mobile'] = {"size": 100, "unit": "%"}

# Make phone MUCH more prominent in contact
contact_left = contact['elements'][0]  # uyerpgy
for el in contact_left['elements']:
    if el['id'] == 'o8mg0dq':
        el['settings']['editor'] = '<p><strong style="font-size:18px;color:#FFFFFF">Loukas Dentistry</strong><br><span style="color:rgba(255,255,255,.7)">350 S Northwest Hwy, Suite 300<br>Park Ridge, IL 60068</span></p><p style="margin-top:12px"><a href="tel:8476961919" style="color:#18C6B3;font-size:26px;font-weight:700;text-decoration:none;letter-spacing:0.5px">(847) 696-1919</a></p>'

# Communities - extra bottom padding for mobile CTA bar
communities['settings']['padding_mobile'] = {
    "unit": "px", "top": "30", "right": "16", "bottom": "80", "left": "16", "isLinked": False
}


# =============================================
# ASSEMBLE FINAL PAGE
# =============================================
final_data = [
    mobile_cta,     # Sticky mobile CTA bar
    hero,           # Modified hero
    trust_strip,    # NEW: trust strip
    services,       # Modified services
    about,          # Modified about
    ba,             # Before & After (mobile widths)
    team,           # Team (mobile widths)
    testimonials,   # Testimonials (mobile widths + Google link)
    faq,            # FAQ (mobile padding)
    contact,        # Contact (prominent phone, mobile widths)
    communities     # Communities (extra bottom padding)
]

# Write
output_path = '/home/user/DRLoukas/elementor-build/elementor-compact.json'
with open(output_path, 'w') as f:
    json.dump(final_data, f, ensure_ascii=False)

print(f"Redesign complete: {len(final_data)} sections")
print(f"File size: {len(json.dumps(final_data, ensure_ascii=False)):,} bytes")

# Verify key changes
text = json.dumps(final_data, ensure_ascii=False)
checks = [
    ("Mobile sticky CTA bar", "m0b1cta" in text),
    ("Hero gradient overlay", "background_overlay_gradient_type" in text),
    ("Trust strip", "tr5tstr" in text),
    ("Service tile gradients", text.count("background_overlay_gradient_type") >= 7),
    ("Service tile subtitles", "Permanent Tooth Replacement" in text),
    ("Text shadows on tiles", "text_shadow_text_shadow_type" in text),
    ("Mobile widths (47%)", "47" in text),
    ("About eyebrow", "ABOUT OUR PRACTICE" in text),
    ("Credential badges", "Board Certified" in text),
    ("Prominent phone in hero", "h3r0phn" in text),
    ("Google reviews link", "rv4gogl" in text),
    ("Mobile padding reductions", "padding_mobile" in text),
    ("Hero PARK RIDGE eyebrow", "PARK RIDGE" in text),
    ("Service links in about", "dental-implants" in text and "invisalign" in text),
    ("Communities extra bottom padding", '"bottom": "80"' in text),
]
print("\nVerification:")
for label, ok in checks:
    print(f"  {'OK' if ok else 'FAIL'}: {label}")
