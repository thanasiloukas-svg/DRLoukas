#!/usr/bin/env python3
import json, string, random

random.seed(42)
_counter = [0]

def uid():
    _counter[0] += 1
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=7))

def C(settings=None, elements=None):
    return {"id": uid(), "elType": "container", "settings": settings or {}, "elements": elements or [], "isInner": False}

def W(wtype, settings=None):
    return {"id": uid(), "elType": "widget", "settings": settings or {}, "elements": [], "widgetType": wtype}

def pad(t=0, r=0, b=0, l=0):
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}

def sz(val, unit="px"):
    return {"size": val, "unit": unit}

def brd(r=12):
    return {"unit": "px", "top": str(r), "right": str(r), "bottom": str(r), "left": str(r), "isLinked": True}

TEAL = "#18C6B3"
NAVY = "#06202D"
DARK = "#082B3D"
TEXT_CLR = "#365F6F"
WHITE = "#FFFFFF"
LIGHT = "#F0FAF9"
SAND = "#F8F6F2"
PF = "Playfair Display"
SS = "Source Sans Pro"

def h(title, tag="h2", align="center", color=NAVY, size=36):
    return W("heading", {"title": title, "header_size": tag, "align": align, "title_color": color,
        "typography_typography": "custom", "typography_font_family": PF,
        "typography_font_size": sz(size), "typography_font_weight": "700"})

def p(html, align="center", color=TEXT_CLR, size=17):
    return W("text-editor", {"editor": html, "align": align, "text_color": color,
        "typography_typography": "custom", "typography_font_family": SS, "typography_font_size": sz(size)})

def button(label, url, bg=TEAL, tc=WHITE, outline=False):
    s = {"text": label, "link": {"url": url, "is_external": False, "nofollow": False},
         "align": "center", "typography_typography": "custom", "typography_font_family": SS,
         "typography_font_weight": "600", "typography_font_size": sz(16),
         "border_radius": brd(6), "text_padding": pad(14, 28, 14, 28)}
    if outline:
        s.update({"button_text_color": WHITE, "button_border_border": "solid",
                  "button_border_width": pad(2,2,2,2), "button_border_color": "rgba(255,255,255,0.7)"})
    else:
        s.update({"button_text_color": tc, "background_background": "classic", "background_color": bg})
    return W("button", s)

def image(url, img_id=0):
    return W("image", {"image": {"url": url, "id": img_id}, "image_size": "full",
        "width": {"size": 100, "unit": "%"}})

SP = pad(80, 20, 80, 20)

# ======== SECTION 1: HERO ========
hero = C(
    settings={"content_width": "full", "flex_direction": "column",
        "flex_align_items": "center", "flex_justify_content": "center",
        "min_height": sz(85, "vh"),
        "background_background": "classic",
        "background_image": {"url": "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-reception-hero-desktop-1920x1080-1.webp", "id": 2479},
        "background_position": "center center", "background_size": "cover",
        "background_overlay_background": "classic",
        "background_overlay_color": "rgba(6,32,45,0.55)",
        "padding": pad(120, 20, 120, 20)},
    elements=[C(
        settings={"content_width": "boxed", "boxed_width": sz(900),
            "flex_direction": "column", "flex_align_items": "center",
            "background_background": "classic", "background_color": "rgba(255,255,255,0.12)",
            "padding": pad(50, 50, 50, 50), "border_radius": brd(16),
            "custom_css": "selector { backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255,255,255,0.18); }",
            "gap": sz(24)},
        elements=[
            h("Dental Implants, Invisalign &amp; Aesthetic Dentistry in Park Ridge", "h1", "center", WHITE, 44),
            p("<p>Combining advanced dental technology with personalized care. Dr. Thanasi Loukas and team deliver implants, Invisalign, veneers, Botox, and comprehensive family dentistry in Park Ridge, IL.</p>", "center", "rgba(255,255,255,0.9)"),
            C(settings={"flex_direction": "row", "flex_align_items": "center",
                "flex_justify_content": "center", "gap": sz(16), "flex_wrap": "wrap"},
              elements=[
                  button("Book Appointment", "https://www.drloukas.com/contact-us/"),
                  button("Call (847) 696-1919", "tel:8476961919", outline=True)]),
            C(settings={"flex_direction": "row", "flex_justify_content": "center",
                "gap": sz(16), "flex_wrap": "wrap", "margin": {"unit": "px", "top": "10"}},
              elements=[
                  C(settings={"background_background": "classic", "background_color": "rgba(255,255,255,0.15)",
                      "padding": pad(10, 22, 10, 22), "border_radius": brd(30)},
                    elements=[W("heading", {"title": "20+ Years", "header_size": "h6", "align": "center",
                        "title_color": WHITE, "typography_typography": "custom",
                        "typography_font_family": SS, "typography_font_size": sz(14), "typography_font_weight": "600"})]),
                  C(settings={"background_background": "classic", "background_color": "rgba(255,255,255,0.15)",
                      "padding": pad(10, 22, 10, 22), "border_radius": brd(30)},
                    elements=[W("heading", {"title": "5,000+ Patients", "header_size": "h6", "align": "center",
                        "title_color": WHITE, "typography_typography": "custom",
                        "typography_font_family": SS, "typography_font_size": sz(14), "typography_font_weight": "600"})]),
                  C(settings={"background_background": "classic", "background_color": "rgba(255,255,255,0.15)",
                      "padding": pad(10, 22, 10, 22), "border_radius": brd(30)},
                    elements=[W("heading", {"title": "4.9★ Google Rating", "header_size": "h6", "align": "center",
                        "title_color": WHITE, "typography_typography": "custom",
                        "typography_font_family": SS, "typography_font_size": sz(14), "typography_font_weight": "600"})])])])])

