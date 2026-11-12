#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HITECH Tech's Ledger generator. ~1500-word 2nd-person pages from the CSV,
brand-matched YouTube embeds, racing theme. Override base with HITECH_BASE."""
import csv, html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hitech_theme as T

HERE = os.environ.get("HITECH_BASE") or os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "data", "techs_ledger_verified_starter.csv")
OUT = os.path.join(HERE, "ledger")
os.makedirs(OUT, exist_ok=True)
SITE, PHONE, TEL, ADDR, IG, YT, EMAIL = T.SITE, T.PHONE, T.TEL, T.ADDR, T.IG, T.YT, T.EMAIL

def esc(s): return html.escape(str(s or "").strip())
def wc(text): return len(re.sub("<[^>]+>", " ", text).split())

BRAND_NOTE = {
 "Honda": "Honda builds a bike that usually just runs, so when one acts up riders tend to ignore it longer than they should. That habit is the real risk here. The machine earned its trust, and that trust talks you out of stopping when you should stop.",
 "Yamaha": "Yamaha sport bikes feel tight and willing right up until a part lets go, and the crossplane engines especially hide stress well. A Yamaha rarely warns you twice, so the first odd signal is the one you act on.",
 "Kawasaki": "Kawasaki runs hard and the green bikes get ridden hard, which means a small assembly fault gets found at the worst possible rpm. Treat anything on a ZX as a high-load problem first.",
 "Suzuki": "Suzuki keeps things simple and honest, but simple parts still wear and recalls still apply. On a GSX-R the feel through the lever and the front end tells you most of what you need before any tool comes out.",
 "Harley-Davidson": "A Harley lives with vibration as a design trait, and vibration loosens, chafes, and fatigues things over miles. On these bikes you check connections, routing, and fasteners before you ever suspect something exotic.",
 "Ducati": "Ducati gets called fragile and that is lazy. These bikes are sensitive, not weak. They want clean voltage, correct torque, and the right fluid, and they reward a tech who respects the spec instead of guessing.",
 "Aprilia": "Aprilia packs serious engineering into a small package, and that density means a single component can take down a system. On these you follow the recall population first and the symptom second.",
 "MV Agusta": "MV Agusta is built like jewelry with a redline, and the tolerances are tight enough that a clamp or a torque value matters more than it would on a softer bike. Precision in, precision out.",
}
CATEGORY_NOTE = {
 "Fuel System": "Fuel problems lie to you. They feel like ignition, they feel like a sensor, they feel like a tired battery, and then the bike dies on a heat-soaked restart and the pump is the answer all along. Pressure and prime tell the truth.",
 "Transmission": "A gearbox rarely fails clean. It warns with a false neutral, a notchy shift, a missed gear under load, and riders learn to ride around it instead of through it. By the time it is loud, the damage is already done.",
 "Electrical": "Electrical faults are pattern problems, not part problems. The same melted connector, the same lazy ground, the same overworked lead shows up bike after bike. Find the pattern and you find the fix.",
 "Engine Lubrication": "Oil pressure is not negotiable. The moment a relief valve, a passage, or a pump misbehaves, the clock starts on the whole engine. This is a stop-now category, not a watch-and-see one.",
 "Ignition": "Ignition stumbles read like fuel and fuel reads like ignition. The trick is to stop swapping parts and start reading the spark event under the exact condition the rider describes.",
 "Brakes": "Brakes are where confidence and physics meet. A lever can feel fine in the lot and go long at the bottom of a hard stop. You test braking under the load it will actually see, not at idle.",
 "Wheels / Chassis": "Wheels and chassis carry every input you give the bike. A defect here does not announce itself politely. It shows up as a shimmy, a flat spot, or a crack you only find because you went looking.",
 "Frame / Chassis": "The frame is the one part you cannot ride around. A chassis fault changes how every other system behaves, so you verify it before you trust anything bolted to it.",
 "Engine": "Engine recalls are the ones that end rides early. When the manufacturer calls for inspection or replacement, the failure mode is usually severe and fast, so the bench takes priority over the road.",
 "Suspension": "Suspension faults sneak up because the bike still rolls. The danger is contact, clearance, and control under load, not whether it idles. You check it static and under compression.",
 "Steering / Front end": "The front end is where a fault becomes a crash. Any play, any clamp issue, any torque concern at the steering gets verified first because there is no good version of losing the front.",
 "Driveline": "Driveline faults put energy where it should not go. A loose wheel, a tired shaft, a worn cush drive: each one turns clean power into a problem you feel through the seat before you understand it.",
}
def cat_key(c):
    for k in CATEGORY_NOTE:
        if k.lower() in c.lower(): return k
    cl = c.lower()
    if "brake" in cl: return "Brakes"
    if "suspension" in cl or "axle" in cl: return "Suspension"
    if "steering" in cl: return "Steering / Front end"
    if "wheel" in cl or "chassis" in cl: return "Wheels / Chassis"
    if "light" in cl or "electric" in cl: return "Electrical"
    return "Engine"

def urg_line(u):
    u = (u or "").lower()
    if "stop" in u: return "This one is a stop-riding call. Not &ldquo;finish your route and deal with it later&rdquo; &mdash; park it."
    if "high" in u: return "This rates high. You can move the bike, but you do it deliberately and you get it looked at now, not next month."
    return "This sits in the middle. It will not strand you today, but ignoring it is how a cheap fix turns into an expensive one."

def steps_list(raw):
    out = []
    for p in raw.split(";"):
        p = re.sub(r"^\s*\d+\s*", "", p.strip())
        if p: out.append(p[0].upper() + p[1:])
    return out

def header():
    return """<header class="site-header">
