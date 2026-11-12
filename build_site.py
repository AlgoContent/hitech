#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds index.html for HITECH MOTORCYCLE using hitech_theme."""
import csv, html, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hitech_theme as T

HERE = os.environ.get("HITECH_BASE") or os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "techs_ledger_verified_starter.csv")
def esc(s): return html.escape(str(s or "").strip())
with open(CSV, encoding="utf-8") as f:
    ROWS = list(csv.DictReader(f))

CATEGORIES = [("repairs.png","Repairs &amp; Service","No-starts, electrical, brakes, diagnostics, recalls."),
              ("maintenance.png","Maintenance","Fluids, tires, chains, valve service, intervals."),
              ("motorcycle.png","Customization","Harley &amp; European builds, bags, bars, stance, wiring."),
              ("performance.png","Dyno &amp; Performance","Dyno tuning, ECU flashing, exhaust, top-end.")]

KEYWORDS = ("motorcycle mechanic near me, motorcycle repair shop Miramar FL, motorcycle service Fort Lauderdale, "
    "motorcycle mechanic Broward County, motorcycle dyno tuning South Florida, dyno tune motorcycle Miami, "
    "ecu flashing motorcycle near me, sport bike performance shop South Florida, motorcycle tire change near me, "
    "motorcycle oil change and inspection near me, motorcycle diagnostic service Miami, "
    "independent Harley Davidson mechanic Miramar, Ducati repair shop Miami, independent Ducati mechanic Fort Lauderdale, "
    "BMW motorcycle service independent Broward, Suzuki GSXR specialist South Florida, Yamaha Kawasaki sport bike mechanic near me, "
    "motorcycle crash estimate near me, motorcycle collision repair South Florida, motorcycle carburetor cleaning near me, "
    "Miami, Miami Beach, Weston, Fort Lauderdale, Hollywood, Pembroke Pines, 33023")
DESC = ("HiTECH Motorcycle in Miramar, FL: independent motorcycle repair, service, customization and dyno "
    "tuning for Harley-Davidson, Ducati, BMW, Triumph and every sport bike. Serving Miami, Fort Lauderdale, "
    "Weston and all of South Florida. Rated %s from %s Google reviews. Tap to message the mechanic.") % (T.RATING, T.REVIEW_COUNT)

def cat_tiles():
    return "".join('<a class="cat-tile" href="%s"><img src="assets/images/%s" alt="motorcycle %s Miramar South Florida"><span class="ct-h">%s</span><span class="ct-p">%s</span></a>'%(link,img,h.lower(),h,p) for (img,h,p),link in zip(CATEGORIES,["motorcycle-repair-miramar-fl.html","motorcycle-repair-miramar-fl.html","custom-builds-south-florida.html","dyno-tuning-south-florida.html"]))

def faults_by_brand():
    order=[]; groups={}
    for r in ROWS:
        b=r["brand"]
        if b not in groups: groups[b]=[]; order.append(b)
        groups[b].append(r)
    out=[]
    for b in order:
        cards="".join('<a class="lcard" href="ledger/%s.html"><span class="lc-cat">%s</span><b>%s</b><span class="lc-yr">%s&ndash;%s</span><span class="lc-sym">%s</span><span class="lc-meta">%s &middot; %s</span></a>'%(
            esc(r["page_slug"]),esc(r["problem_category"]),esc(r["model"]).split("/")[0].strip(),
            r["year_start"],r["year_end"],esc(r["common_symptom"]),esc(r["urgency_level"]),esc(r["tsb_or_recall_id"])) for r in groups[b])
        out.append('<div class="brandgroup"><h3>%s</h3><div class="lgrid two">%s</div></div>'%(esc(b),cards))
    return "".join(out)