# ======== SECTION 2: SERVICES ========
svc_data = [
    ("Dental Implants", "https://www.drloukas.com/wp-content/uploads/2026/06/before-after-dental-implants_ffab8b60.jpg", "/dental-implants/", 3001),
    ("Invisalign", "https://www.drloukas.com/wp-content/uploads/2026/06/invisalign-before-and-after3_2b8a4b66.jpg", "/invisalign/", 3005),
    ("Porcelain Veneers", "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-veneers-after-1-scaled.jpg", "/porcelain-veneers/", 2722),
    ("Botox &amp; Dysport", "https://www.drloukas.com/wp-content/uploads/2026/06/dr-thanasi-loukas-botox-treatment-planning-park-ridge-il.webp", "/botox-dysport/", 2898),
    ("Dental Crowns", "https://www.drloukas.com/wp-content/uploads/2026/06/implant-crowns-before-and-after_e886eb1e.jpg", "/dental-crowns/", 2996),
    ("Lip Fillers", "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-lip-filler-result-park-ridge.jpg", "/lip-filler/", 2720),
]
tiles = []
for name, iurl, link, iid in svc_data:
    tiles.append(C(
        settings={"flex_direction": "column", "width": sz(30, "%"), "width_mobile": sz(100, "%"), "width_tablet": sz(45, "%"),
            "background_background": "classic", "background_image": {"url": iurl, "id": iid},
            "background_position": "center center", "background_size": "cover",
            "min_height": sz(280), "flex_justify_content": "flex-end",
            "padding": pad(20, 20, 24, 20), "border_radius": brd(12),
            "background_overlay_background": "classic", "background_overlay_color": "rgba(6,32,45,0.4)",
            "overflow": "hidden",
            "link": {"url": f"https://www.drloukas.com{link}", "is_external": False}},
        elements=[h(name, "h3", "left", WHITE, 22)]))

services = C(
    settings={"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center",
        "padding": SP, "background_background": "classic", "background_color": WHITE, "gap": sz(40)},
    elements=[
        h("Our Services"),
        p("<p>From dental implants to Invisalign to aesthetic treatments &mdash; comprehensive care under one roof.</p>"),
        C(settings={"flex_direction": "row", "flex_wrap": "wrap", "gap": sz(20),
            "flex_justify_content": "center", "content_width": "full"},
          elements=tiles)])

