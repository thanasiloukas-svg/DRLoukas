#!/usr/bin/env python3
import json, string, random
random.seed(99)
_c = [0]
def uid():
    _c[0] += 1
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))

def C(s=None, e=None):
    return {"id": uid(), "elType": "container", "settings": s or {}, "elements": e or [], "isInner": False}

def W(t, s=None):
    return {"id": uid(), "elType": "widget", "settings": s or {}, "elements": [], "widgetType": t}

def pad(t, r=None, b=None, l=None):
    if r is None: r = t
    if b is None: b = t
    if l is None: l = r
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": t==r==b==l}

T = "#18C6B3"
N = "#06202D"
TX = "#365F6F"
W_ = "#FFFFFF"

def heading(txt, tag="h2", align="center", color=N):
    return W("heading", {"title": txt, "header_size": tag, "align": align, "title_color": color})

def txt(html, align="center"):
    return W("text-editor", {"editor": html, "align": align})

def btn(label, url, bg=T):
    return W("button", {"text": label, "link": {"url": url}, "background_background": "classic", "background_color": bg, "button_text_color": W_})

SP = pad(80, 20)

# 1. HERO
hero = C({"content_width": "full", "flex_direction": "column", "flex_align_items": "center", "flex_justify_content": "center",
    "min_height": {"size": 80, "unit": "vh"},
    "background_background": "classic",
    "background_image": {"url": "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-reception-hero-desktop-1920x1080-1.webp", "id": 2479},
    "background_position": "center center", "background_size": "cover",
    "background_overlay_background": "classic", "background_overlay_color": "rgba(6,32,45,0.55)",
    "padding": pad(100, 20)},
  [C({"content_width": "boxed", "boxed_width": {"size": 900, "unit": "px"},
      "flex_direction": "column", "flex_align_items": "center",
      "background_background": "classic", "background_color": "rgba(255,255,255,0.12)",
      "padding": pad(50), "border_radius": pad(16),
      "custom_css": "selector{backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.18)}",
      "gap": {"size": 20, "unit": "px"}},
    [heading("Dental Implants, Invisalign &amp; Aesthetic Dentistry in Park Ridge", "h1", "center", W_),
     txt("<p>Combining advanced dental technology with personalized care. Dr. Thanasi Loukas and team deliver implants, Invisalign, veneers, Botox, and comprehensive family dentistry.</p>"),
     C({"flex_direction": "row", "flex_justify_content": "center", "gap": {"size": 16, "unit": "px"}, "flex_wrap": "wrap"},
       [btn("Book Appointment", "https://www.drloukas.com/contact-us/"),
        W("button", {"text": "Call (847) 696-1919", "link": {"url": "tel:8476961919"}, "button_text_color": W_,
            "button_border_border": "solid", "button_border_width": pad(2), "button_border_color": "rgba(255,255,255,.7)"})]),
     C({"flex_direction": "row", "flex_justify_content": "center", "gap": {"size": 16, "unit": "px"}, "flex_wrap": "wrap"},
       [C({"background_background": "classic", "background_color": "rgba(255,255,255,.15)", "padding": pad(8, 20), "border_radius": pad(30)},
          [heading("20+ Years", "h6", "center", W_)]),
        C({"background_background": "classic", "background_color": "rgba(255,255,255,.15)", "padding": pad(8, 20), "border_radius": pad(30)},
          [heading("5,000+ Patients", "h6", "center", W_)]),
        C({"background_background": "classic", "background_color": "rgba(255,255,255,.15)", "padding": pad(8, 20), "border_radius": pad(30)},
          [heading("4.9★ Google Rating", "h6", "center", W_)])])])])

# 2. SERVICES
svc = [("Dental Implants", "https://www.drloukas.com/wp-content/uploads/2026/06/before-after-dental-implants_ffab8b60.jpg", "/dental-implants/"),
       ("Invisalign", "https://www.drloukas.com/wp-content/uploads/2026/06/invisalign-before-and-after3_2b8a4b66.jpg", "/invisalign/"),
       ("Porcelain Veneers", "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-veneers-after-1-scaled.jpg", "/porcelain-veneers/"),
       ("Botox &amp; Dysport", "https://www.drloukas.com/wp-content/uploads/2026/06/dr-thanasi-loukas-botox-treatment-planning-park-ridge-il.webp", "/botox-dysport/"),
       ("Dental Crowns", "https://www.drloukas.com/wp-content/uploads/2026/06/implant-crowns-before-and-after_e886eb1e.jpg", "/dental-crowns/"),
       ("Lip Fillers", "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-lip-filler-result-park-ridge.jpg", "/lip-filler/")]
