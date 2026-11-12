#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builds service+city landing pages (700+ words each) for HiTECH Motorcycle."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hitech_theme as T
HERE = os.environ.get("HITECH_BASE") or os.path.dirname(os.path.abspath(__file__))

def header():
    return """<header class="site-header">
<a class="brandlogo" href="index.html"><img src="assets/images/name.png" alt="HiTECH Motorcycle logo"><span class="brand">Hitech <span>Motorcycle</span></span></a>
<nav class="nav-links" aria-label="Primary">
<a href="index.html#services">Services</a><a href="motorcycle-repair-miramar-fl.html">Repair</a><a href="custom-builds-south-florida.html">Custom</a><a href="ledger/index.html">Tech&rsquo;s Ledger</a><a href="index.html#faq">FAQ</a><a href="index.html#contact">Contact</a>
</nav><div class="header-actions">%s</div></header>
%s""" % (T.msg_button("Message", big=False), T.logo_band(""))

def footer():
    maps = "https://www.google.com/maps?q=3056+S+State+Rd+7,+Miramar,+FL+33023&output=embed"
    return """<footer class="footer">
<div><strong>HiTECH Motorcycle</strong><p>Repair, service, customization, dyno tuning &amp; crash estimates. %s. Tue&ndash;Sat 9&ndash;6. Serving Miami, Fort Lauderdale, Weston &amp; all of South Florida.</p>
<div style="margin-top:10px">%s</div></div>
<div><strong>Find Us</strong><iframe title="HiTECH Motorcycle map" src="%s" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
<div><strong>Follow</strong><a href="%s" rel="me">Instagram &rarr;</a><a href="%s" rel="me">YouTube @hitech00BIKE &rarr;</a><a href="%s" target="_blank" rel="noopener">Google Reviews &rarr;</a><a href="mailto:%s">%s</a></div>
</footer>
%s
%s""" % (T.ADDR, T.msg_button("Message the Mechanic"), maps, T.IG, T.YT, T.GOOGLE_REVIEWS, T.EMAIL, T.EMAIL, T.mobile_bar(), T.JS)

# shared short closing (kept brief to limit duplicate content)
CLOSING = ("How it works at HiTECH","So you know what to expect","""Bring us the bike, or tap Message the Mechanic first with the year, make, model and mileage and what you are after. We are at %s, open Tuesday to Saturday, 9 to 6, central to Miami-Dade and Broward so riders come to us from Miami, Miami Beach, Fort Lauderdale, Weston, Hollywood and Pembroke Pines. You get a straight assessment, a clear price before the work starts, and the honest version of what is urgent versus what can wait. Independent means factory-level work without dealership markup, and it means the same tech who diagnoses your bike is the one who fixes it. We would rather tell you the truth and lose a job than sell you work you do not need and lose your trust. That is how a shop earns a book of regulars instead of one-time tickets, and it is why so many of our customers found us by word of mouth from another rider who got treated right. Send a short video if sound, vibration or a dash warning is part of the story &mdash; ten seconds of the bike talking usually tells us more than a paragraph, and it gets you a faster, more accurate answer before the bike is ever on the lift.""" % T.ADDR)