# ======== SECTION 3: ABOUT ========
about = C(
    settings={"content_width": "boxed", "flex_direction": "row", "flex_wrap": "wrap",
        "padding": SP, "background_background": "classic", "background_color": LIGHT, "gap": sz(40),
        "flex_align_items": "center"},
    elements=[
        C(settings={"flex_direction": "column", "width": sz(55, "%"), "width_mobile": sz(100, "%"), "gap": sz(20)},
          elements=[
              h("Park Ridge's Trusted Dental Practice", "h2", "left", NAVY, 34),
              p("<p>For over 20 years, Loukas Dentistry has been the trusted choice for families in Park Ridge and surrounding communities. Dr. Thanasi Loukas, DMD, combines advanced training in implant dentistry, cosmetic procedures, and facial aesthetics with a genuine commitment to patient comfort.</p><p>Our modern, technology-driven practice offers everything from routine cleanings to full-mouth rehabilitations, Invisalign orthodontics, porcelain veneers, Botox, and lip fillers &mdash; all in one convenient location.</p>", "left"),
              button("Meet Our Team", "https://www.drloukas.com/about-us/", TEAL)]),
        C(settings={"flex_direction": "column", "width": sz(40, "%"), "width_mobile": sz(100, "%")},
          elements=[
              W("image", {"image": {"url": "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-dentistry-office-lobby-park-ridge-il.jpg", "id": 2842},
                  "image_size": "full", "width": {"size": 100, "unit": "%"},
                  "border_radius": brd(12)})])])

# ======== SECTION 4: SCOPE OF PRACTICE ========
scope_cards = [
    ("General Dentistry", "fas fa-tooth", "Cleanings, exams, fillings, root canals, extractions, and preventive care for the whole family."),
    ("Cosmetic Dentistry", "fas fa-smile-beam", "Porcelain veneers, teeth whitening, composite bonding, and smile makeovers."),
    ("Restorative Dentistry", "fas fa-teeth", "Dental implants, crowns, bridges, dentures, and full-mouth rehabilitation."),
    ("Facial Aesthetics", "fas fa-star", "Botox, Dysport, lip fillers, Kybella, and TMJ/migraine treatment."),
]
scope_els = []
for title, icon, desc in scope_cards:
    scope_els.append(C(
        settings={"flex_direction": "column", "width": sz(23, "%"), "width_mobile": sz(100, "%"), "width_tablet": sz(45, "%"),
            "background_background": "classic", "background_color": WHITE,
            "padding": pad(30, 24, 30, 24), "border_radius": brd(12),
            "box_shadow_box_shadow_type": "yes",
            "box_shadow_box_shadow": {"horizontal": 0, "vertical": 4, "blur": 20, "spread": 0, "color": "rgba(8,43,61,0.08)"},
            "gap": sz(12)},
        elements=[
            W("icon", {"selected_icon": {"value": icon, "library": "fa-solid"},
                "align": "left", "primary_color": TEAL, "icon_size": sz(36)}),
            h(title, "h4", "left", NAVY, 20),
            p(f"<p>{desc}</p>", "left", TEXT_CLR, 15)]))

scope = C(
    settings={"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center",
        "padding": SP, "background_background": "classic", "background_color": SAND, "gap": sz(40)},
    elements=[
        h("Scope of Practice"),
        p("<p>Comprehensive dental and aesthetic services for every stage of life.</p>"),
        C(settings={"flex_direction": "row", "flex_wrap": "wrap", "gap": sz(20),
            "flex_justify_content": "center"}, elements=scope_els)])

# ======== SECTION 5: BEFORE & AFTER ========
ba_data = [
    ("Invisalign Transformation", "https://www.drloukas.com/wp-content/uploads/2026/06/invisalign-before-and-after_ada091d8.jpg", 3002),
    ("Composite Bonding", "https://www.drloukas.com/wp-content/uploads/2026/06/composite-bonding-before-after_42f6a8e5.jpg", 3011),
    ("Dental Implant", "https://www.drloukas.com/wp-content/uploads/2026/06/dental-implant-before-and-after_c1b9d4c0.jpg", 2999),
    ("White Filling Restoration", "https://www.drloukas.com/wp-content/uploads/2026/06/before-and-after-white-filling_64d09432.jpg", 3008),
    ("Porcelain Veneers", "https://www.drloukas.com/wp-content/uploads/2026/06/after_veneers-scaled.jpg", 2884),
    ("Full-Mouth Rehabilitation", "https://www.drloukas.com/wp-content/uploads/2026/06/implant-denture-before-after-full-face-park-ridge-scaled.jpg", 2828),
]
ba_els = []
for title, iurl, iid in ba_data:
    ba_els.append(C(
        settings={"flex_direction": "column", "width": sz(30, "%"), "width_mobile": sz(100, "%"), "width_tablet": sz(45, "%"),
            "background_background": "classic", "background_color": WHITE,
            "border_radius": brd(12), "overflow": "hidden",
            "box_shadow_box_shadow_type": "yes",
            "box_shadow_box_shadow": {"horizontal": 0, "vertical": 4, "blur": 16, "spread": 0, "color": "rgba(8,43,61,0.08)"}},
        elements=[
            W("image", {"image": {"url": iurl, "id": iid}, "image_size": "full",
                "width": {"size": 100, "unit": "%"}}),
            C(settings={"padding": pad(16, 16, 16, 16)},
              elements=[h(title, "h4", "center", NAVY, 16)])]))

