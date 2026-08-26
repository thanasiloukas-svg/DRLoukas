# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.
**Last updated: 2026-08-26 evening (image placement session). Treat this as the session handoff — read it fully before touching the site.**

## Project Overview

Workspace for Loukas Dentistry of Park Ridge (www.drloukas.com) — SEO, content, and site management.

## The Practice

- **Name:** Loukas Dentistry of Park Ridge
- **Doctors:** Dr. Thanasi Loukas, DMD and Dr. Maria Loukas, DDS
- **Address:** 714 W Higgins Rd, Park Ridge, IL 60068 (NO suite number, ever)
- **Phone:** (847) 696-1919 (this format only, always)
- **Brand colors:** Teal #18C6B3, Navy #06202D, Text #365F6F
- **Services:** Dental implants, Invisalign, porcelain veneers, Botox/Dysport, dermal fillers, lip filler, jawline filler, Kybella, PDO threads, cosmetic/restorative/preventive dentistry

## Connected Integrations

- **WordPress (www.drloukas.com):** primary tool, MCP prefix `mcp__www_drloukas_com__`.
- **Novamira MCP** (`mcp__Novamira_-_Loukas_Dentistry_of_Park_Ridge__`): WORKS (the older duplicate "drloukas.com" connector pointing at /novamira/v1 is broken — ignore it or ask user to remove). Gives AIOSEO redirect CRUD, wp-cli, execute-php, file access. Connects as WP user ID 1 — never break its OAuth/app passwords.
- **GitHub:** repo `thanasiloukas-svg/drloukas` via `mcp__github__` tools.
- **Google Drive** via `mcp__Google_Drive__`.
- **AIOSEO Search Statistics / GSC link — FIXED Aug 26 ~14:00 UTC:** was authed against the wrong property (`http://drloukas.com`); user reconnected via AIOSEO → Search Statistics → Reconnect and picked `https://www.drloukas.com/`. Verified server-side: `aioseo_options_internal` authedsite now `https://www.drloukas.com/`, verified true, sitemap reports point at the correct resource_id with 0 errors/warnings. Search Statistics data should backfill within a day or two of the reconnect. Note: sitemap `indexed` counts read 0 permanently — Google removed indexed counts from the Sitemaps API; not a symptom. **Rule stands: verify `profile.authedsite` matches the canonical host before trusting any Search Statistics output.** The account also has a `drloukas.com` Domain property in GSC (kept; either property is valid). Site Kit separately has no Search Console module (pagespeed, GA4, RRM, tagmanager only).
- **Google Search Console:** NO remote access. A GSC MCP server (`mcp-server-gsc`, service account `gsc-reader@numeric-anthem-506400-v4.iam.gserviceaccount.com`, key at `D:\claude Drloukas.com\gsc-key.json`) is wired on the user's Windows PC for BOTH Claude Code CLI and Claude Desktop. GSC data must be pulled in a LOCAL session or pasted in. Note: the mcp-server-gsc token refresh can fail transiently ("premature close"); a local helper with a working OAuth token lives in the `google-search-console\` folder of the user's local project.
- **Ahrefs / Semrush:** connected but useless via API — Ahrefs returns "Insufficient plan", Semrush "API units balance is zero".
- Remote sessions CANNOT fetch drloukas.com or google.com (network egress blocked); audit the site through the WordPress/Novamira MCPs.

## Novamira OAuth 429 incident (Aug 26, diagnosed in claude.ai session — PLAN ONLY, no changes made)

- The 429s on the Novamira MCP endpoint come from the **IONOS edge/proxy per-source-IP rate limit (1000 req/window, `x-ws-ratelimit-*` headers)** — not WordPress, not a plugin, not ModSecurity. WordPress and Novamira auth respond normally (clean 401s).
- Suspected driver: an **OAuth retry/re-registration loop** in a client that lost its refresh token — repeatedly hitting `/oauth/register`, `/oauth/token`, discovery, and the MCP endpoint. One cold handshake costs ~6 requests before any work.
- **Operating rules for ALL MCP sessions against this site until resolved:** keep tool calls sequential and paced (no rapid-fire/parallel bursts), one session at a time, don't toggle/reconnect connectors repeatedly, keep sessions long-lived. A 429 here means STOP and wait for the window, not retry.
- **Never** request or apply broad rate-limit exemptions (`/wp-json/`, `/wp-json/mcp/*`, `/.well-known/*`, the oauth register/token/device endpoints). If mitigation is ever needed it must be single-source-IP + exact path `/wp-json/mcp/novamira-oauth` only, time-boxed, owner-applied in the IONOS panel.
- Remediation order (owner-gated): clean disconnect/reconnect of the failing client first; then read-only inventory of Novamira OAuth admin settings (TTLs, rotation, client list, whether open dynamic registration can be disabled — likely the best hardening); Apache access-log confirmation of the looping IP. The full plan lives in the claude.ai session doc "2026-08-26-novamira-oauth-429-repair-plan".
- **OpenAI API key in `mwai_options` is treated as COMPROMISED** (surfaced in a diagnostic read). Owner rotates manually at platform.openai.com → update in AI Engine admin UI → test ARYA → revoke old key. Never pass the key through MCP, chat, or commits.