def schema():
    biz={"@type":["MotorcycleRepair","AutoRepair"],"@id":T.SITE+"/#business","name":T.GBP_NAME,
        "alternateName":"HITECH Motorcycle","image":T.SITE+"/assets/images/name.png","telephone":T.TEL,"email":T.EMAIL,"url":T.SITE,"priceRange":"$$",
        "areaServed":T.CITIES,
        "address":{"@type":"PostalAddress","streetAddress":T.ADDR_STREET,"addressLocality":"Miramar","addressRegion":"FL","postalCode":"33023","addressCountry":"US"},
        "geo":{"@type":"GeoCoordinates","latitude":25.9876,"longitude":-80.2098},
        "sameAs":[T.IG,T.YT],
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"09:00","closes":"18:00"}],
        "aggregateRating":{"@type":"AggregateRating","ratingValue":T.RATING,"reviewCount":T.REVIEW_COUNT,"bestRating":"5"},
        "makesOffer":[{"@type":"Offer","itemOffered":{"@type":"Service","name":n}} for n in ["Motorcycle Repair","Dyno Tuning","ECU Flashing","Maintenance","Tire Service","Brake Service","Electrical Diagnosis","Crash Estimates"]]}
    web={"@type":"WebSite","@id":T.SITE+"/#website","url":T.SITE,"name":"HITECH Motorcycle","publisher":{"@id":T.SITE+"/#business"}}
    faq={"@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":"Where is HiTECH Motorcycle and what are the hours?","acceptedAnswer":{"@type":"Answer","text":"HiTECH Motorcycle (Hi Tech Motorsports) is at "+T.ADDR+", open Tuesday to Saturday 9am-6pm, serving Miami, Fort Lauderdale, Weston and all of South Florida. Call or text "+T.PHONE+"."}},
        {"@type":"Question","name":"Do you do motorcycle dyno tuning in South Florida?","acceptedAnswer":{"@type":"Answer","text":"Yes. In-house dyno tuning, ECU flashing and performance work for sport bikes, V-twins and metric bikes across Broward and Miami-Dade."}},
        {"@type":"Question","name":"Do you work on Harley and independent dealership-level repair?","acceptedAnswer":{"@type":"Answer","text":"Yes. Independent Harley-Davidson, Ducati, BMW, Suzuki, Yamaha, Kawasaki and Honda service without dealership rates."}},
        {"@type":"Question","name":"Do you do motorcycle crash estimates and collision work?","acceptedAnswer":{"@type":"Answer","text":"Yes. Crash estimates, frame and fork inspection, and collision repair for South Florida riders and insurance work."}}]}
    return json.dumps({"@context":"https://schema.org","@graph":[biz,web,faq]})

# ----- Magazine issues -----
ISSUE02 = """
<p class="kicker">Issue 02 / Fall &amp; Winter &middot; Prime Riding Season</p>
<h2>South Florida Prime Riding Season: What to Inspect Before the First Big Run.</h2>
__TOPVID__
<p>November through April is what the rest of the country dreams about. The 3pm downpours have cleared, the humidity breaks, mornings drop into the 60s, and riders are pulling bikes out of carports from West Palm down to Miami. US-27 to Lake Okeechobee, Alligator Alley, Card Sound Road into the Keys &mdash; this is peak season.</p>
<p>The catch: a bike that sat under a cover through four months of monsoon season is not ready for an eight-hour run just because you wiped the dust off the seat. Between humidity, salt air, and ethanol fuel breakdown, idle bikes hide problems that only show up at 75 mph.</p>
<div class="pull">A bike that sat all summer isn't ready for the highway just because it starts in the driveway.</div>
<h3>The monsoon fuel-pump trap</h3>
<p>The most common breakdown we diagnose when the dry season starts is a failing or seized fuel pump &mdash; hard starts, backfiring, or stalling 10 to 15 minutes in. Clogged gas-cap weep holes let rainwater pool and drop into the tank. South Florida E10 pump gas is hygroscopic: water bonds with the ethanol and sinks to the bottom, right where the pump pickup sits. Instead of fuel, the pump draws a corrosive water-and-ethanol slurry.</p>
<p>The tell: a loud screeching whine on prime instead of a clean two-second hum; idles on the stand but starves under load; cuts out after 15 minutes once the pump heats up. The fix is to drain the tank, scope the interior for flash rust, flush it, and replace the pump and filter before you cook your injectors.</p>
__OILVID__
<h3>The pre-run checklist</h3>
<p>Four systems before you load the saddlebags. Tires: our flat, straight roads square off the center strip and leave a ridge that makes the bike resist leaning, then fall into the turn &mdash; and replace any tire with a DOT date over five years no matter the tread. Brake fluid: DOT 4 and 5.1 absorb water through the lines; dark, tea-colored fluid boils under load and fades the lever to the grip. Battery: summer heat kills the plates and the first cold snap exposes it &mdash; you want 12.6 to 12.8V at rest, and it's done if it drops below 10.5V cranking.</p>
<h3>By platform</h3>
<p><strong>Harley &amp; V-twins:</strong> milky primary oil means condensation &mdash; flush it; listen for compensator slap on cold start; inspect the drive belt for stone punctures and the stator plug near the lower crankcase for grime. <strong>Japanese sport bikes:</strong> salt air pits fork stanchions that then slice the seals onto your brakes; a chain left un-lubed after soaked rides rusts and robs power; clean caked radiator fins before you sit in A1A beach traffic. <strong>Italian &amp; European:</strong> check hydraulic clutch slave cylinders for weeping; these ECUs hate low voltage and throw ABS and quickshifter faults below spec; and Ducati timing belts age out regardless of miles &mdash; a snapped belt is valve-to-piston contact.</p>
<p>Riding season only lasts so long. Spending the best weekends waiting for a tow is avoidable with 45 minutes of bench prep. If your bike sat unstarted or took on summer rain, get it on a lift before the long miles.</p>
__VALVEVID__
"""
ISSUE02 = ISSUE02.replace("__TOPVID__", T.yt_embed("TdJlFX8Us2w", "HiTECH Motorcycle cruiser service"))
ISSUE02 = ISSUE02.replace("__OILVID__", T.yt_embed("MVhGRyn4E8A", "HiTECH Motorcycle fuel and oil service"))
ISSUE02 = ISSUE02.replace("__VALVEVID__", T.yt_embed("i4m64buhuKA", "HiTECH Motorcycle valve service"))