<a class="brandlogo" href="../index.html"><img src="../assets/images/name.png" alt="HiTECH Motorcycle logo"><span class="brand">Hitech <span>Motorcycle</span></span></a>
<nav class="nav-links" aria-label="Primary">
<a href="../index.html#services">Services</a><a href="../dyno-tuning-south-florida.html">Dyno Tuning</a><a href="index.html">Tech&rsquo;s Ledger</a><a href="../index.html#faq">FAQ</a><a href="../index.html#contact">Contact</a>
</nav>
<div class="header-actions">%s</div>
</header>
%s""" % (T.msg_button("Message", big=False), T.logo_band("../"))

def footer():
    maps = "https://www.google.com/maps?q=3056+S+State+Rd+7,+Miramar,+FL+33023&output=embed"
    return """<footer class="footer">
<div><strong>HiTECH Motorcycle</strong>
<p>Repair, dyno tuning, maintenance &amp; crash estimates. %s. Tue&ndash;Sat 9&ndash;6. Serving Miami, Fort Lauderdale, Weston &amp; all of South Florida.</p>
<div style="margin-top:10px">%s</div>
</div>
<div><strong>Find Us</strong>
<iframe title="HiTECH Motorcycle map" src="%s" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
<div><strong>Follow</strong>
<a href="%s" rel="me">Instagram &rarr;</a><a href="%s" rel="me">YouTube @hitech00BIKE &rarr;</a><a href="%s" target="_blank" rel="noopener">Google Reviews &rarr;</a><a href="mailto:%s">%s</a>
</div>
</footer>
%s
%s""" % (ADDR, T.msg_button("Message the Mechanic"), maps, IG, YT, T.GOOGLE_REVIEWS, EMAIL, EMAIL, T.mobile_bar(), T.JS)

def video_card():
    return ('<div class="video-card" style="min-height:210px"><video autoplay muted loop playsinline poster="../assets/images/mechanic.png">'
            '<source src="../assets/video/hype-11.mp4" type="video/mp4"></video></div>')

def build_body(r, related):
    b, m = esc(r["brand"]), esc(r["model"])
    yr = r["year_start"] if r["year_start"] == r["year_end"] else "%s&ndash;%s" % (r["year_start"], r["year_end"])
    symptom = esc(r["common_symptom"]); cause = esc(r["likely_cause"]); fix = esc(r["how_to_fix"])
    cat = esc(r["problem_category"]); catn = CATEGORY_NOTE[cat_key(cat)]; brandn = BRAND_NOTE.get(r["brand"], "")
    tip = esc(r["tech_pro_tip"]); recall = esc(r["tsb_or_recall_id"]); srctype = esc(r["status_source"])
    ride = esc(r["ridability"]); urg = esc(r["urgency_level"]); track = esc(r["vibe_track"])
    plat = esc(r["engine_platform"]); steps = steps_list(r["diagnostic_steps"])
    name = ("%s %s %s" % (yr, b, m)).replace("&ndash;", "-")
    vid = T.yt_for(r["brand"], r["problem_category"])
    P = []
    P.append('<h2>The scene</h2>')
    P.append('<p>You know the bike. You know how it sounds on a cold start, how it settles at idle, how it pulls when the road finally opens. So when a %s %s does this &mdash; %s &mdash; you notice it before anyone else would. That instinct is worth more than any scan tool. The trick is not ignoring it because the rest of the bike still feels fine.</p>' % (b, m, symptom.lower()))
    P.append('<p>This page is for the %s %s and the riders living with it right now. It is written the way it would get explained on the shop floor: what you are feeling, why it happens, whether you should keep riding, and exactly how it gets fixed. No fear, no hype, no chasing noise. Just the pattern and the path through it.</p>' % (yr, m))
    P.append('<div class="pull">%s.</div>' % symptom)
    P.append('<p>%s</p>' % catn)
    P.append('<h2>What is actually happening</h2>')
    P.append('<p>Here is the mechanical truth. %s. That is not a guess and it is not a forum rumor &mdash; it is the failure mode tied to this exact platform. The %s setup in the %s puts this component in a spot where the problem shows up under real riding conditions, not on a stand in a clean shop.</p>' % (cause, plat, m))
    P.append('<p>Why does it fool people? Because the symptom and the source sit in different places. You feel %s, so your gut sends you toward the obvious suspect. Meanwhile the real cause &mdash; %s &mdash; sits quietly upstream doing the damage. A tech who has seen this a few times stops trusting the obvious and starts trusting the pattern. %s</p>' % (symptom.lower(), cause.lower(), brandn))
    P.append('<p>That is the whole game with a known fault. One %s doing this is a story. A documented population of them doing the same thing is a signal, and a signal you can act on with confidence instead of throwing parts at it.</p>' % m)
    P.append('<h2>Watch: inside the shop</h2>')
    P.append('<p>Here is real work on bikes like this from the HiTECH bench. Same diagnostic discipline, same order of operations.</p>')
    P.append(T.yt_embed(vid, "HiTECH Motorcycle %s service" % b))
    P.append('<h2>Can you keep riding it?</h2>')
    P.append('<p>%s The honest read on this %s is: <strong>%s</strong>. Ridability is not about whether the bike will roll out of the driveway today. It is about what happens at the worst moment &mdash; the on-ramp, the heat-soaked restart, the panic stop, the lean you did not plan for. That is the moment a %s fault collects on its debt.</p>' % (urg_line(urg), m, ride, cat.lower()))
    P.append('<p>Treat the urgency level as a floor, not a ceiling. If your bike is showing this and you are not sure, the safe move is the cheap move: stop, send us the details, and let someone who has seen it decide. A tow is annoying. The alternative on this category is worse.</p>')
    P.append('<h2>How a tech diagnoses it</h2>')
    P.append('<p>You do not start by taking things apart. You start by confirming you are chasing the right problem on the right bike. Here is the order it actually gets worked, step by step.</p>')
    if steps:
        P.append('<ol class="steps">' + "".join("<li>%s</li>" % esc(s) for s in steps) + '</ol>')
    P.append('<p>Notice what that sequence does. It verifies the bike qualifies before any cover comes off, it reproduces the complaint instead of assuming it, and it confirms the repair worked under load before the bike goes back to you. Skip a step and you end up guessing. Follow it and the %s tells you what it needs.</p>' % m)
    P.append('<h2>The fix</h2>')
    P.append('<p>The repair the manufacturer specifies is direct: %s. This is documented under <strong>%s</strong>, sourced from %s. That matters for two reasons. First, on a recall the parts and labor are usually covered, so you are not paying out of pocket for a factory defect. Second, the corrected part is an updated design &mdash; it is not the same component going back in to fail again on the same schedule.</p>' % (fix, recall, srctype))
    P.append('<p>What HiTECH does on a %s like this is straightforward. We confirm eligibility, document the symptom you reported, perform the corrective work to spec, and road test the bike under the conditions that exposed the fault in the first place. You leave with the work done right and the paper to prove it.</p>' % m)
    P.append('<div class="callout"><b>30-year shop note</b>%s</div>' % tip)
    P.append('<p>That note is the difference between a parts-swapper and a tech. Anyone can read a bulletin. Knowing how the failure actually shows up &mdash; what to look at before you commit to the teardown &mdash; is what keeps the repair clean and keeps you from paying for the same job twice.</p>')
    P.append('<h2>Why South Florida makes this worse</h2>')
    P.append('<p>Where you ride changes how fast a fault grows, and South Florida is not kind to a %s. The heat sits on the engine in stop-and-go traffic from Miami to Fort Lauderdale, and a %s problem that would stay quiet in a dry, cool climate gets pushed harder here every single ride. Heat soak, humidity, and salt air off the Atlantic all accelerate the exact failure mode this bike already has on paper.</p>' % (m, cat.lower()))
    P.append('<p>That is why we tell local riders not to measure the problem by miles alone. A %s that lives in this climate ages on a different clock. The corrosion starts sooner, the connectors work harder, the fluids cook faster, and the part the bulletin warns about reaches its limit ahead of schedule. If your bike spends its summers idling in Miami-Dade or Broward traffic, you are on the front edge of this, not the back of it.</p>' % m)
    P.append('<p>None of that means panic. It means timing. Catch a %s fault on a %s early down here and it is a scheduled repair. Catch it late and it is a tow off I-95 in August. The climate is the reason the second one happens more than it should, and the reason a quick message to the shop is worth more here than almost anywhere else.</p>' % (cat.lower(), b))
    P.append('<h2>What waiting actually costs</h2>')
    P.append('<p>Riders put this off for one of two reasons: the bike still runs, or they are afraid of the bill. Both are understandable and both are how a small job turns into a big one. On a %s fault, the failed part rarely fails alone. It takes neighbors with it, and the longer it runs compromised, the more of the bike it drags into the repair.</p>' % cat.lower())
    P.append('<p>Run the math the honest way. The corrective work on this is defined and, under %s, often covered. Wait until it lets go and you are no longer paying for one repair &mdash; you are paying for the collateral, the downtime, and whatever the failure did at speed. There is no version of a %s problem on a %s that gets cheaper by being ignored. It gets more expensive and more dangerous on the same curve.</p>' % (recall, cat.lower(), m))
    P.append('<h2>What to send us before you bring it in</h2>')
    P.append('<p>Make the intake easy and we move faster. Tap Message the Mechanic and send the year, make, model and mileage, then the exact symptom in your words. Tell us when it happens &mdash; cold, hot, in traffic, on the highway, after it sits. Note any work done recently and whether the bike is stock. If sound or a dash warning is part of it, send a ten-second clip. On a %s that detail often points straight at the answer before the bike is even on the lift.</p>' % m)
    P.append('<p>The riders who get the fastest turnaround are the ones who describe the first difference they noticed, not the final failure. &ldquo;It felt different when hot last week&rdquo; is a better starting point than &ldquo;it died on me today.&rdquo; You ride this bike every day. You are the best sensor it has.</p>')
    P.append('<div class="pull">Every symptom is a signal. Once you learn the rhythm, you stop guessing and start fixing.</div>')
    P.append('<p>That is the whole Ledger mindset, and it is why this section exists. A good mechanic does not chase the loudest noise on the bike. They follow the pattern, and on a %s %s %s the pattern is already written down. You just needed someone to translate it. Now you have it &mdash; so do not sit on a %s problem hoping it gets quiet. Send it over, and let&rsquo;s get you back on the road. Vibe track for this one: %s.</p>' % (yr, b, m, cat.lower(), track))
    if related:
        rel = '<div class="card relband"><h4>More in the Ledger</h4>' + "".join(
            '<a href="%s.html">%s %s &mdash; %s</a>' % (esc(rr["page_slug"]), esc(rr["brand"]), esc(rr["model"]).split("/")[0].strip(), esc(rr["problem_category"])) for rr in related) + '</div>'
    else:
        rel = ''
    return "\n".join(P), rel, name

def json_ld(r, name, url):
    cat = esc(r["problem_category"])
    art = {"@context":"https://schema.org","@type":"TechArticle","headline":esc(r["seo_title"]),
        "description":esc(r["meta_description"]),"about":"%s %s issue" % (name, cat),"articleSection":"Tech's Ledger",
        "keywords":esc(r["keywords"]),"datePublished":"2026-03-25","dateModified":"2026-11-12",
        "author":{"@type":"Organization","name":"HiTECH Motorcycle"},
        "publisher":{"@type":"Organization","name":"HiTECH Motorcycle","address":{"@type":"PostalAddress","streetAddress":T.ADDR_STREET,"addressLocality":"Miramar","addressRegion":"FL","postalCode":"33023","addressCountry":"US"}},
        "mainEntityOfPage":url}
    howto = {"@context":"https://schema.org","@type":"HowTo","name":"How to diagnose %s %s issue" % (name, cat.lower()),
        "step":[{"@type":"HowToStep","position":i+1,"text":esc(s)} for i,s in enumerate(steps_list(r["diagnostic_steps"]))]}
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":"Why does my %s have this problem?" % name,"acceptedAnswer":{"@type":"Answer","text":esc(r["likely_cause"])+"."}},
        {"@type":"Question","name":"Is it safe to ride my %s with this issue?" % name,"acceptedAnswer":{"@type":"Answer","text":"Urgency is rated %s; ridability is %s. Verify your VIN against %s and contact HiTECH Motorcycle at %s." % (esc(r["urgency_level"]), esc(r["ridability"]), esc(r["tsb_or_recall_id"]), PHONE)}},
        {"@type":"Question","name":"How is the %s issue fixed?" % name,"acceptedAnswer":{"@type":"Answer","text":esc(r["how_to_fix"])+" Documented under %s." % esc(r["tsb_or_recall_id"])}}]}
    biz = {"@context":"https://schema.org","@type":["MotorcycleRepair","AutoRepair"],"name":T.GBP_NAME,"alternateName":"HiTECH Motorcycle","telephone":TEL,"url":SITE,
        "image":"%s/assets/images/name.png" % SITE,"address":{"@type":"PostalAddress","streetAddress":T.ADDR_STREET,"addressLocality":"Miramar","addressRegion":"FL","postalCode":"33023","addressCountry":"US"},
        "areaServed":T.CITIES,"sameAs":[IG,YT],"aggregateRating":{"@type":"AggregateRating","ratingValue":T.RATING,"reviewCount":T.REVIEW_COUNT,"bestRating":"5"}}
    return "\n".join('<script type="application/ld+json">%s</script>' % json.dumps(x) for x in (art, howto, faq, biz))

def page(r, related):
    body, rel, name = build_body(r, related)
    slug = esc(r["page_slug"]); url = "%s/ledger/%s.html" % (SITE, slug)
    yr = r["year_start"] if r["year_start"] == r["year_end"] else "%s-%s" % (r["year_start"], r["year_end"])
    title = esc(r["seo_title"]); desc = esc(r["meta_description"]); kws = esc(r["keywords"])
    cat = esc(r["problem_category"]); src = esc(r["source_link"])
    brand = esc(r["brand"]); modelshort = esc(r["model"]).split("/")[0].strip()
    head = """<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s | HiTECH Motorcycle Miramar</title>