### Standing redaction rule (adopted Aug 26 — applies to every session)
When reading options/settings/config: never dump a full option when a targeted read will do; treat values matching credential patterns (`sk-`, `api_key`, `secret`, `token`, `password`, bearer strings, private keys) as sensitive; never write such values into reports, chat, artifacts, or commits — report presence and location only (e.g. "a key exists at `mwai_options.ai_envs[0].apikey`"); if a secret is retrieved incidentally, flag it for rotation and treat it as exposed from that moment.

## CRITICAL RULES — DO NOT VIOLATE

### Operational Safety
- **NEVER** use `wp_update_option` to modify `wpassetcleanup_settings` — site-wide PHP fatals
- **NEVER** write `aioseo_options` / `aioseo_options_dynamic` via `wp_update_option` — the MCP tool decodes the JSON string into an array, which corrupts AIOSEO's storage format. AIOSEO settings changes go through wp-admin UI or Novamira abilities only.
- **NEVER** change existing URL slugs, post titles, or H1s
- **NEVER** delete the old loukas theme; never modify live .htaccess
- **NEVER** add manual meta/canonical/robots tags (AIOSEO handles these)
- **NEVER** install/activate: elementor (installed but INACTIVE — leave it), elementor-pro, header-footer-elementor, bulletproof-security, all-in-one-seo-pack free (Pro 5.0.1 is the active one), google-analytics-for-wordpress, wp-super-cache, jetpack-boost*, wp-asset-clean-up
  - *Jetpack Boost was found ACTIVE on 2026-08-26 despite this list — flagged to user, left as-is.
- Never publish anything unless the user explicitly asks — default post_status draft
- No guaranteed-outcome language; no hyphens in patient-facing sentences (use commas); internal links use full drloukas.com URLs

