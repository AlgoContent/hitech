# HITECH Asset Manifest

Drop your image files from C:\HITECH into the folders below using these EXACT names before deploy.
The site references these paths. Files marked (have) are already populated.

## assets/logos/  (brand scroller - small, transparent PNG/SVG, ~120px tall)
- honda.svg (have)
- yamaha.png
- kawasaki.png
- suzuki.png
- ducati.png
- harley-davidson.png
- bmw.png
- aprilia.png
- mv-agusta.png
- triumph.png

Tip: the scroller auto-greyscales logos and reveals color on hover. From your C:\HITECH\logo folder,
rename each brand logo to match the list above.

## assets/images/  (UI art)
- name.png         -> your HITECH wordmark logo (header)            [from C:\HITECH\name.png]
- mechanic.png     -> hero/video poster + magazine                 [from C:\HITECH\mechanic.png]
- mechanic2.png    -> magazine column image                        [from C:\HITECH\mechanic2.png]
- repairs.png      -> Services tile "Repairs"                      [your REPAIRS .png]
- performance.png  -> Services tile "Performance"                  [your PERFORMANCE .png]
- maintenance.png  -> Services tile "Maintenance"                  [your MAINTENANCE .png]
- motorcycle.png   -> Services tile "Every Machine" + OG share img [your MOTORCYCLE .png]

## assets/video/  (already populated)
- hype-11.mp4      -> hero video (have)
- hype-12.mp4      -> spare hero video (have)
- bmw_service.mp4  -> service clip (have)

## Affiliate links
Right-rail "Gear & Partners" has 8 slots. Live: realfimodel.com, dividond.com, coffeebarroasters.com.
Slots 4-8 are blank (href="#") - edit AFFILIATES in build_site.py / generate_ledger.py, then re-run.