ba = C(
    settings={"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center",
        "padding": SP, "background_background": "classic", "background_color": WHITE, "gap": sz(40)},
    elements=[
        h("Before &amp; After Results"),
        p("<p>Real patients, real results. See what advanced dentistry can do for your smile.</p>"),
        C(settings={"flex_direction": "row", "flex_wrap": "wrap", "gap": sz(20),
            "flex_justify_content": "center"}, elements=ba_els),
        button("View Full Gallery", "https://www.drloukas.com/gallery/")])

# ======== SECTION 6: TEAM ========
team_cards = [
    ("Dr. Thanasi Loukas, DMD", "Founder &amp; Lead Dentist",
     "https://www.drloukas.com/wp-content/uploads/2026/06/dr-thanasi-loukas-dmd-202606.jpg", 2334,
     "Specializing in dental implants, cosmetic dentistry, and facial aesthetics with over 20 years of clinical experience."),
    ("Dr. Maria Loukas, DDS", "General &amp; Family Dentistry",
     "https://www.drloukas.com/wp-content/uploads/2026/06/dr-maria-loukas-dds-professional-portrait-20260609011840.jpg", 2577,
     "Dedicated to gentle, comprehensive dental care for patients of all ages with a focus on preventive dentistry."),
    ("Elena Boggess, RDH", "Registered Dental Hygienist",
     "https://www.drloukas.com/wp-content/uploads/2026/06/elena-bogis-rdh-202606.jpg", 2335,
     "Providing thorough, comfortable cleanings and personalized oral health education for every patient."),
]
team_els = []
for name, role, iurl, iid, bio in team_cards:
    team_els.append(C(
        settings={"flex_direction": "column", "width": sz(30, "%"), "width_mobile": sz(100, "%"), "width_tablet": sz(45, "%"),
            "background_background": "classic", "background_color": WHITE,
            "border_radius": brd(12), "overflow": "hidden",
            "box_shadow_box_shadow_type": "yes",
            "box_shadow_box_shadow": {"horizontal": 0, "vertical": 4, "blur": 16, "spread": 0, "color": "rgba(8,43,61,0.08)"},
            "flex_align_items": "center"},
        elements=[
            W("image", {"image": {"url": iurl, "id": iid}, "image_size": "full",
                "width": {"size": 100, "unit": "%"}}),
            C(settings={"padding": pad(20, 20, 20, 20), "flex_direction": "column", "gap": sz(8), "flex_align_items": "center"},
              elements=[
                  h(name, "h4", "center", NAVY, 20),
                  W("heading", {"title": role, "header_size": "h6", "align": "center",
                      "title_color": TEAL, "typography_typography": "custom",
                      "typography_font_family": SS, "typography_font_size": sz(14), "typography_font_weight": "600"}),
                  p(f"<p>{bio}</p>", "center", TEXT_CLR, 15)])]))

team = C(
    settings={"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center",
        "padding": SP, "background_background": "classic", "background_color": LIGHT, "gap": sz(40)},
    elements=[
        h("Meet Our Team"),
        p("<p>Experienced professionals dedicated to your comfort and care.</p>"),
        W("image", {"image": {"url": "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-dentistry-team-dr-thanasi-dr-maria-elena-park-ridge.jpg", "id": 2840},
            "image_size": "full", "width": {"size": 80, "unit": "%"},
            "border_radius": brd(12), "align": "center"}),
        C(settings={"flex_direction": "row", "flex_wrap": "wrap", "gap": sz(20),
            "flex_justify_content": "center"}, elements=team_els)])