tiles = [C({"background_background": "classic",
    "background_image": {"url": u}, "background_size": "cover",
    "min_height": {"size": 260, "unit": "px"}, "flex_justify_content": "flex-end",
    "padding": pad(20), "border_radius": pad(12), "overflow": "hidden",
    "background_overlay_background": "classic", "background_overlay_color": "rgba(6,32,45,.4)",
    "width": {"size": 30, "unit": "%"},
    "link": {"url": f"https://www.drloukas.com{lk}"}},
  [heading(n, "h3", "left", W_)]) for n, u, lk in svc]
services = C({"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center", "padding": SP, "gap": {"size": 40, "unit": "px"}},
  [heading("Our Services"),
   txt("<p>From dental implants to Invisalign to aesthetic treatments &mdash; comprehensive care under one roof.</p>"),
   C({"flex_direction": "row", "flex_wrap": "wrap", "gap": {"size": 20, "unit": "px"}, "flex_justify_content": "center"}, tiles)])

# 3. ABOUT
about = C({"content_width": "boxed", "flex_direction": "row", "flex_wrap": "wrap", "padding": SP,
    "background_background": "classic", "background_color": "#F0FAF9", "gap": {"size": 40, "unit": "px"}, "flex_align_items": "center"},
  [C({"flex_direction": "column", "width": {"size": 55, "unit": "%"}, "gap": {"size": 20, "unit": "px"}},
    [heading("Park Ridge's Trusted Dental Practice", "h2", "left"),
     txt("<p>For over 20 years, Loukas Dentistry has been the trusted choice for families in Park Ridge. Dr. Thanasi Loukas, DMD, combines advanced training in implant dentistry, cosmetic procedures, and facial aesthetics with a genuine commitment to patient comfort.</p><p>Our modern practice offers everything from routine cleanings to full-mouth rehabilitations, Invisalign, veneers, Botox, and lip fillers &mdash; all in one convenient location.</p>", "left"),
     btn("Meet Our Team", "https://www.drloukas.com/about-us/")]),
   C({"flex_direction": "column", "width": {"size": 40, "unit": "%"}},
    [W("image", {"image": {"url": "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-dentistry-office-lobby-park-ridge-il.jpg", "id": 2842},
        "image_size": "full", "border_radius": pad(12)})])])

# 4. TEAM
team_data = [
    ("Dr. Thanasi Loukas, DMD", "Founder &amp; Lead Dentist", "https://www.drloukas.com/wp-content/uploads/2026/06/dr-thanasi-loukas-dmd-202606.jpg",
     "Specializing in dental implants, cosmetic dentistry, and facial aesthetics with 20+ years of experience."),
    ("Dr. Maria Loukas, DDS", "General &amp; Family Dentistry", "https://www.drloukas.com/wp-content/uploads/2026/06/dr-maria-loukas-dds-professional-portrait-20260609011840.jpg",
     "Gentle, comprehensive dental care for patients of all ages."),
    ("Elena Boggess, RDH", "Dental Hygienist", "https://www.drloukas.com/wp-content/uploads/2026/06/elena-bogis-rdh-202606.jpg",
     "Thorough cleanings and personalized oral health education.")]
tcards = [C({"flex_direction": "column", "width": {"size": 30, "unit": "%"},
    "background_background": "classic", "background_color": W_, "border_radius": pad(12), "overflow": "hidden"},
  [W("image", {"image": {"url": u}, "image_size": "full"}),
   C({"padding": pad(20), "flex_direction": "column", "gap": {"size": 6, "unit": "px"}, "flex_align_items": "center"},
     [heading(n, "h4", "center"), heading(r, "h6", "center", T), txt(f"<p>{b}</p>")])]) for n, r, u, b in team_data]