ISSUE01 = """
<p class="kicker">Issue 01 / Summer Service</p>
<h2>Summer Is Here. Prep the Bike for Sunset Rides.</h2>
<img class="mech" src="assets/images/mechanic2.png" alt="HITECH mechanic working on a motorcycle in South Florida">
<p>You walk toward the bike while the heat is still lifting off the pavement. Softer light, cleaner shadows, a road that stops looking like a commute and starts looking like an invitation. This is the hour motorcycles make the most sense. You are not escaping the day. You are finishing it right.</p>
<p>The sunset ride looks effortless from the outside, but the bike does not feel it as a postcard. It feels the hot start, the traffic crawl, the sudden throttle, the brake squeeze at the last yellow, the fan cycling, the chain load, and every small weakness you hoped would stay quiet.</p>
<div class="pull">You do not prep the bike because you fear the ride. You prep it because you respect it.</div>
<p>Start with the tires: pressure cold, tread read like evidence, sidewalls checked. A cupping front feels vague in a lean; old rubber does not get safer at sunset, just prettier. Then heat: coolant level, fan operation, radiator clear. A bike that suddenly runs hotter than usual is talking &mdash; listen before it shouts. Brakes get the same respect: squeeze the lever and notice firm, soft, spongy, pulsing, or late.</p>
<p>The fastest way to catch a problem is to notice the first difference, not the final failure. Did it sit too long? Did the battery struggle? Did the idle change? When you feel that first difference, send it. That is the whole point of having a shop you trust on the other end of a message.</p>
"""

HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Motorcycle Repair, Service &amp; Custom Work Miramar FL | HiTECH Motorcycle | South Florida</title>
<meta name="description" content="%(desc)s">
<meta name="keywords" content="%(kw)s">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#090A0D">
<meta name="geo.region" content="US-FL"><meta name="geo.placename" content="Miramar, Miami, Fort Lauderdale"><meta name="geo.position" content="25.9876;-80.2098"><meta name="ICBM" content="25.9876, -80.2098">
<link rel="canonical" href="%(site)s/">
<link rel="manifest" href="manifest.webmanifest">
<meta property="og:type" content="website"><meta property="og:site_name" content="HiTECH Motorcycle">
<meta property="og:title" content="Motorcycle Repair &amp; Dyno Tuning in Miramar | HiTECH Motorcycle">
<meta property="og:description" content="%(desc)s"><meta property="og:url" content="%(site)s/">
<meta property="og:image" content="%(site)s/assets/images/name.png"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="HiTECH Motorcycle | Miramar &amp; South Florida">
<meta name="twitter:description" content="%(desc)s"><meta name="twitter:image" content="%(site)s/assets/images/name.png">
%(pixels)s
<script type="application/ld+json">%(schema)s</script>
<style>%(css)s</style>
</head>
<body>
<header class="site-header">
<a class="brandlogo" href="#top"><img src="assets/images/name.png" alt="HiTECH Motorcycle logo"><span class="brand">Hitech <span>Motorcycle</span></span></a>
<nav class="nav-links" aria-label="Primary">
<a href="#services">Services</a><a href="motorcycle-repair-miramar-fl.html">Repair</a><a href="custom-builds-south-florida.html">Custom</a><a href="ledger/index.html">Tech&rsquo;s Ledger</a><a href="#faq">FAQ</a><a href="#contact">Contact</a>
</nav>
<div class="header-actions">%(msg_small)s</div>
</header>
<main id="top">