PAGES = [
{"slug":"motorcycle-repair-miramar-fl","service":"Motorcycle Repair &amp; Service","order":1,
 "metatitle":"Motorcycle Repair &amp; Service Miramar FL | Hollywood &amp; Pembroke Pines | HiTECH",
 "desc":"General motorcycle repair and service in Miramar, FL, serving Hollywood, Pembroke Pines, Fort Lauderdale and Miami. Oil, tires, brakes, diagnostics, electrical, recalls. Tap to message the mechanic.",
 "kw":"motorcycle repair shop miramar fl, motorcycle mechanic near me, motorcycle service fort lauderdale, motorcycle oil change and inspection near me, motorcycle tire change near me, motorcycle diagnostic service miami, motorcycle mechanic broward county, motorcycle electrical repair south florida",
 "kicker":"General Service &amp; Repair","h1":"Motorcycle Repair &amp; Service in Miramar, Hollywood &amp; Pembroke Pines",
 "lede":"Oil and inspection, tire mount and balance, brakes, batteries, diagnostics, and the electrical gremlins nobody else wants. Independent shop in Miramar, central to Hollywood, Pembroke Pines, Fort Lauderdale and Miami &mdash; factory-level work without dealership rates.",
 "vids":["MVhGRyn4E8A","i4m64buhuKA"],
 "sec":[("Service that keeps the bike honest",
   ["Most breakdowns are not dramatic. They are a skipped oil change, a chain run dry, a battery past its life, a tire worn into the cords, fluid that should have been flushed a year ago. The fix is cheap when you catch it on the lift and expensive when it catches you on the highway. Our scheduled service covers fluids, chain and sprockets, tires, brakes, and the inspection that tells you what is coming before it arrives.",
    "Bring us a year, make, model and mileage and we will tell you what the bike is due for and what can wait. No upsell on parts that still have life, no skipping the one that is about to let go. That is the whole deal: you leave knowing the real condition of the machine, not a padded list."]),
  ("Diagnostics and electrical",
   ["No-starts, intermittent dash warnings, charging problems, melted connectors, and the kind of fault that only shows up when the bike is hot. This is where a lot of shops start throwing parts. We start by reading the pattern &mdash; when it happens, what changed, what the voltage is actually doing &mdash; and we find the cause instead of renting you a cure.",
    "Scope, multimeter, and the experience to know where a given platform hides its weak grounds. A no-start on a fuel-injected bike is a different hunt than one on a carbureted classic, and a charging fault on a V-twin lives in a different place than on an inline four. Knowing that up front is the difference between a repair that holds and one you are back for in a month."]),
  ("Tires, brakes, and the stuff that stops you",
   ["Tire mount and balance, brake fluid flush, pads and rotors, and the honest conversation about a tire that looks fine on tread but is five years old and dry-rotting in the Florida sun. Down here, heat and ozone age rubber faster than miles do, so a tire can have tread and still be unsafe. Brakes and tires are not where you save money. They are where you spend it on purpose.",
    "Florida&rsquo;s flat, straight roads also square off the center of a tire while the shoulders keep tread, which makes a bike resist leaning and then fall into a turn. If your bike feels like it fights you into corners, that is often the tire, not you."]),
  ("Recalls and known faults",
   ["A lot of what strands riders is already documented. Fuel-pump recalls, transmission and electrical campaigns, brake and fuel-system bulletins &mdash; the manufacturers have written them down, and the parts and labor are usually covered. We diagnose recall-related symptoms, point you to the official fix, and handle the work. Our Tech&rsquo;s Ledger breaks down the verified ones by model so you can check your bike before you call.",
    "The point is to catch the problem while it is still a scheduled repair. A fault on a bike in this climate ages on a fast clock &mdash; heat soak, humidity and salt air push it harder every ride &mdash; so the window between a cheap fix and an expensive one is shorter here than almost anywhere."]),]},
{"slug":"custom-builds-south-florida","service":"Motorcycle Customization","order":2,
 "metatitle":"Motorcycle Customization South Florida | Harley &amp; European Builds | HiTECH Miramar",
 "desc":"Motorcycle customization in Miramar for Harley-Davidson, V-twins and European bikes: bags, bars, stance, lighting, wiring and fitment done right. Serving Miami, Fort Lauderdale and South Florida.",
 "kw":"motorcycle customization south florida, harley custom builds miramar, custom bagger south florida, european motorcycle custom, motorcycle wiring and lighting, ape hangers bars installation, motorcycle stance suspension, custom motorcycle shop miami",
 "kicker":"Customization","h1":"Harley &amp; European Custom Builds in South Florida",
 "lede":"Bags, bars, stance, lighting, wiring and the fitment details that separate a real build from a parts-bin bike. We customize Harley-Davidson and American V-twins alongside European machines &mdash; Miramar-based, serving Miami, Fort Lauderdale and all of South Florida.",
 "vids":["k9_scg88oqQ","TdJlFX8Us2w"],
 "sec":[("Custom with taste and discipline",
   ["A good build has stance, proportion, sound, restraint, and a reason to exist. A bad one has mystery wires, poor fitment, rubbing parts, weak brakes, and a photo angle doing too much work. We build the first kind. Whether it is a bagger that has to swallow long-distance miles on US-27 or a stripped European bike with a clean cockpit, the rule is the same: make it beautiful, then make it work.",
    "That means we sweat the parts you do not see. Wiring routed and loomed so it survives Florida heat and vibration, fasteners torqued to spec, fender and tire clearance checked under full compression, and brakes and lighting that stay safe no matter what the build looks like. Style is never an excuse for a bike that is dangerous to ride."]),
  ("Harley &amp; V-twin builds",
   ["Baggers and cruisers are a lifestyle down here, and they get ridden hard in heat and traffic. We handle bars and risers, bag and fender work, stance and suspension, audio and lighting, exhaust, and the charging upgrades a loaded touring bike actually needs when you add stereo, lights and accessories that all pull current.",
    "We also fix the builds other shops rushed: the ape hangers with brake lines stretched to the limit, the stereo wired into a circuit that cannot carry it, the lowering job that now drags hard parts in every driveway. If your bike looks the part but fights you on the road, we make it ride as good as it looks."]),
  ("European &amp; metric customization",
   ["European bikes reward a lighter, more precise hand &mdash; cockpit and controls, lighting and plate relocation, suspension setup, tasteful exhaust, and the electronics work these platforms demand. Ducati, BMW, Triumph and the metric sport bikes all hate sloppy wiring and low voltage, so clean electrical work is not optional on these builds, it is the whole job.",
    "We keep the character of the machine while sharpening it. The goal is a bike that still feels like what the factory intended, only tighter, cleaner and yours &mdash; not a European bike buried under parts that fight its design."]),
  ("Fitment, wiring and the safety side",
   ["Customization lives or dies on fitment and wiring. We check clearance under load, not just on the stand, so nothing rubs when the suspension compresses or the bars turn lock to lock. Electrical gets proper connectors, fusing and grounds, because a melted connector or a lazy ground is how a beautiful build leaves you on the shoulder at night.",
    "Before any build leaves, it gets the same once-over we give a repair: brakes bled firm, lighting verified front and rear, charging checked under load, and a road test. A custom bike should turn heads in the lot and still be the safest bike on the ride."]),]},
{"slug":"harley-davidson-service-repair","service":"Harley-Davidson Service","order":3,
 "metatitle":"Independent Harley-Davidson Mechanic Miramar | V-Twin vs Sport Bike | HiTECH",
 "desc":"Independent Harley-Davidson and American V-twin service in Miramar, serving Broward and Miami-Dade. Primary, compensator, stator, belt and charging work &mdash; without dealership rates.",
 "kw":"independent harley davidson mechanic miramar, harley repair south florida, american v-twin service, harley stator charging, drive belt tension, sport bike vs metric service south florida, harley primary compensator",
 "kicker":"American V-Twin &amp; Metric","h1":"Independent Harley-Davidson &amp; V-Twin Service vs. Sport Bike &amp; Metric",
 "lede":"Two very different machines, two very different failure patterns, one shop that knows both. Independent Harley-Davidson and American V-twin work alongside sport bike and metric service &mdash; Miramar-based, serving Broward and Miami-Dade without dealership rates.",
 "vids":["TdJlFX8Us2w","k9_scg88oqQ"],
 "sec":[("The V-twin: vibration, heat, and charging",
   ["A Harley lives with vibration as a design trait, and vibration is what loosens, chafes and fatigues things over the miles. On a V-twin we check the primary fluid first &mdash; milky means condensation, flush it &mdash; and we listen for compensator slap on a cold start. The stator plug near the lower front crankcase is a known grime-and-moisture trap that burns pins and kills charging, so it gets inspected before anyone blames the battery.",
    "Drive belt tension and condition matter more here than riders think. South Florida limestone sand and road debris pit and fray rubber belts; we inspect every inch before you load tour bags for a long weekend. A belt that fails at speed is not a roadside fix, so it is worth the five minutes on the lift."]),
  ("The sport bike and metric side",
   ["Different architecture, different vulnerabilities. Salt air and road grime pit chrome fork stanchions, and pitted chrome slices fork seals that then spray oil onto your front brakes. A chain left un-lubed after soaked summer rides rusts, robs power and risks snapping at highway rpm. Radiators cake with bugs and grime, and these bikes run hot by design, so the fans had better engage before you sit in A1A beach traffic.",
    "We service Yamaha, Suzuki, Kawasaki and Honda sport bikes with the same discipline we bring to the V-twins &mdash; and the dyno is in-house when you want the metric bike to actually make its power instead of guessing at a map."]),
  ("Why independent, and when to use the dealer",
   ["Dealership rates make sense for warranty work and for recalls, which are usually covered. For everything else &mdash; maintenance, performance, the out-of-warranty repair &mdash; an independent shop that knows the platform gives you the same quality without the markup. We will tell you honestly when a job belongs at the dealer and when it belongs on our lift.",
    "That honesty is the whole value of an independent. You are not a warranty number here; you are a rider with a bike and a budget, and we treat the repair that way."]),
  ("Seasonal prep for both",
   ["Down here the calendar matters. A bike that sat under a cover through monsoon season &mdash; Harley or sport bike &mdash; is not ready for a long run just because it starts. Fuel systems take on water through ethanol, batteries that cranked all summer quit the first cold morning, brake fluid saturates and fades, and tires square off and dry-rot in the sun.",
    "We run a pre-season inspection on both platforms: fuel system and pressure, brake fluid moisture, charging output, suspension and fork seals, and chain or belt. Forty-five minutes on the bench buys you the whole riding season without a tow."]),]},
{"slug":"dyno-tuning-south-florida","service":"Motorcycle Dyno Tuning","order":4,
 "metatitle":"Motorcycle Dyno Tuning South Florida | ECU Flashing Miami | HiTECH",
 "desc":"In-house motorcycle dyno tuning and ECU flashing in Miramar, serving Miami, Fort Lauderdale and Broward. Sport bikes, V-twins and metric. Tap to message the mechanic.",
 "kw":"motorcycle dyno tuning south florida, dyno tune motorcycle miami, ecu flashing motorcycle near me, sport bike performance shop south florida, custom motorcycle exhaust installation near me, motorcycle tuner miramar, harley dyno tune",
 "kicker":"Dyno &amp; Performance","h1":"Motorcycle Dyno Tuning &amp; ECU Flashing in South Florida",
 "lede":"A mod without a tune is not performance &mdash; it is imbalance. We put your bike on the dyno, read what it is actually doing, and dial the fuel and timing to match the hardware. Miramar-based, serving Miami, Fort Lauderdale and all of Broward and Miami-Dade.",
 "vids":["smVENbJfOvc"],   # Kawasaki clip is a fuel-pump job - it lives in Issue 02, not the dyno page
 "sec":[("Why a dyno tune, and why now",
   ["You bolted on an exhaust, a filter, a full system, maybe a different sprocket. The bike feels different, but different is not the same as right. The stock map was written for stock airflow, and the moment you change how the engine breathes, the fueling is guessing. On the dyno we stop guessing: we measure air-fuel ratio under load, across the whole rpm range, and build a map that matches the parts actually on the bike.",
    "This is the single highest-value thing you can do to a modified bike, and it is the thing most riders skip because the bike still runs. It runs lean in the spots that cook pistons and rich in the spots that foul plugs and dump fuel economy. A proper tune cleans both up, and you feel it everywhere &mdash; smoother roll-on, cleaner throttle, no surging at cruise, and real, measured power instead of a number off a forum."]),
  ("What we actually do on the dyno",
   ["Every tune starts with a baseline pull so we can see where the bike is, not where we assume it is. From there we log air-fuel across the range, check for knock, confirm the sensors are honest, and build the map in passes until the curve is clean and the ratios are safe under load. You leave with a printout and a bike that pulls the way the hardware promised.",
    "We tune sport bikes, V-twins and metric cruisers, and we handle ECU flashing on the platforms that support it. If your bike needs a piggyback or a standalone instead, we will tell you that up front rather than sell you the wrong path. A tune is only as good as the plan behind it."]),
  ("Exhaust, intake, and the rest of the package",
   ["Dyno time pairs with the hardware. Full exhaust installation, intake work, sprocket and gearing changes, and the carburetor cleaning and restoration that older bikes need before they will hold a tune at all. A clogged pilot circuit or a tired fuel pump will fight any map, so we sort the mechanical side first and tune second.",
    "That order matters. Tuning around a problem buries it; fixing it first and tuning after gives you a number that holds. We would rather spend an hour making the bike healthy than sell you a map it cannot keep."]),
  ("Harley and V-twin tuning",
   ["V-twins respond to tuning as much as any sport bike, and in this heat they need it. A rich, hot-running big twin stuck in Miami traffic makes life miserable &mdash; the tune cleans up the fueling, drops the heat, and wakes up the midrange where a cruiser actually lives. Pair it with the right exhaust and intake and the bike feels like a different machine.",
    "We dyno Harleys and American V-twins the same careful way: baseline, log, build, verify under load. No canned maps, no guessing &mdash; your bike, your hardware, your numbers on paper."]),]},
{"slug":"sport-bike-maintenance-dyno","service":"Sport Bike Maintenance","order":5,
 "metatitle":"Sport Bike Maintenance &amp; Dyno South Florida | GSX-R R1 ZX | HiTECH",
 "desc":"Sport bike maintenance and dyno tuning in Miramar for Suzuki GSX-R, Yamaha R1/R6, Kawasaki ZX and Honda CBR. Fork seals, chains, cooling, ECU work. Serving Miami and Fort Lauderdale.",
 "kw":"sport bike maintenance south florida, yamaha kawasaki sport bike mechanic near me, suzuki gsxr specialist south florida, r1 r6 service, zx-10r service, fork seal replacement, sport bike dyno tune miami, honda cbr service",
 "kicker":"Sport Bikes","h1":"Sport Bike Maintenance &amp; Dyno Tuning in South Florida",
 "lede":"GSX-R, R1, R6, ZX, CBR &mdash; precision machines that punish neglect fast. Fork seals, chains, cooling, brakes and the dyno work that makes the mods real. Miramar-based, serving Miami, Fort Lauderdale and all of Broward.",
 "vids":["smVENbJfOvc","P54eoe9m_Lk"],
 "sec":[("Maintenance a sport bike actually needs",
   ["A sport bike rewards precision and punishes neglect faster than any other machine. Chain slack and O-ring integrity, fork seals and stanchion condition, coolant and fan operation, brake fluid and pad life, steering head bearings &mdash; these are the items that decide whether the bike feels sharp or nervous at speed. Miss them and the first warning you get is mid-corner.",
    "We set these bikes up properly: chain and sprockets, suspension sag and seals, cooling system verified under heat, and brakes bled to a firm lever. Then the bike does what the spec sheet promised instead of fighting you into the apex."]),
  ("The dyno is where the mods become real",
   ["Exhaust, intake, sprockets, a full tune &mdash; on the dyno we measure air-fuel under load and build a map that matches the hardware. A performance mod without a tune is imbalance, not performance. For Suzuki GSX-R, Yamaha R1 and R6, Kawasaki ZX and Honda CBR, this is the step that turns parts into power you can feel and verify on a printout.",
    "We also catch the high-rpm problems that only show under load: a tired fuel filter, worn plugs, an intake leak, a map that falls flat up top. The dyno finds them; the bench fixes them. You do not want to discover a lean spot at redline on the street."]),
  ("Known faults, handled",
   ["Several of these platforms carry documented recalls and bulletins &mdash; R1 transmission and headlight campaigns, R6 wheel and shift issues, ZX oil-pressure and spark-plug recalls, GSX-R brake and fuel items. Our Tech&rsquo;s Ledger breaks each one down by model, and we handle the diagnosis and the official fix.",
    "Checking your VIN against the campaign before a problem strands you is free and fast. Bring us the bike and we will tell you where it stands."]),
  ("Florida heat and the sport bike",
   ["These bikes run hot by design, and South Florida does not help. Radiators cake with bugs and grime, fans have to engage on time, and coolant that has not been changed loses its ability to move heat. Sitting in beach traffic on A1A is exactly the condition that exposes a tired cooling system.",
    "Salt air also pits fork chrome, which then kills seals and drops oil onto your brakes, and a chain left un-lubed after wet rides rusts stiff. Our maintenance targets the stuff this climate attacks first, so the bike stays sharp through the whole riding season."]),]},
{"slug":"crash-estimates-salvage-inspection","service":"Motorcycle Crash Estimates","order":6,
 "metatitle":"Motorcycle Crash Estimate Near Me | Collision &amp; Frame Inspection | HiTECH",
 "desc":"Motorcycle crash estimates, collision repair and frame/fork inspection in Miramar, serving Miami, Fort Lauderdale and South Florida. Insurance and pre-purchase salvage inspections.",
 "kw":"motorcycle crash estimate near me, motorcycle collision repair south florida, motorcycle frame and fork inspection south florida, salvage motorcycle inspection, insurance motorcycle estimate miami, rebuilt title inspection",
 "kicker":"Crash &amp; Inspection","h1":"Motorcycle Crash Estimates, Collision Repair &amp; Frame Inspection",
 "lede":"Down the bike, buying a salvage title, or dealing with an insurer? We write honest crash estimates and inspect frame, forks and driveline the way it needs to be inspected &mdash; Miramar-based, serving Miami, Fort Lauderdale and South Florida.",
 "vids":["i4m64buhuKA"],
 "sec":[("The estimate, done straight",
   ["After a crash the damage you see is rarely the whole story. Bent forks, a tweaked frame, cracked or bent subframe, damaged mounts, driveline damage &mdash; a lot of it hides until someone measures it. We write an estimate that documents all of it, so whether you are working with an insurer or deciding if the bike is worth saving, you are working from the truth and not a guess.",
    "We photograph, measure, and list parts and labor clearly. If the bike is totaled on the numbers, we will tell you. If it is a straightforward rebuild, we will tell you that too, and what it will actually cost to make it safe again."]),
  ("Frame and fork inspection",
   ["This is the inspection that decides whether a bike is safe to ride again. Forks for straightness and seal condition, frame for alignment and cracks, steering head and wheel bearings, and the driveline for the damage an impact sends downstream. A bike that looks fine in photos can be geometrically wrong in a way you feel the first time you lean it.",
    "It is also the inspection to get before you buy a salvage-title bike. Pay for the inspection before you pay for the bike, not after &mdash; a cheap salvage with a bent frame is not cheap, it is a project you did not sign up for."]),
  ("Insurance and salvage work",
   ["We handle insurance estimates and the pre-purchase inspection on salvage and rebuilt titles. Bring us the bike, the paperwork, and what you are trying to decide, and we will give you the honest mechanical picture so the decision is yours to make with real information.",
    "No pressure either way. Some salvage bikes are a smart buy and some are a trap, and the only way to know is to measure. That is what we do."]),
  ("Getting back on the road safely",
   ["If the bike is worth fixing, we rebuild it right: straightened or replaced chassis parts, correct forks, proper alignment, and the full safety pass before it goes back out &mdash; brakes, lighting, charging and a road test. A repaired crash bike should ride like nothing happened, not like a bike you have to baby.",
    "And if you are not sure whether to repair, part it out, or walk away, that is a conversation we are glad to have before you spend a dollar."]),]},
]
PAGES.sort(key=lambda p:p["order"])