team = C({"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center", "padding": SP,
    "background_background": "classic", "background_color": "#F0FAF9", "gap": {"size": 40, "unit": "px"}},
  [heading("Meet Our Team"),
   W("image", {"image": {"url": "https://www.drloukas.com/wp-content/uploads/2026/06/loukas-dentistry-team-dr-thanasi-dr-maria-elena-park-ridge.jpg", "id": 2840},
       "image_size": "full", "width": {"size": 80, "unit": "%"}, "border_radius": pad(12), "align": "center"}),
   C({"flex_direction": "row", "flex_wrap": "wrap", "gap": {"size": 20, "unit": "px"}, "flex_justify_content": "center"}, tcards)])

# 5. B&A (3 items)
ba_items = [
    ("Invisalign Result", "https://www.drloukas.com/wp-content/uploads/2026/06/invisalign-before-and-after_ada091d8.jpg"),
    ("Dental Implant", "https://www.drloukas.com/wp-content/uploads/2026/06/dental-implant-before-and-after_c1b9d4c0.jpg"),
    ("Porcelain Veneers", "https://www.drloukas.com/wp-content/uploads/2026/06/after_veneers-scaled.jpg")]
ba_cards = [C({"flex_direction": "column", "width": {"size": 30, "unit": "%"},
    "background_background": "classic", "background_color": W_, "border_radius": pad(12), "overflow": "hidden"},
  [W("image", {"image": {"url": u}, "image_size": "full"}),
   C({"padding": pad(12)}, [heading(n, "h4", "center")])]) for n, u in ba_items]
ba = C({"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center", "padding": SP, "gap": {"size": 40, "unit": "px"}},
  [heading("Before &amp; After Results"),
   txt("<p>Real patients, real results. See what advanced dentistry can do.</p>"),
   C({"flex_direction": "row", "flex_wrap": "wrap", "gap": {"size": 20, "unit": "px"}, "flex_justify_content": "center"}, ba_cards),
   btn("View Full Gallery", "https://www.drloukas.com/gallery/")])

# 6. TESTIMONIALS
reviews = [
    ("Michael R.", "“Dr. Loukas and his team are amazing. I needed dental implants and was nervous, but they made me feel at ease. The results are incredible!”"),
    ("Sarah K.", "“I got Invisalign here and the iTero scanner made it so easy — no goopy impressions! My teeth are already straighter. Friendly and professional.”"),
    ("Jennifer M.", "“I got Botox and lip fillers and couldn’t be happier. Dr. Loukas has a great eye for aesthetics. The office is beautiful. Highly recommend!”")]
rev_cards = [C({"flex_direction": "column", "width": {"size": 30, "unit": "%"},
    "background_background": "classic", "background_color": W_, "padding": pad(24), "border_radius": pad(12),
    "gap": {"size": 10, "unit": "px"}},
  [W("star-rating", {"rating": 5, "star_color": "#F4B942"}),
   txt(f"<p>{r}</p>", "left"),
   heading(n, "h5", "left")]) for n, r in reviews]
testimonials = C({"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center", "padding": SP,
    "background_background": "classic", "background_color": "#F8F6F2", "gap": {"size": 40, "unit": "px"}},
  [heading("What Our Patients Say"),
   C({"flex_direction": "row", "flex_wrap": "wrap", "gap": {"size": 20, "unit": "px"}, "flex_justify_content": "center"}, rev_cards)])

# 7. FAQ
faq_items = [
    ("What dental services do you offer?", "We offer dental implants, Invisalign, porcelain veneers, teeth whitening, crowns, bridges, root canals, cleanings, Botox, Dysport, lip fillers, and Kybella."),
    ("Do you accept dental insurance?", "Yes, we accept most major dental insurance plans. We also offer flexible payment options and CareCredit financing."),
    ("How do I schedule an appointment?", "Call (847) 696-1919 or visit our contact page to submit a request online."),
    ("What are your office hours?", "Monday 9–6, Tuesday 10–7:30, Wednesday Closed, Thursday 10–7:30, Friday 9–2, Saturday 9–3."),
    ("Do you offer emergency dental care?", "Yes, we accommodate same-day emergencies. Call (847) 696-1919 immediately for urgent dental needs."),
    ("What is Invisalign?", "Invisalign uses custom clear aligners to straighten teeth, typically in 6–18 months. We use the iTero digital scanner for precise planning."),
    ("Are dental implants right for me?", "Most healthy adults are candidates. Dr. Loukas uses CBCT 3D imaging to evaluate bone structure and create a personalized plan."),
    ("Do you offer cosmetic dentistry?", "Yes — veneers, whitening, bonding, smile makeovers, Botox, lip fillers, and more.")]