<meta name="description" content="%s">
<meta name="keywords" content="%s, motorcycle repair Miami, motorcycle mechanic Fort Lauderdale, %s specialist South Florida, Miramar motorcycle service">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#090A0D">
<meta name="geo.region" content="US-FL"><meta name="geo.placename" content="Miramar, Miami, Fort Lauderdale">
<link rel="canonical" href="%s">
<meta property="og:type" content="article"><meta property="og:title" content="%s">
<meta property="og:description" content="%s"><meta property="og:url" content="%s">
<meta property="og:image" content="%s/assets/images/repairs.png"><meta property="og:site_name" content="HiTECH Motorcycle">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s">
%s
%s
<style>%s</style></head><body>
%s
<main class="wrap">
<nav class="crumbs"><a href="../index.html">HITECH</a> / <a href="index.html">Tech&rsquo;s Ledger</a> / %s %s</nav>
<div class="lede-grid">
<div>
<p class="kicker">Tech&rsquo;s Ledger &middot; %s &middot; %s</p>
<h1>%s</h1>
<p class="deck">%s</p>
<div class="meta-row"><span class="tag red">%s</span><span class="tag blue">%s</span><span class="tag">%s</span><span class="tag">%s</span><span class="tag">Recall %s</span></div>
<div class="tools">%s<a class="button button-ghost" href="%s">Follow on IG</a><a class="button button-ghost" href="%s">YouTube</a></div>
</div>
<aside class="rail">%s
%s
%s
%s
%s
</aside>
</div>
<article class="body">
%s
<div class="verify"><strong>Verify before you wrench.</strong> This is recall-aware content, not a substitute for a VIN check. Confirm your bike against <a href="%s" target="_blank" rel="noopener">%s &mdash; %s</a>. Last verified %s.</div>
<div class="cta-block">
<h3>Got this on your %s? Don&rsquo;t sit on it.</h3>
<p>Tap to send the mechanic your year, make, model, mileage and symptom. Independent %s service for Miami, Fort Lauderdale and all of South Florida &mdash; without dealership rates.</p>
<div class="cta-actions">%s<a class="button button-ghost" href="%s">Follow on IG</a><a class="button button-ghost" href="%s">YouTube</a></div>
</div>
</article>
</main>
%s
</body></html>""" % (
        title, desc, kws, modelshort.lower() if modelshort else brand.lower(), url, title, desc, url, SITE, title, desc,
        T.PIXELS, json_ld(r, name, url), T.CSS(), header(),
        brand, modelshort,
        brand, cat, esc(r["page_title"]), desc,
        esc(r["urgency_level"]), esc(r["ridability"]), yr, esc(r["bike_type"]), esc(r["tsb_or_recall_id"]),
        T.msg_button("Message the Mechanic"), IG, YT,
        video_card(), T.reviews_widget(), T.partner_rail(), T.follow_card(), rel,
        body, src, esc(r["status_source"]), esc(r["tsb_or_recall_id"]), esc(r["last_verified"]),
        brand, brand, T.msg_button("Message the Mechanic"), IG, YT, footer())
    return head, rel

def ledger_index(rows):
    order=[]; groups={}
    for r in rows:
        b=r["brand"]
        if b not in groups: groups[b]=[]; order.append(b)
        groups[b].append(r)
    blocks=[]
    for b in order:
        cards="".join('<a class="lcard" href="%s.html"><span class="lc-cat">%s</span><b>%s</b><span class="lc-yr">%s&ndash;%s &middot; %s</span><span class="lc-sym">%s</span><span class="lc-meta">%s &middot; recall %s</span></a>'%(
            esc(r["page_slug"]),esc(r["problem_category"]),esc(r["model"]).split("/")[0].strip(),
            r["year_start"],r["year_end"],esc(r["bike_type"]),esc(r["common_symptom"]),
            esc(r["urgency_level"]),esc(r["tsb_or_recall_id"])) for r in groups[b])
        blocks.append('<div class="brandgroup"><h3>%s</h3><div class="lgrid">%s</div></div>'%(esc(b),cards))
    grid="".join(blocks)
    desc = "The Tech's Ledger: verified, recall-backed motorcycle issues for Honda, Yamaha, Kawasaki, Suzuki, Harley-Davidson, Ducati, Aprilia and MV Agusta, grouped by brand. Symptom, cause, fix, and how to reach the mechanic in Miami and South Florida."
    coll = json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":"The Tech's Ledger","description":desc,"url":"%s/ledger/index.html" % SITE,"isPartOf":{"@type":"WebSite","name":"HiTECH Motorcycle","url":SITE}})
    return """<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Tech&rsquo;s Ledger | Verified Motorcycle Issues &amp; Fixes | HiTECH Motorcycle Miramar</title>