# ======== SECTION 7: TECHNOLOGY ========
tech_data = [
    ("CBCT 3D Imaging", "fas fa-x-ray", "Cone-beam CT scans provide detailed 3D views for precise implant placement and diagnosis."),
    ("iTero Digital Scanner", "fas fa-laptop-medical", "No messy impressions &mdash; digital scans for Invisalign, crowns, and veneers."),
    ("Intraoral Camera", "fas fa-camera", "See what we see &mdash; high-definition images of your teeth on screen."),
    ("Digital Workflow", "fas fa-microchip", "CAD/CAM technology for same-day restorations and streamlined treatment."),
]
tech_els = []
for title, icon, desc in tech_data:
    tech_els.append(C(
        settings={"flex_direction": "column", "width": sz(23, "%"), "width_mobile": sz(100, "%"), "width_tablet": sz(45, "%"),
            "background_background": "classic", "background_color": SAND,
            "padding": pad(30, 24, 30, 24), "border_radius": brd(12), "gap": sz(12),
            "flex_align_items": "center"},
        elements=[
            W("icon", {"selected_icon": {"value": icon, "library": "fa-solid"},
                "align": "center", "primary_color": TEAL, "icon_size": sz(40)}),
            h(title, "h4", "center", NAVY, 18),
            p(f"<p>{desc}</p>", "center", TEXT_CLR, 15)]))

tech = C(
    settings={"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center",
        "padding": SP, "background_background": "classic", "background_color": WHITE, "gap": sz(40)},
    elements=[
        h("Advanced Technology"),
        p("<p>State-of-the-art equipment for accurate diagnoses and comfortable treatments.</p>"),
        C(settings={"flex_direction": "row", "flex_wrap": "wrap", "gap": sz(20),
            "flex_justify_content": "center"}, elements=tech_els)])

# ======== SECTION 8: TESTIMONIALS ========
reviews = [
    ("Michael R.", "Dr. Loukas and his team are absolutely amazing. I needed dental implants and was nervous about the procedure, but they made me feel completely at ease. The results are incredible — my new teeth look and feel natural. Best dental experience I’ve ever had!"),
    ("Sarah K.", "I’ve been coming to Loukas Dentistry for years and just got Invisalign. The iTero scanner made it so easy — no goopy impressions! My teeth are already looking straighter after just a few months. The whole staff is friendly and professional."),
    ("Jennifer M.", "I got Botox and lip fillers here and couldn’t be happier with the results. Dr. Loukas has a great eye for aesthetics and made sure everything looked natural. The office is beautiful and modern. Highly recommend!"),
]
rev_els = []
for name, review in reviews:
    rev_els.append(C(
        settings={"flex_direction": "column", "width": sz(30, "%"), "width_mobile": sz(100, "%"), "width_tablet": sz(45, "%"),
            "background_background": "classic", "background_color": WHITE,
            "padding": pad(30, 24, 30, 24), "border_radius": brd(12),
            "box_shadow_box_shadow_type": "yes",
            "box_shadow_box_shadow": {"horizontal": 0, "vertical": 4, "blur": 16, "spread": 0, "color": "rgba(8,43,61,0.08)"},
            "gap": sz(12)},
        elements=[
            W("star-rating", {"rating": 5, "star_size": sz(18), "star_color": "#F4B942", "align": "left"}),
            p(f"<p>“{review}”</p>", "left", TEXT_CLR, 15),
            h(name, "h5", "left", NAVY, 16)]))

testimonials = C(
    settings={"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center",
        "padding": SP, "background_background": "classic", "background_color": SAND, "gap": sz(40)},
    elements=[
        h("What Our Patients Say"),
        p("<p>Real reviews from real patients in Park Ridge and surrounding communities.</p>"),
        C(settings={"flex_direction": "row", "flex_wrap": "wrap", "gap": sz(20),
            "flex_justify_content": "center"}, elements=rev_els),
        button("Read More Reviews", "https://www.google.com/maps/place/Loukas+Dentistry/", NAVY)])