faq = C({"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center", "padding": SP, "gap": {"size": 40, "unit": "px"}},
  [heading("Frequently Asked Questions"),
   C({"content_width": "boxed", "boxed_width": {"size": 800, "unit": "px"}, "flex_direction": "column"},
     [W("toggle", {"tabs": [{"tab_title": q, "tab_content": a, "_id": uid()} for q, a in faq_items],
         "title_color": N, "title_active_color": T})])])

# 8. CONTACT
hours = "<p><strong>Office Hours</strong></p><table><tr><td>Monday</td><td>9 AM – 6 PM</td></tr><tr><td>Tuesday</td><td>10 AM – 7:30 PM</td></tr><tr><td>Wednesday</td><td>Closed</td></tr><tr><td>Thursday</td><td>10 AM – 7:30 PM</td></tr><tr><td>Friday</td><td>9 AM – 2 PM</td></tr><tr><td>Saturday</td><td>9 AM – 3 PM</td></tr></table>"
contact = C({"content_width": "boxed", "flex_direction": "row", "flex_wrap": "wrap", "padding": SP,
    "background_background": "classic", "background_color": N, "gap": {"size": 40, "unit": "px"}},
  [C({"flex_direction": "column", "width": {"size": 48, "unit": "%"}, "gap": {"size": 20, "unit": "px"}},
    [heading("Contact Us", "h2", "left", W_),
     txt("<p><strong>Loukas Dentistry</strong><br>350 S Northwest Hwy, Suite 300<br>Park Ridge, IL 60068</p><p><strong>Phone:</strong> <a href='tel:8476961919' style='color:#18C6B3'>(847) 696-1919</a></p>", "left"),
     txt(hours, "left"),
     W("google_maps", {"address": "350 S Northwest Hwy Suite 300, Park Ridge, IL 60068", "zoom": {"size": 15}, "height": {"size": 220, "unit": "px"}})]),
   C({"flex_direction": "column", "width": {"size": 48, "unit": "%"},
       "background_background": "classic", "background_color": W_, "padding": pad(30), "border_radius": pad(12)},
    [heading("Request an Appointment", "h3", "left"),
     W("form", {"form_name": "Contact",
         "form_fields": [
             {"custom_id": "name", "field_type": "text", "field_label": "Name", "required": "true", "width": "50", "_id": uid()},
             {"custom_id": "phone", "field_type": "tel", "field_label": "Phone", "required": "true", "width": "50", "_id": uid()},
             {"custom_id": "email", "field_type": "email", "field_label": "Email", "width": "100", "_id": uid()},
             {"custom_id": "message", "field_type": "textarea", "field_label": "Message", "width": "100", "_id": uid()}],
         "button_text": "Request Appointment", "button_width": "100",
         "button_background_color": T, "button_text_color": W_,
         "email_to": "info@drloukas.com", "email_subject": "Appointment Request - drloukas.com"})])])

# 9. COMMUNITIES
communities = C({"content_width": "boxed", "flex_direction": "column", "flex_align_items": "center",
    "padding": pad(40, 20), "background_background": "classic", "background_color": "#F0FAF9"},
  [heading("Proudly Serving Park Ridge &amp; Surrounding Communities", "h3"),
   txt("<p>Des Plaines &bull; Niles &bull; Edison Park &bull; Norwood Park &bull; Rosemont &bull; Morton Grove &bull; Glenview &bull; Skokie &bull; Chicago</p>")])

data = [hero, services, about, team, ba, testimonials, faq, contact, communities]
out = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
path = "/tmp/claude-0/-home-user-DRLoukas/b93e6ed3-77fd-5a2b-b0f3-898bb442bd92/scratchpad/elementor-compact.json"
with open(path, "w") as f:
    f.write(out)
print(f"Size: {len(out)} bytes ({len(out)//1024}KB)")
print(f"Elements: {_c[0]} IDs")
