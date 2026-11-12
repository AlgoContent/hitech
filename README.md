# HiTECH Motorcycle - Website (hitech00bike.com)

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
3056 S State Rd 7 Ste 78, Miramar, FL 33023 (Hi Tech Motorsports) | Tue-Sat 9-6 | Text/WhatsApp 954.793.6390 | https://www.instagram.com/hi_tech_motorcycles | https://www.youtube.com/@hitech00BIKE