<section class="hero">
<div class="hero-copy">
<span class="issue-tag">Repair &middot; Service &middot; Custom &middot; Miramar, South Florida</span>
<h1>Motorcycle repair, service &amp; <em>custom work</em> done right.</h1>
<p class="hero-lede">Independent repair, service and customization for Harley riders, European machines and every bike in the garage &mdash; Ducati, BMW, Triumph and the sport-bike crowd too. Factory-level work without dealership rates, out of our Miramar shop, rated %(rating)s from %(revcount)s Google reviews. Dyno tuning in-house when you want it. Read the Tech&rsquo;s Ledger, then tap to send it straight to the mechanic.</p>
<div class="hero-actions">%(msg_big)s<a class="button button-dark" href="ledger/index.html">Read the Ledger</a><a class="button button-ghost" href="motorcycle-repair-miramar-fl.html">Repair &amp; Service</a></div>
<div class="cover-lines">
<div><strong>Repair &amp; Service</strong> No-starts, electrical, brakes, diagnostics, recalls.</div>
<div><strong>Customization</strong> Harley &amp; European builds, bags, bars, stance, wiring.</div>
<div><strong>Dyno &amp; Performance</strong> Dyno tuning, ECU flashing, exhaust, top-end.</div>
</div>
</div>
<aside class="hero-rail">
<div class="video-card"><video autoplay muted loop playsinline poster="assets/images/mechanic.png"><source src="assets/video/hype-11.mp4" type="video/mp4"></video>
<div class="video-cap"><h2>In the shop. On the road.</h2><p>This is what your bike sounds like when it is right.</p></div></div>
<div class="contact-card" id="contact">
<p class="eyebrow">Contact the shop</p>
<h3>%(addr)s &middot; Tue&ndash;Sat 9&ndash;6</h3>
<p>Send year, make, model, mileage, symptoms, and a short clip if sound matters.</p>
%(msg_contact)s
</div>
</aside>
</section>

%(logoband)s

<section id="services">
<div class="section-head"><div><div class="bar"></div><p class="eyebrow">What we do</p><h2>Repair. Service. Customize. Then tune.</h2></div><p>Harley, European and metric &mdash; tap a lane to see the work behind it.</p></div>
<div class="cat-grid">%(cattiles)s</div>
</section>

<section id="magazine">
<div class="section-head"><div><div class="bar"></div><p class="eyebrow">HITECH Magazine</p><h2>The Tech&rsquo;s Ledger, long form.</h2></div><p>Seasonal prep and straight talk from the lifts in Miramar.</p></div>
<div class="split">
<div>
<div class="issuetabs"><button class="on" onclick="showIssue(2,this)">Issue 02 &middot; Winter</button><button onclick="showIssue(1,this)">Issue 01 &middot; Summer</button></div>
<article class="mag issuepane on" id="issue2">%(issue2)s</article>
<article class="mag issuepane" id="issue1">%(issue1)s</article>
</div>
<aside class="rail">
%(partners)s
%(follow)s
</aside>
</div>
</section>

<section id="faults">
<div class="work-split">
<div>
<div class="col-head"><div class="bar"></div><p class="eyebrow">Tech&rsquo;s Ledger &middot; faults by brand</p><h2>Verified faults. Real fixes. By the bike.</h2><a class="col-see" href="ledger/index.html">See all &rarr;</a></div>
<div class="ledger-scroll"><div class="lscroll-inner">%(faultsbybrand)s</div></div>
</div>
<aside class="work-rail">
%(reviews)s
<div class="card"><h4>Talk to the mechanic</h4><p style="margin:0 0 10px">Year, make, model, mileage, and what changed. A ten-second clip beats a paragraph.</p>%(msg_rail)s</div>
%(subform)s
</aside>
</div>
</section>

<section id="videos">
<div class="section-head"><div><div class="bar"></div><p class="eyebrow">Watch</p><h2>From the shop floor.</h2></div><p>Real work on real bikes. More on <a href="%(yt)s" target="_blank" rel="noopener" style="color:#fff;text-decoration:underline">YouTube @hitech00BIKE</a>.</p></div>
%(videorotor)s
</section>