def render(p):
    body=[]
    allsecs=list(p["sec"])
    for i,(h2,paras) in enumerate(allsecs):
        body.append("<h2>%s</h2>"%h2)
        for para in paras: body.append("<p>%s</p>"%para)
        if i < len(p["vids"]):
            body.append(T.yt_embed(p["vids"][i], "HiTECH Motorcycle %s"%re.sub('&[a-z]+;','',p['service'])))
    # shared closing
    body.append("<h2>%s</h2>"%CLOSING[0])
    body.append("<p>%s</p>"%CLOSING[2])
    # unique per-page booking paragraph (built from this page's own keyword + service)
    kw1=p["kw"].split(",")[0].strip()
    svc_plain=re.sub('&amp;','and',p["service"])
    body.append("<h2>Book your %s in South Florida</h2>"%svc_plain.lower())
    body.append(("<p>If you have been searching for %s, or a %s shop near you in Miami, Miami Beach, Fort Lauderdale, "
        "Weston, Hollywood or Pembroke Pines, that is exactly what we do. HiTECH is an independent %s shop in Miramar, "
        "rated %s from %s Google reviews, and we handle this work day in and day out for riders across Broward and "
        "Miami-Dade. Tap Message the Mechanic with your year, make, model and mileage, or call the shop during "
        "Tuesday-to-Saturday hours, and we will get you scheduled and back on the road.</p>") % (
        kw1, svc_plain.lower(), svc_plain.lower(), T.RATING, T.REVIEW_COUNT))
    bodyhtml="\n".join(body)
    svc={"@context":"https://schema.org","@type":"Service","name":re.sub('&amp;','&',p["service"]),"serviceType":re.sub('&amp;','&',p["service"]),
        "areaServed":T.CITIES,"provider":{"@type":["MotorcycleRepair","AutoRepair"],"name":T.GBP_NAME,"telephone":T.TEL,"url":T.SITE,
        "address":{"@type":"PostalAddress","streetAddress":T.ADDR_STREET,"addressLocality":"Miramar","addressRegion":"FL","postalCode":"33023","addressCountry":"US"},
        "aggregateRating":{"@type":"AggregateRating","ratingValue":T.RATING,"reviewCount":T.REVIEW_COUNT,"bestRating":"5"}},
        "url":"%s/%s.html"%(T.SITE,p["slug"])}
    out="""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="keywords" content="%s, Miramar, Miami, Fort Lauderdale, Hollywood, Pembroke Pines, Weston, Broward, South Florida">
<meta name="robots" content="index, follow, max-image-preview:large"><meta name="theme-color" content="#090A0D">
<meta name="geo.region" content="US-FL"><meta name="geo.placename" content="Miramar, Miami, Fort Lauderdale"><meta name="geo.position" content="25.9876;-80.2098">
<link rel="canonical" href="%s/%s.html">
<meta property="og:type" content="website"><meta property="og:title" content="%s"><meta property="og:description" content="%s"><meta property="og:url" content="%s/%s.html"><meta property="og:image" content="%s/assets/images/name.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="%s"><meta name="twitter:description" content="%s">
%s
<script type="application/ld+json">%s</script>
<style>%s</style></head><body>
%s
<main class="wrap">
<nav class="crumbs"><a href="index.html">HITECH</a> / %s</nav>
<div class="lede-grid">
<div>
<p class="kicker">%s</p>
<h1>%s</h1>
<p class="deck">%s</p>
<div class="tools">%s<a class="button button-ghost" href="ledger/index.html">Tech&rsquo;s Ledger</a></div>
<article class="body">
%s
<div class="cta-block"><h3>Ready when you are.</h3>
<p>Tap to message the mechanic, or stop by the Miramar shop Tuesday to Saturday, 9 to 6. Serving Miami, Fort Lauderdale, Weston and all of South Florida.</p>
<div class="cta-actions">%s<a class="button button-ghost" href="%s">Follow on IG</a><a class="button button-ghost" href="%s">YouTube</a></div></div>
</article>
</div>
<aside class="rail">%s
<div class="card"><h4>Talk to the mechanic</h4><p style="margin:0 0 10px">Year, make, model, mileage, and what you need. A clip beats a paragraph.</p>%s</div>
%s</aside>
</div>
</main>
%s
</body></html>""" % (
      p["metatitle"], p["desc"], p["kw"], T.SITE, p["slug"], p["metatitle"], p["desc"], T.SITE, p["slug"], T.SITE,
      p["metatitle"], p["desc"], T.PIXELS, json.dumps(svc), T.CSS(), header(),
      re.sub('&amp;','&',p["service"]), p["kicker"], p["h1"], p["lede"], T.msg_button("Message the Mechanic"),
      bodyhtml, T.msg_button("Message the Mechanic"), T.IG, T.YT,
      T.reviews_widget(), T.msg_button("Message the Mechanic"), T.subscribe_form("Join Bike Culture","Send"), footer())
    return out

for p in PAGES:
    out=render(p)
    with open(os.path.join(HERE, p["slug"]+".html"), "w", encoding="utf-8") as f:
        f.write(out)
    words=len(re.sub('<[^>]+>',' ',re.search(r'<article class="body">(.*)</article>',out,re.S).group(1)).split())
    print(p["slug"], words, "words")