# ======== SECTION 9: FAQ ========
faq_items = [
    ("What dental services do you offer?",
     "We offer comprehensive dental care including dental implants, Invisalign clear aligners, porcelain veneers, teeth whitening, dental crowns and bridges, root canals, extractions, cleanings, and preventive care. We also provide facial aesthetic services including Botox, Dysport, lip fillers, and Kybella."),
    ("Do you accept dental insurance?",
     "Yes, we accept most major dental insurance plans. Our team will work with your insurance provider to maximize your benefits. We also offer flexible payment options and financing through CareCredit for patients without insurance."),
    ("How do I schedule an appointment?",
     "You can schedule an appointment by calling our office at (847) 696-1919, or by visiting our contact page to submit a request online. We offer convenient appointment times Monday through Saturday."),
    ("What are your office hours?",
     "Our office hours are: Monday 9:00 AM – 6:00 PM, Tuesday 10:00 AM – 7:30 PM, Wednesday Closed, Thursday 10:00 AM – 7:30 PM, Friday 9:00 AM – 2:00 PM, and Saturday 9:00 AM – 3:00 PM."),
    ("Do you offer emergency dental care?",
     "Yes, we accommodate dental emergencies and will do our best to see you the same day. If you’re experiencing severe pain, swelling, or a dental injury, please call our office immediately at (847) 696-1919."),
    ("What is Invisalign and how does it work?",
     "Invisalign uses a series of custom-made, clear plastic aligners to gradually straighten your teeth. The aligners are virtually invisible, removable for eating and brushing, and typically achieve results in 6–18 months. We use the iTero digital scanner for precise treatment planning."),
    ("Are dental implants right for me?",
     "Dental implants are an excellent option for replacing one or more missing teeth. They look, feel, and function like natural teeth. Dr. Loukas uses CBCT 3D imaging to evaluate your bone structure and create a customized treatment plan. Most healthy adults are good candidates."),
    ("Do you offer cosmetic dentistry services?",
     "Absolutely! Our cosmetic services include porcelain veneers, professional teeth whitening, composite bonding, smile makeovers, and gum contouring. We also offer Botox, lip fillers, and other facial aesthetic treatments to complement your new smile."),
]

faq = C(
    settings={"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center",
        "padding": SP, "background_background": "classic", "background_color": WHITE, "gap": sz(40)},
    elements=[
        h("Frequently Asked Questions"),
        p("<p>Answers to common questions about our services, insurance, and office.</p>"),
        C(settings={"content_width": "boxed", "boxed_width": sz(800), "flex_direction": "column"},
          elements=[
              W("toggle", {
                  "tabs": [{"tab_title": q, "tab_content": a, "_id": uid()} for q, a in faq_items],
                  "border_color": "#E8E8E8",
                  "title_color": NAVY,
                  "title_active_color": TEAL,
                  "tab_content_color": TEXT_CLR,
                  "title_typography_typography": "custom",
                  "title_typography_font_family": SS,
                  "title_typography_font_size": sz(17),
                  "title_typography_font_weight": "600",
                  "tab_content_typography_typography": "custom",
                  "tab_content_typography_font_family": SS,
                  "tab_content_typography_font_size": sz(15)})])])

# ======== SECTION 10: CONTACT ========
hours_html = """<p><strong>Office Hours</strong></p>
<table style="width:100%; border-collapse:collapse;">
<tr><td style="padding:4px 0;">Monday</td><td style="padding:4px 0; text-align:right;">9:00 AM &ndash; 6:00 PM</td></tr>
<tr><td style="padding:4px 0;">Tuesday</td><td style="padding:4px 0; text-align:right;">10:00 AM &ndash; 7:30 PM</td></tr>
<tr><td style="padding:4px 0;">Wednesday</td><td style="padding:4px 0; text-align:right;">Closed</td></tr>
<tr><td style="padding:4px 0;">Thursday</td><td style="padding:4px 0; text-align:right;">10:00 AM &ndash; 7:30 PM</td></tr>
<tr><td style="padding:4px 0;">Friday</td><td style="padding:4px 0; text-align:right;">9:00 AM &ndash; 2:00 PM</td></tr>
<tr><td style="padding:4px 0;">Saturday</td><td style="padding:4px 0; text-align:right;">9:00 AM &ndash; 3:00 PM</td></tr>
<tr><td style="padding:4px 0;">Sunday</td><td style="padding:4px 0; text-align:right;">Closed</td></tr>
</table>"""