<section id="faq">
<div class="section-head"><div><div class="bar"></div><p class="eyebrow">FAQ</p><h2>Straight answers.</h2></div></div>
<div class="faq-grid">
<details open><summary>Where are you and what are the hours?</summary><p>%(addr)s. Open Tuesday to Saturday, 9am&ndash;6pm. Serving Miami, Miami Beach, Fort Lauderdale, Weston, Hollywood and Pembroke Pines. Tap Message the Mechanic to text, WhatsApp or call.</p></details>
<details><summary>Do you do dyno tuning and ECU work?</summary><p>Yes &mdash; in-house dyno tuning, ECU flashing, exhaust and top-end performance work for sport bikes, V-twins and metric bikes.</p></details>
<details><summary>What brands do you service?</summary><p>Harley-Davidson, Ducati, BMW Motorrad, Suzuki, Yamaha, Kawasaki, Honda, Aprilia, MV Agusta and most other makes &mdash; independent, without dealership rates.</p></details>
<details><summary>Do you handle crash estimates and collision work?</summary><p>Yes. Crash estimates, frame and fork inspection, and collision repair for riders and insurance work across South Florida.</p></details>
<details><summary>What should I send before bringing a bike in?</summary><p>Year, make, model, mileage, the exact symptom, when it happens, recent work, and a short video if sound or a dash warning matters.</p></details>
<details><summary>Do you serve Miami and Fort Lauderdale?</summary><p>Yes. We are in Miramar, central to Miami-Dade and Broward, and riders come to us from across South Florida.</p></details>
</div>
</section>

</main>
<footer class="footer">
<div><strong>HiTECH Motorcycle</strong>
<p>Independent motorcycle repair, dyno tuning, maintenance and crash estimates. %(addr)s. Tue&ndash;Sat 9&ndash;6. Serving Miami, Fort Lauderdale, Weston &amp; all of South Florida.</p>
<div style="margin-top:10px">%(msg_footer)s</div>
</div>
<div><strong>Find Us</strong>
<iframe title="HiTECH Motorcycle map" src="https://www.google.com/maps?q=3056+S+State+Rd+7,+Miramar,+FL+33023&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
<div><strong>Follow</strong>
<a href="%(ig)s" rel="me">Instagram &rarr;</a><a href="%(yt)s" rel="me">YouTube @hitech00BIKE &rarr;</a>
<a href="%(gr)s" target="_blank" rel="noopener">Google Reviews &rarr;</a><a href="mailto:%(email)s">%(email)s</a>
</div>
</footer>
%(mbar)s
%(js)s
<script>function showIssue(n,btn){document.querySelectorAll('.issuepane').forEach(function(p){p.classList.remove('on')});document.getElementById('issue'+n).classList.add('on');document.querySelectorAll('.issuetabs button').forEach(function(b){b.classList.remove('on')});btn.classList.add('on');}</script>
</body>
</html>"""

out = HTML % {"desc":DESC,"kw":KEYWORDS,"site":T.SITE,"schema":schema(),"css":T.CSS(),"pixels":T.PIXELS,"videorotor":T.video_rotator(),
    "addr":T.ADDR,"email":T.EMAIL,"ig":T.IG,"yt":T.YT,"gr":T.GOOGLE_REVIEWS,"js":T.JS,"mbar":T.mobile_bar(),
    "rating":T.RATING,"revcount":T.REVIEW_COUNT,
    "logoband":T.logo_band(),"cattiles":cat_tiles(),"partners":T.partner_rail(),"follow":T.follow_card(),
    "faultsbybrand":faults_by_brand(),"reviews":T.reviews_widget(),"subform":T.subscribe_form("Get the next Issue + shop specials","Send"),
    "issue2":ISSUE02,"issue1":ISSUE01,
    "msg_small":T.msg_button("Message",big=False),
    "msg_big":T.msg_button("Message the Mechanic"),
    "msg_contact":T.msg_button("Message the Mechanic"),
    "msg_rail":T.msg_button("Message the Mechanic"),
    "msg_footer":T.msg_button("Message the Mechanic")}
with open(os.path.join(HERE,"index.html"),"w",encoding="utf-8") as f:
    f.write(out)
print("index.html bytes:", len(out))