<meta name="description" content="%s">
<meta name="keywords" content="motorcycle recall fixes, Honda CBR fuel pump, Yamaha R1 transmission, Kawasaki ZX recall, Suzuki GSX-R brake, Harley electrical, Ducati Panigale recall, motorcycle repair Miami, Fort Lauderdale motorcycle service, Miramar motorcycle mechanic">
<meta name="robots" content="index, follow, max-image-preview:large"><meta name="theme-color" content="#090A0D">
<link rel="canonical" href="%s/ledger/index.html">
<meta property="og:title" content="The Tech's Ledger | HiTECH Motorcycle"><meta property="og:description" content="%s"><meta property="og:type" content="website"><meta property="og:url" content="%s/ledger/index.html">
%s
<script type="application/ld+json">%s</script>
<style>%s</style></head><body>
%s
<main class="wrap">
<nav class="crumbs"><a href="../index.html">HITECH</a> / Tech&rsquo;s Ledger</nav>
<p class="kicker">Verified &middot; Recall-backed &middot; Shop-tested</p>
<h1>The Tech&rsquo;s Ledger</h1>
<p class="deck">Every bike speaks. Most riders do not know the language &mdash; so we translated it. Real issues on real machines, grouped by brand, each tied to an official recall or bulletin, with the symptom, the cause, the fix, and a straight line to the mechanic.</p>
<div class="tools">%s<a class="button button-ghost" href="%s">Follow on IG</a><a class="button button-ghost" href="%s">YouTube</a></div>
<div style="margin-top:22px">%s</div>
</main>
%s
</body></html>""" % (desc, SITE, desc, SITE, T.PIXELS, coll, T.CSS(), header(), T.msg_button("Message the Mechanic"), IG, YT, grid, footer())

def main():
    with open(CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    by_brand = {}
    for r in rows: by_brand.setdefault(r["brand"], []).append(r)
    report = []
    for r in rows:
        sibs = [x for x in by_brand[r["brand"]] if x is not r][:3]
        if len(sibs) < 3:
            for x in rows:
                if x is not r and x not in sibs: sibs.append(x)
                if len(sibs) >= 3: break
        htmlout, _ = page(r, sibs)
        with open(os.path.join(OUT, r["page_slug"] + ".html"), "w", encoding="utf-8") as o:
            o.write(htmlout)
        report.append((r["page_slug"], wc(re.search(r'<article class="body">(.*)</article>', htmlout, re.S).group(1))))
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as o:
        o.write(ledger_index(rows))
    print("PAGES:", len(rows), "| MIN words:", min(w for _, w in report), "MAX:", max(w for _, w in report))

if __name__ == "__main__":
    main()
