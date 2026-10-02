# 2026-08-26 DrLoukas SEO & Content Growth Plan

Prepared 2026-08-26 from a live site audit via WordPress/Novamira. Primary origin: **https://www.drloukas.com/**. Shareable version: published as the "Loukas Growth Plan" artifact (session 2026-08-26).

Constraints honored: no redesign, no mass content generation, no page deletions, no redirect/canonical changes.

## Critical fixes

- **FIXED — Elk Grove Village wrong address.** /elk-grove-village-dentist/ (1830) said "1501 S. Elmhurst Rd., Park Ridge" and "open Monday through Saturday". Corrected to 714 W Higgins Rd, directions rewritten via Higgins Rd (IL 72)/I-90, days claim corrected to Mon/Tue/Thu/Sat-morning. Verified live, IndexNow pinged. DB sweep confirms no other page contains "1501"/"Elmhurst".
- **FIXED — Hours normalized sitewide vs GBP** (owner screenshot = authority): Mon 10-4, Tue 10-6, Wed closed, Thu 10-6:30, Fri closed on GBP / "by appointment (surgical cases)" on site (intentional), Sat 9-2, Sun closed. Sunday added to footer.php, homepage contact table, homepage FAQ (visible + schema, validated). The stale Mon 9-6/Tue 10-7:30 schedule exists ONLY in draft page 14 (not rendered) — Google snippet is a stale crawl.
- **FIXED — AIOSEO Search Statistics** reconnected from `http://drloukas.com` to `https://www.drloukas.com/` (verified server-side).
- **OWNER — rotate OpenAI key (P0) and the exposed WP application password.**

## SEO cleanup

- **Canonical audit: PASS.** All 4 origin variants 301 single-hop → `https://www.drloukas.com/`. WP Home/Site URLs, canonical tag, og:url, sitemap URLs all www-https. No action.
- **All-on-4 cannibalization: ALREADY RESOLVED.** /all-on-x-all-on-4-dental-implants/ (2346) is a draft; its URL 301s to /all-on-4/ (2565), whose title covers both phrasings, keyphrase set, SEO score 77. = recommendation C, implemented. Follow-through: request indexing for /all-on-4/, grow implant cluster links.
- **Location pages audit: all correct except EGV (fixed).** Rosemont/Chicago/Niles/Norwood Park state hours matching GBP; all have 714 + correct phone; copy is individually written, no doorway pattern. EGV is thin (2.8KB vs ~18KB siblings) — expand with real local content.
- **OPEN — hours single source of truth:** add a `[loukas_hours]` shortcode (theme/Angie validated snippet) and swap homepage displays onto it. Footer is already theme-level.
- **OPEN — housekeeping (owner-gated):** 2 consent plugins, 2 backup plugins, MonsterInsights deletable, 9 Uncategorized posts, duplicate category pairs. After a full backup.

## Existing strengths

Clean redirect/canonical layer (361 redirects), complete metadata sitewide (as of today), full Local Business schema + completed knowledge graph, FAQPage/VideoObject coverage, real before/after assets + video library + Smile Gallery, GBP active with reviews, differentiators (two generations, implants placed+restored in-office, CBCT, CEREC, iTero, Thu evening/Sat hours), individually written location pages.

## Content opportunities — case-package pipeline (adopted strategy)

Approved case → case page → treatment-page internal link → Smile Gallery → IG/FB → GBP post → LinkedIn pro version → YouTube Short → schema.

- Patient authorization is a HARD GATE before drafting. Never publish patient-identifying info from WP media/filenames/notes.
- Pilot-ready now: crowns B/A, Botox frown-line result, TMJ masseter (imagery live on site).
- Case page anatomy: concern → diagnostics (CBCT/iTero) → plan + why → result → what similar patients should know → exact-anchor link to treatment hub.
- Invisalign: if Sept 10 GSC pull shows no recovery, next lever = fresh Invisalign case package into 1409.
- Implant cluster: bone grafting + guided surgery pages (real workflow), linking to /all-on-4/ and /dental-implants/.

## Social opportunities

- **GBP = highest leverage** for "dentist park ridge" (~13.7): weekly posts from case packages, prompt review replies (one 5-star awaiting reply), fresh photos.
- IG/FB stay patient-facing visual. Zapier connector = direct publishing path for LinkedIn + GBP, **with human approval gate for clinical/treatment-claim content**.
- TikTok + LinkedIn URLs pending owner confirmation before adding to AIOSEO sameAs. X: none, leave empty.

## LinkedIn strategy

- Company page = practice brand; Dr. Loukas personal profile = clinician authority (implant workflows, CBCT planning, digital dentistry, CE, two-generation story). Personal leads (better organic reach).
- Entity wiring once URLs confirmed: company → Organization sameAs (AIOSEO social profiles); personal → Person/author sameAs (Author SEO addon, already active).
- Cadence: 1 professional post/week, produced as the LinkedIn arm of each case package. Nothing created/published yet.

## 30-day priorities

1. Owner: rotate OpenAI key; GSC request-indexing for 7 URLs (5 queued + /all-on-4/ + /elk-grove-village-dentist/); reply to waiting review; confirm TikTok/LinkedIn URLs.
2. Hours shortcode single source of truth.
3. Pilot 3 case packages (crowns, Botox, TMJ) — social variants held for approval.
4. GBP weekly rhythm + review replies.
5. Sept 10 GSC re-pull (local session): invisalign/dentist-park-ridge baselines.
6. Plugin cleanup after full backup.
7. Expand EGV page.

## 90-day priorities

1. Implant cluster completion (bone grafting, guided surgery, full-arch comparison).
2. LinkedIn launch + sameAs wiring.
3. E-E-A-T: author pages for both doctors, Person schema, 6-10 published case pages.
4. Review velocity program.
5. Bing Webmaster Tools verification (IndexNow already pinging Bing).
6. Video completion (duration conflicts, re-request indexing).