### LOCKED Pages — ZERO WRITES:
1. ~~Homepage (ID 3258)~~ — **UNLOCKED by user Aug 26, 2026** for surgical SEO work (target "Park Ridge dentist", pos 13.7). No title/slug/H1 changes. See "Homepage SEO pass" below.
2. ~~/invisalign-park-ridge/ (ID 1409)~~ — **UNLOCKED by user Aug 26, 2026** after "invisalign park ridge il" slipped to ~9.2. Still: no title/slug/H1 changes; edits stay surgical. See "Invisalign cluster" below.
3. **/porcelain-veneers/**
4. **/botox-dysport/** — NOTE: since Aug 20 this URL 301s to /botox/ (ID 461); the Botox rankings live on /botox/ now. **/botox/ itself was worked on Aug 26 with user approval** — see "Botox page consolidation" below.
5. **/cosmetic-dentistry/**
- Never modify _aioseo_title/_description/_keyphrases on any page that already has values; never change existing titles/slugs/H1s anywhere

## SITE STATE (as of 2026-08-26)

### Content consolidation (Aug 23) — DONE, do not redo or "fix"
- ~186 legacy blog posts (2014-2020) intentionally set to **draft**. Do NOT republish.
- Replaced by consolidated guides: /healthy-teeth-at-home-guide-park-ridge/ (3972), /teeth-grinding-tmj-guide-park-ridge/ (3970), /gum-disease-guide-park-ridge/ (3967).
- **All old post URLs have 301 redirects — 361 redirects live in AIOSEO Redirects** (verified complete on Aug 26 against a full draft-post inventory; user confirmed working). Check `aioseo-redirects/list` via Novamira before creating any redirect — duplicates are rejected.
- GSC "381 not indexed" is expected fallout: redirected posts + noindexed tag/author/date archives + attachment redirects. Not a problem to fix.

### AIOSEO keyphrases — DONE (~220+ posts/pages, prior sessions). Locked pages skipped.

### Plugin change (Aug 26, claude.ai session): AIOSEO News Sitemap 1.0.21 DELETED
It was inactive, so no site output changed; reinstallable from the Elite account if ever needed (a dental practice won't need a Google News sitemap). Everything else AIOSEO untouched: Pro 5.0.1 active; free 5.0.0.1 inactive-in-place; Author SEO, Image SEO, IndexNow, Link Assistant, Local Business, Video Sitemap, Broken Link Checker active; REST API addon inactive-in-place. Elementor, Asset CleanUp, WP Super Cache, MonsterInsights, six old themes, Duplicator, WP File Manager: still present, pending owner's call on a backup — this was the ONLY deletion.

### Video SEO (Aug 26 session) — DONE
All published video watch pages under /videos/ plus service pages were audited. Fixes applied:
- VideoObject schema ADDED to /botox-parties/ (3839) and /lip-fillers-park-ridge/ (1623)
- thumbnailUrl corrected on /videos/botox-treatment-park-ridge/ (2641) and /videos/lip-filler-treatment-park-ridge/ (2642); leftover empty video div removed from 2641
- duration PT46S added to snap-in VideoObject on /implant-supported-dentures/ (2563); publisher logo fixed on 2819
- All 11 /videos/ pages verified "Submitted and indexed" via URL Inspection API, but `videoIndexingResult` empty — Google hasn't evaluated the videos themselves. Crawls predate the fixes.
- Known remaining: homepage (LOCKED) has schema-only VideoObject with no embedded video; 1409 (LOCKED) embeds video without schema; /cosmetic-dentistry/dermal-fillers/ (116) says PT6S vs watch page 2805 PT45S for the same mp4 — user to confirm real duration; pages 104/2876 YouTube VideoObjects missing duration (unknown durations).
- ~15 raw mp4 uploads in the media library sit on no watch page — these are most of GSC's "videos not indexed"; attachment URLs for them already 301 to watch pages where relevant.

### TMJ/Botox topic cluster (Aug 26) — DONE
"botox for tmj near me" (GSC pos ~30) was split across 5 pages. Fixed by differentiation + interlinking: 1850 (/botox-tmj-jaw-pain-park-ridge-il/) got FAQ + FAQPage schema + related-links; /tmj-treatment/ (1859) and /botox-for-migraines-headaches-park-ridge-il/ (3303) now cross-link to 1850. Do not create a new Botox-TMJ post — strengthen 1850 instead. Evening session: 1850 now has a masseter injection photo (attachment 4045) plus a new "Botox Is One Part of a Complete TMJ Treatment Plan" H2 covering the multifactorial approach (custom occlusal guard, anti-inflammatory treatment, muscle relaxers in selected cases).

### Invisalign cluster de-cannibalization (Aug 26, after user unlocked 1409) — DONE
"invisalign park ridge il" slipped from ~#4 to ~9.2. Cause: two live "Invisalign vs braces" pages competing (1849 /invisalign-vs-braces-park-ridge-il/ post + 1624 /braces-vs-invisalign/ page) plus orthodontics page 104. Fixes applied:
- AIOSEO canonical set on 1624 → 1849 (field was empty; 1849 chosen as survivor — geo slug, focused content, prior sessions' comparison home). Both stay live for visitors.
- 1409: fixed stray `</p></p>` in intro; comparison link repointed from 1624 to 1849; VideoObject schema ADDED for park-ridge-invisalign.mp4 (its known gap). Note: that mp4's video-canonical belongs to /videos/invisalign-results-park-ridge/ (2639) — 1409's schema is metadata support, not a watch-page claim.
- Watch "invisalign park ridge il" position in the ~Sept 10 GSC re-pull; if no recovery, next levers are fresh content on 1409 and more internal links with exact anchors.

### Homepage SEO pass (Aug 26, after user unlocked 3258) — DONE
- **Fixed broken FAQPage JSON-LD**: the schema script contained a full duplicated question array pasted after the closing brace — invalid JSON, so Google could not parse the homepage FAQ schema at all. Deduplicated; now valid.
- **Removed the schema-only VideoObject** from the @graph (it referenced YouTube 8nwlO4GGDyw with no video embedded on the page — an invalidation risk with no upside).
- Keyword presence: "Park Ridge dentist(s)" woven into hero description and The Loukas Dentistry Difference section (which also lost the off-target "among the best Chicago dentists" claim). New FAQ item "Are you accepting new patients in Park Ridge?" added to visible FAQ + schema in sync.
- **CORRECTION (evening session): the live homepage IS rendered by the theme template** `loukas-custom/front-page.php` (post 3258 content is dormant). Homepage edits go through the template file via Novamira execute-php file ops, with a backup first. Repo copies of front-page.php and assets/js/canvas.js were reverse-synced from production on Aug 26 — the repo now mirrors live; NEVER deploy an older repo copy over the live theme.

### Image placements (Aug 26 evening session) — DONE
All photos supplied by the user in chat, processed locally (Pillow crop/resize, WEBP), uploaded via chunked-base64 pipeline (see AIOSEO Technical Reference), promo pricing text and IG story frames cropped off before publishing. New attachments:
- 4045 masseter injection → 1850 hero figure
- 4048 forehead injection, 4049 eyebrow/frown injection, 4050 frown-line B/A collage → /botox/ (461) photo grid extended from 3 to 6 ld-v112 photo cards
- 4051 party treatment photo → /botox-parties/ (3839) figure before "What Guests Can Have Treated"
- 4052 crowns before + 4053 crowns after → third B/A card on /restorative-dentistry/dental-crowns/ (100)
- 4056 labeled BEFORE|AFTER crowns composite (1404×700) → full-width figure in the homepage Before & After section of front-page.php (backup: front-page.php.bak-20260826-crowns alongside the older .bak-20260826)

### Botox page consolidation (/botox/ ID 461, Aug 26) — DONE
- Merged TWO visible FAQ sections into the styled ld-v112-faq (now 10 details items); deleted the bolted-on duplicate faq-section div.
- Replaced THREE FAQPage schemas' worth of markup (one had no visible counterpart) with ONE valid FAQPage matching visible questions.
- Deleted the duplicate "Related Services" strip that contained two broken links (/tmj-treatment-park-ridge-il/, /lip-fillers-park-ridge-il/).
- Retargeted links: migraine card → /botox-for-migraines-headaches-park-ridge-il/ (was pointing at the TMJ guide); "Botox for TMJ" anchor → /botox-tmj-jaw-pain-park-ridge-il/.
- **CRITICAL FIND: /contact/ does not exist as a page.** 15 published pages (incl. locked veneers/cosmetic) had CTAs pointing at it. Fixed 461's three links to /contact-us/ and created AIOSEO redirect #366 /contact/ → /contact-us/ (301) which heals all other pages without editing them.

### SEO continuation pass (Aug 26 afternoon, remote session) — DONE
- **Internal links:** /services/ (68) Invisalign card description now carries exact anchor "Invisalign in Park Ridge, IL" → 1409 (card's "Learn more" link untouched); guides 3972/3970 "Park Ridge dentist" home anchors fixed from relative `/` to full URL; guide 3967 gained a "Park Ridge dentist" home link in its closing CTA. Homepage now has in-content links from all 3 consolidated guides.
- **Meta fills (all were EMPTY, never overwrote):** posts 3303/3604/3603 got full title+description+focus keyphrase; 13 legacy published posts (777, 737, 743, 750, 755, 760, 775, 785, 786, 795, 799, 867, 762) got focus keyphrases. `aioseo-posts/list-missing-seo` is now clean except Privacy Policy (intentionally skipped).
- **Knowledge graph schema completed** (was empty, via aioseo()->options API — safe path): organizationLogo = loukas_logo_master_transparent.png, phone = +18476961919, email = loukasgendentistry@gmail.com.
- **IndexNow pings** sent for ~15 updated URLs via aioseoIndexNow()->ping->pingPost($permalink,'publish') (reaches Bing/Yandex; Google relies on sitemap + manual GSC requests).
- **Audit findings:** AIOSEO notifications: 0. robots.txt: clean, 3 sitemaps declared, no physical file (dynamic). Sitemap config already correct (no attachments/author/date) — former pending item 1 was ALREADY DONE. Local Business fully configured (address/phone/hours/priceRange/areaServed). **ALL category archives are per-term noindexed (deliberate, prior session)** — term meta is moot, do not fill; tag archives noindexed globally. Term 5 (cosmetic dentistry cat) description was overwritten before this was discovered — zero impact (noindexed).
- **Social profile gaps:** Facebook/Instagram/YouTube set; TikTok and X/Twitter URLs empty (user has Smash Balloon TikTok feed, so a TikTok account likely exists — ask user). Webmaster Tools verification fields all empty (GSC verified via other means; Bing Webmaster Tools optional future win).
- **Plugin redundancy (report only, nothing deactivated):** TWO cookie-consent plugins active (Cookie Consent GDPR/CCPA v0.0.10 + WPConsent v1.1.8) — owner should pick one; TWO backup plugins active (All-in-One WP Migration + Duplicator) — pick one; MonsterInsights inactive vs Site Kit active (GA4 covered — MonsterInsights deletable at cleanup); WP Super Cache is now INACTIVE (state change from earlier notes; Jetpack Boost is the active cache layer); 9 published posts sit in "Uncategorized" — recategorize someday.

### uploadDate normalization (Aug 26) — DONE
GSC rich-results warned on date-only uploadDate values. All video pages scanned via execute-php; fixed to full ISO 8601 with -05:00 on: 2641, 2805, 116, 3839. Homepage 3258 still date-only (LOCKED). 2819's value was already valid (GSC warning came from stale June crawl).

### GSC snapshot (Jul 29-Aug 26 2026, URL-prefix property)
46 clicks/28d, 40 branded. "dentist park ridge": pos 13.7, 200 impr (main opportunity — homepage locked, improve via internal links/GBP/reviews). "60068 clear aligners": pos 8.2, 0 clicks (snippet loses; leave — AIOSEO fields locked). Baselines: Invisalign #4, veneers #10, Botox #13, cosmetic #9.

### GSC "Profile page" enhancement
Comes from the **AIOSEO Author SEO (E-E-A-T) addon** on author archives (noindexed). 5 admin users exist: loukaswpboss (Dr. Loukas, ID 1 — authors everything), ionos, ionos123, manus-seo-agent, manus-seo-temp. Exact GSC error text never obtained; fix via AIOSEO → Search Appearance → Author SEO when user supplies it.

## PENDING / OPEN ITEMS
0. **P0 (owner, manual, time-sensitive): rotate the OpenAI API key** (new key at platform.openai.com → enter in AI Engine admin UI → test ARYA → revoke old). ~~Reconnect AIOSEO Search Statistics~~ — DONE Aug 26, now authed to `https://www.drloukas.com/`; re-check Search Statistics data in a day or two.
1. ~~Sitemap post types click~~ — verified ALREADY CORRECT Aug 26 (posts/pages/products only, no attachments, author/date off). Nothing to do.
2. User to hit "Request indexing" in GSC UI for: /videos/botox-treatment-park-ridge/, /videos/lip-filler-treatment-park-ridge/, /botox-parties/, /lip-fillers-park-ridge/, /implant-supported-dentures/.
3. Confirm real duration of video_20220414_1.mp4 (dermal filler) → align 116 vs 2805 schema.
4. Verify all 11 /videos/ pages appear in video-sitemap.xml (5 showed "sitemaps: none" in URL Inspection).
5. Redirect hit_count is 0 on all 361 redirects — user confirmed redirects work, so it's likely just logging; ignore unless 404s reappear.
6. Video watch pages 3594-3597 still draft ("videos are not correct anyways") — leave alone.
7. Re-pull GSC top queries ~Sept 10 (local session) to measure consolidation + schema fixes.
8. Homepage front-page.php/canvas.js SFTP upload to IONOS — on user's side.
9. WP application password for user loukaswpboss appeared in chat (Aug 26) — user advised to rotate at leisure.

## AIOSEO Technical Reference

Meta fields: `_aioseo_title`, `_aioseo_description`, `_aioseo_keyphrases` (JSON: {"focus":{"keyphrase":"...","score":0,"analysis":{}},"additional":[]}), `_aioseo_og_*`, `_aioseo_twitter_*`.
Redirects: manage via Novamira abilities `aioseo-redirects/list|create|update|delete` (create rejects duplicate sources).
Content edits: prefer `wp_alter_post` (search/replace or regex, `\z` appends) over full-content rewrites. A 60s timeout on wp_alter_post does NOT mean failure — verify with execute-php before retrying (edits have applied despite the timeout).

**Image upload pipeline (remote sessions; wp_upload_media chokes on large base64):** process locally → `base64 -w0` → `split -b 26000 -d` (26000 bytes stays inline in tool output; larger gets persisted to a file) → append each chunk via execute-php `file_put_contents($f, '<chunk>', FILE_APPEND)` to `wp_upload_dir()['basedir'].'/ld-tmp-img.b64'` → **after EVERY append check the appended byte count equals the chunk size** (paste corruption adds stray bytes; repair with `ftruncate` to the expected total + `md5_file` compare) → finalize: base64_decode strict, md5 verify, write to `wp_upload_dir()['path']`, `wp_insert_attachment` + `wp_generate_attachment_metadata` + `_wp_attachment_image_alt`, unlink temp.

## Tone & Brand Voice

Professional but approachable; confident, educational, never salesy. No hyphens in patient-facing sentences (use commas). No guaranteed outcomes. Content should feel like it comes from the practice. Always tag Park Ridge, IL.
