#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Emits sitemap.xml, robots.txt, llms.txt, manifest, social posts, README for HiTECH."""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hitech_theme as T
HERE = os.environ.get("HITECH_BASE") or os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "techs_ledger_verified_starter.csv")
SITE, PHONE, WA, ADDR, IG, YT = T.SITE, T.PHONE, T.WA, T.ADDR, T.IG, T.YT
TODAY = "2026-11-12"
LANDING = ["motorcycle-repair-miramar-fl","custom-builds-south-florida","harley-davidson-service-repair",
           "dyno-tuning-south-florida","sport-bike-maintenance-dyno","crash-estimates-salvage-inspection"]
with open(CSV, encoding="utf-8") as f: ROWS = list(csv.DictReader(f))

def w(rel, text):
    p = os.path.join(HERE, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as fh: fh.write(text)
    print("wrote", rel, len(text))

# sitemap
urls=[(SITE+"/","1.0","weekly")]
for s in LANDING: urls.append((SITE+"/"+s+".html","0.9","monthly"))
urls.append((SITE+"/ledger/index.html","0.9","weekly"))
for r in ROWS: urls.append((SITE+"/ledger/"+r["page_slug"]+".html","0.8","monthly"))
sm=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for loc,pr,ch in urls: sm.append("  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>"%(loc,TODAY,ch,pr))
sm.append("</urlset>"); w("sitemap.xml","\n".join(sm))

# robots - allow AI/answer engines incl. Alibaba/Qwen + ByteDance
ai_bots=["GPTBot","OAI-SearchBot","ChatGPT-User","Google-Extended","GoogleOther","ClaudeBot","anthropic-ai","Claude-Web",
    "PerplexityBot","Perplexity-User","Applebot-Extended","Bingbot","CCBot","Amazonbot","Bytespider","PetalBot",
    "Qwenbot","AlibabaBot","Alibaba-site-verification","YouBot","cohere-ai","Diffbot","Timpibot","meta-externalagent"]
rb=["User-agent: *","Allow: /",""]
rb.append("# Answer-engine / AI crawlers welcome (AEO: ChatGPT, Gemini, Claude, Perplexity, Alibaba Qwen, Bing)")
for b in ai_bots: rb.append("User-agent: %s"%b); rb.append("Allow: /")
rb.append(""); rb.append("Sitemap: %s/sitemap.xml"%SITE); w("robots.txt","\n".join(rb)+"\n")

# llms.txt
ledger_lines="\n".join("- [%s](%s/ledger/%s.html): %s"%(r["seo_title"],SITE,r["page_slug"],r["meta_description"]) for r in ROWS)
land_lines="\n".join("- [%s](%s/%s.html)"%(s.replace("-"," ").title(),SITE,s) for s in LANDING)
llms="""# HiTECH Motorcycle (Hi Tech Motorsports)

> Independent motorcycle repair, dyno tuning, maintenance and crash estimates in Miramar, FL.
> Serving Miami, Miami Beach, Fort Lauderdale, Weston, Hollywood, Pembroke Pines and all of South Florida.
> Rated %s from %s Google reviews.

## Contact
- Business name (Google): %s
- Address: %s
- Phone / Text / WhatsApp: %s (%s)
- Hours: Tuesday-Saturday 9:00-18:00
- Instagram: %s
- YouTube: %s
- Website: %s

## Services (high-intent)
- Motorcycle repair & diagnostics (no-start, electrical, brakes)
- Dyno tuning & ECU flashing (sport bikes, V-twins, metric)
- Scheduled maintenance (oil, tires, chains, valve service)
- Independent Harley-Davidson / American V-twin service
- Sport bike & metric service (Suzuki GSX-R, Yamaha R1/R6, Kawasaki ZX, Honda CBR)
- Crash estimates, collision repair, frame & fork inspection

## Service pages
%s

## The Tech's Ledger (verified, recall-backed issues)
%s

## How to engage
Tap "Message the Mechanic" and text or WhatsApp %s with year, make, model, mileage, the symptom,
when it happens, and a short video if sound matters.
"""%(T.RATING,T.REVIEW_COUNT,T.GBP_NAME,ADDR,PHONE,WA,IG,YT,SITE,land_lines,ledger_lines,PHONE)
w("llms.txt",llms)

# manifest
w("manifest.webmanifest","""{
  "name": "HiTECH Motorcycle",
  "short_name": "HiTECH",
  "description": "Motorcycle repair, dyno tuning and service in Miramar, South Florida.",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#090A0D",
  "theme_color": "#090A0D",
  "icons": [ { "src": "assets/images/name.png", "sizes": "512x512", "type": "image/png" } ]
}
""")

# social posts
def tags(): return "#motorcycle #motorcyclelife #sportbike #harleydavidson #ducati #dynotuning #miami #fortlauderdale #miramar #southflorida #motorcyclerepair #hitechmotorcycle"
yt_map={"Suzuki":"https://youtu.be/P54eoe9m_Lk","Yamaha":"https://youtu.be/smVENbJfOvc","Kawasaki":"https://youtu.be/gOxCroShxfA","Harley-Davidson":"https://youtube.com/shorts/k9_scg88oqQ"}
seen=[]; brand_posts=[]
for r in ROWS:
    if r["brand"] in seen: continue
    seen.append(r["brand"]); brand_posts.append(r)
bp="\n\n".join("### %s\n**Hook:** %s on your %s? Here's exactly why &mdash; and the fix.\n**Body:** %s. We broke it down in the Tech's Ledger: symptom, real cause, official repair. No guessing. Independent %s service in Miramar for Miami, Fort Lauderdale & all of South Florida.\n**CTA:** Tap to message the mechanic. Full breakdown: %s/ledger/%s.html%s\n**Tags:** %s"%(
    r["brand"], r["common_symptom"].split(" or ")[0].capitalize(), r["brand"], r["common_symptom"].capitalize(), r["brand"],
    SITE, r["page_slug"], ("\n**Video:** "+yt_map[r["brand"]]) if r["brand"] in yt_map else "", tags()) for r in brand_posts)
social="""# HiTECH Motorcycle - Social Posts (ready to publish)

Tone: motorcycle mechanic + rider, 2nd person, no hype. Every post ends with a clear CTA.
Open Graph + Twitter tags are on every page, so links preview on Facebook, Instagram and LinkedIn.

---

## Launch / season post (FB / IG / LinkedIn)

**Facebook / LinkedIn:**
Prime riding season is here. Your bike sat through four months of South Florida monsoon &mdash; it isn't
ready for an 8-hour run just because you wiped the dust off the seat.

Fuel pumps full of ethanol slurry, squared-off tires, brake fluid that's boiling, batteries that cranked
all summer and are about to quit the first cold morning. We prep bikes right: fuel, brakes, charging,
suspension, chains. Harley, sport, metric, European.

Independent repair + in-house dyno tuning in Miramar. Serving Miami, Fort Lauderdale & all of South Florida.
Rated %s from %s Google reviews.

Tap to message the mechanic: %s
Read the Tech's Ledger: %s/ledger/index.html

**Instagram caption:**
Prime season is here. Is your bike actually ready? 🏍️
Independent repair + dyno tuning. Miramar, South Florida.
%s ⭐ on Google. Link in bio.
%s

---

## Service spotlight posts

**Dyno tuning:** A mod without a tune isn't performance &mdash; it's imbalance. In-house dyno + ECU flashing.
%s/dyno-tuning-south-florida.html

**Crash estimate:** Down the bike? The damage you see is rarely the whole story. Honest estimates + frame/fork
inspection. %s/crash-estimates-salvage-inspection.html

---

## Per-brand posts (rotate one per week)

%s

---

## Posting checklist
- Facebook Page: paste body, attach the page link (OG image auto-loads), publish.
- Instagram: image/reel + caption; put %s in bio.
- LinkedIn: use the FB/LinkedIn body.
- Reply to the first 3 comments within an hour to boost reach.
"""%(T.RATING,T.REVIEW_COUNT,WA,SITE,T.RATING,tags(),SITE,SITE,bp,SITE)
w("social/social-posts.md",social)

# README
readme="""# HiTECH Motorcycle - Website (hitech00bike.com)

Static site on Vercel. Homepage (magazine Issue 01 + 02, Tech's Ledger faults, reviews, dyno/service lanes),
22 verified Tech's Ledger pages, and 5 service+city landing pages. Built programmatically from
`data/techs_ledger_verified_starter.csv` + `hitech_theme.py`.

## Rebuild after editing content
```
python3 generate_ledger.py   # 22 ledger pages + ledger index
python3 build_site.py         # homepage
python3 build_landing.py      # 5 service/city landing pages
python3 build_deploy.py       # sitemap, robots, llms.txt, manifest, social
```
(To point at another folder: set HITECH_BASE env var.)

## Key files to edit
- Affiliates / partners, reviews, YouTube video IDs, pixel IDs: `hitech_theme.py`
- Analytics: paste Google (G-XXXX) and Meta Pixel IDs in the PIXELS block in `hitech_theme.py`.
- Google reviews: aggregate rating/count in `hitech_theme.py` (RATING / REVIEW_COUNT); swap the
  highlight lines in REVIEW_HIGHLIGHTS; GOOGLE_REVIEWS is the link out.
- Shop videos: the homepage "From the shop floor" grid pulls YouTube IDs from YT_VIDEOS in `hitech_theme.py`.

## SEO / AEO
- Per-page meta + canonical + OG/Twitter (FB/IG/LinkedIn previews).
- JSON-LD: MotorcycleRepair/AutoRepair (LocalBusiness) with Tue-Sat hours + AggregateRating, WebSite,
  FAQPage, Service, TechArticle, HowTo.
- llms.txt + AI-crawler allows in robots.txt (ChatGPT, Gemini, Claude, Perplexity, Alibaba Qwen, Bing).
- Sitemap already submitted in Google Search Console: sitemap.xml.

## Contact baked in
%s (Hi Tech Motorsports) | Tue-Sat 9-6 | Text/WhatsApp %s | %s | %s
"""%(ADDR,PHONE,IG,YT)
w("README.md",readme)
print("DONE")