contact = C(
    settings={"content_width": "boxed", "flex_direction": "row", "flex_wrap": "wrap",
        "padding": SP, "background_background": "classic", "background_color": NAVY, "gap": sz(40),
        "flex_align_items": "flex-start"},
    elements=[
        C(settings={"flex_direction": "column", "width": sz(48, "%"), "width_mobile": sz(100, "%"), "gap": sz(20)},
          elements=[
              h("Contact Us", "h2", "left", WHITE, 34),
              p("<p><strong>Loukas Dentistry</strong><br>350 S Northwest Hwy, Suite 300<br>Park Ridge, IL 60068</p><p><strong>Phone:</strong> <a href='tel:8476961919' style='color:#18C6B3;'>(847) 696-1919</a><br><strong>Email:</strong> <a href='mailto:info@drloukas.com' style='color:#18C6B3;'>info@drloukas.com</a></p>", "left", "rgba(255,255,255,0.85)", 16),
              p(hours_html, "left", "rgba(255,255,255,0.85)", 15),
              W("google_maps", {"address": "350 S Northwest Hwy Suite 300, Park Ridge, IL 60068",
                  "zoom": {"size": 15}, "height": {"size": 250, "unit": "px"},
                  "border_radius": brd(12)})]),
        C(settings={"flex_direction": "column", "width": sz(48, "%"), "width_mobile": sz(100, "%"),
            "background_background": "classic", "background_color": WHITE,
            "padding": pad(30, 30, 30, 30), "border_radius": brd(12), "gap": sz(8)},
          elements=[
              h("Request an Appointment", "h3", "left", NAVY, 24),
              W("form", {
                  "form_name": "Homepage Contact Form",
                  "form_fields": [
                      {"custom_id": "name", "field_type": "text", "field_label": "Full Name",
                       "placeholder": "Your name", "required": "true", "width": "50", "_id": uid()},
                      {"custom_id": "phone", "field_type": "tel", "field_label": "Phone",
                       "placeholder": "(555) 123-4567", "required": "true", "width": "50", "_id": uid()},
                      {"custom_id": "email", "field_type": "email", "field_label": "Email",
                       "placeholder": "you@email.com", "required": "true", "width": "100", "_id": uid()},
                      {"custom_id": "service", "field_type": "select", "field_label": "Service Interested In",
                       "field_options": "General Dentistry\nDental Implants\nInvisalign\nPorcelain Veneers\nBotox / Dysport\nLip Fillers\nOther",
                       "width": "100", "_id": uid()},
                      {"custom_id": "message", "field_type": "textarea", "field_label": "Message",
                       "placeholder": "Tell us how we can help...", "rows": 4, "width": "100", "_id": uid()},
                  ],
                  "button_text": "Request Appointment",
                  "button_size": "md",
                  "button_width": "100",
                  "button_background_color": TEAL,
                  "button_text_color": WHITE,
                  "button_border_radius": brd(6),
                  "email_to": "info@drloukas.com",
                  "email_subject": "New Appointment Request - drloukas.com Homepage",
                  "label_color": NAVY,
                  "field_text_color": DARK,
                  "field_background_color": "#F8F9FA",
                  "field_border_color": "#DEE2E6",
                  "field_border_radius": brd(6),
              })])])

# ======== SECTION 11: COMMUNITIES SERVED ========
communities = C(
    settings={"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center",
        "padding": pad(50, 20, 50, 20), "background_background": "classic", "background_color": LIGHT, "gap": sz(16)},
    elements=[
        h("Proudly Serving Park Ridge &amp; Surrounding Communities", "h3", "center", NAVY, 22),
        p("<p>Des Plaines &bull; Niles &bull; Edison Park &bull; Norwood Park &bull; Rosemont &bull; Morton Grove &bull; Glenview &bull; Skokie &bull; Harwood Heights &bull; Chicago</p>", "center", TEXT_CLR, 15)])

# ======== ASSEMBLE ========
data = [hero, services, about, scope, ba, team, tech, testimonials, faq, contact, communities]

output = json.dumps(data, ensure_ascii=False)
outpath = "/tmp/claude-0/-home-user-DRLoukas/b93e6ed3-77fd-5a2b-b0f3-898bb442bd92/scratchpad/elementor-homepage.json"
with open(outpath, "w") as f:
    f.write(output)

print(f"JSON written to {outpath}")
print(f"Size: {len(output)} bytes")
print(f"Elements: {_counter[0]} total IDs generated")
