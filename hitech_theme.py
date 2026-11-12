# -*- coding: utf-8 -*-
"""Shared theme + components for HITECH Motorcycle. Racing palette, legible headers,
tap-to-message, real brand logos, Google reviews, mobile sticky bar, AEO pixels."""

SITE = "https://hitech00bike.com"
PHONE = "954.793.6390"; TEL = "+19547936390"; WA = "https://wa.me/19547936390"
GBP_NAME = "Hi Tech Motorsports"            # matches Google Business Profile
ADDR = "3056 S State Rd 7 Ste 78, Miramar, FL 33023"
ADDR_STREET = "3056 S State Rd 7 Ste 78"
IG = "https://www.instagram.com/hi_tech_motorcycles"
YT = "https://www.youtube.com/@hitech00BIKE"
EMAIL = "ops@hitech00bike.com"
OPS_EMAIL = "ops@hitech00bike.com"
SUBMIT_URL = "https://submit-zuirpy7nza-uc.a.run.app"
RATING = "4.9"; REVIEW_COUNT = "97"
GOOGLE_REVIEWS = "https://www.google.com/maps/search/?api=1&query=Hi+Tech+Motorsports+3056+S+State+Rd+7+Miramar+FL+33023"

CITIES = ["Miramar","Miami","Miami Beach","Weston","Fort Lauderdale","Hollywood",
          "Pembroke Pines","Davie","Plantation","Sunrise","Aventura","Hialeah",
          "Broward County","Miami-Dade","South Florida"]

# Real brand logo files that exist in assets/logos (filename, alt)
LOGOS = [("honda.svg","Honda"),("yamaha.jpg","Yamaha"),("Kawasaki.jpg","Kawasaki"),
         ("suzuki.png","Suzuki"),("Ducati.png","Ducati"),("hd.jpg","Harley-Davidson"),
         ("motorrad.png","BMW Motorrad")]

PARTNERS = [
    ("RealFi Model", "https://www.realfimodel.com"),
    ("Dividond", "https://www.dividond.com"),
    ("Coffee Bar Roasters", "https://www.coffeebarroasters.com"),
]

# Brand / topic -> YouTube id (shorts and normal both embed at /embed/<id>)
YT_VIDEOS = {
    "Suzuki":"P54eoe9m_Lk", "Yamaha":"smVENbJfOvc", "Kawasaki":"gOxCroShxfA",
    "Harley-Davidson":"k9_scg88oqQ", "cruiser":"TdJlFX8Us2w",
    "valve":"i4m64buhuKA", "oil":"MVhGRyn4E8A",
}
def yt_for(brand, category=""):
    if brand in YT_VIDEOS: return YT_VIDEOS[brand]
    c = (category or "").lower()
    if "valve" in c or "engine" in c: return YT_VIDEOS["valve"]
    if "lubric" in c or "oil" in c: return YT_VIDEOS["oil"]
    if brand in ("Aprilia","MV Agusta","Ducati"): return YT_VIDEOS["cruiser"]
    return YT_VIDEOS["oil"]

def yt_embed(vid, title="HITECH Motorcycle video"):
    return ('<div class="ytwrap"><iframe loading="lazy" src="https://www.youtube-nocookie.com/embed/%s?rel=0" '
            'title="%s" frameborder="0" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" '
            'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>') % (vid, title)

# Ordered shop videos for the rotating player (id, label)
SHOP_VIDEOS = [("TdJlFX8Us2w","Cruiser build"),("k9_scg88oqQ","Harley short"),
               ("smVENbJfOvc","Yamaha service"),("gOxCroShxfA","Kawasaki service"),
               ("P54eoe9m_Lk","Suzuki service"),("i4m64buhuKA","Valve service"),
               ("MVhGRyn4E8A","Oil service")]
def video_rotator():
    first = SHOP_VIDEOS[0][0]
    thumbs = "".join(
        '<button type="button" class="vthumb%s" data-id="%s" onclick="pickVid(this)">'
        '<img loading="lazy" src="https://i.ytimg.com/vi/%s/mqdefault.jpg" alt="%s"><span>%s</span></button>'
        % (" on" if i == 0 else "", vid, vid, lbl, lbl) for i, (vid, lbl) in enumerate(SHOP_VIDEOS))
    return ('<div class="vrotor">'
            '<div class="ytwrap vrotor-main"><iframe id="vrotorFrame" loading="lazy" '
            'src="https://www.youtube-nocookie.com/embed/%s?rel=0" title="HITECH Motorcycle shop video" '
            'frameborder="0" allow="accelerometer;autoplay;clipboard-write;encrypted-media;gyroscope;picture-in-picture" '
            'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'
            '<div class="vrotor-strip">%s</div></div>') % (first, thumbs)

PIXELS = """<!-- ANALYTICS / PIXELS - paste IDs, then uncomment -->
<!-- Google tag (gtag.js) - replace G-XXXXXXXXXX
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
gtag('js',new Date());gtag('config','G-XXXXXXXXXX');</script>
-->
<!-- Meta (Facebook) Pixel - replace YOUR_PIXEL_ID
<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,
'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','YOUR_PIXEL_ID');fbq('track','PageView');</script>
-->"""

JS = """<script>
function toggleMsg(btn){var w=btn.closest('.msg');if(w)w.classList.toggle('open');}
function subForm(e){e.preventDefault();var f=e.target;
if(f._company && f._company.value){return false;}            /* honeypot: bots fill this, humans never see it */
var ok=f.querySelector('.sub-ok'),btn=f.querySelector('button[type=submit]');
var data={name:(f.name.value||''),email:(f.email.value||''),bike:(f.bike.value||''),
message:(f.message?f.message.value:''),source:location.hostname,page:location.pathname,form:'hitech-website'};
if(btn){btn.disabled=true;btn.dataset.t=btn.textContent;btn.textContent='Sending...';}
fetch('__SUBMIT_URL__',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)})
.then(function(r){if(!r.ok)throw r.status;return r.text();})
.then(function(){f.reset();if(ok){ok.textContent='Thanks \\u2014 we got it. We will be in touch.';ok.style.display='block';}
if(btn){btn.disabled=false;btn.textContent=btn.dataset.t||'Send';}})
.catch(function(){if(ok){ok.textContent='Could not send \\u2014 text us at %(phone)s.';ok.style.display='block';}
if(btn){btn.disabled=false;btn.textContent=btn.dataset.t||'Send';}});
return false;}
var VRthumbs=document.querySelectorAll('.vthumb');var vIdx=0,vAuto=true;
function vLoad(id,play){var fr=document.getElementById('vrotorFrame');if(fr)fr.src='https://www.youtube-nocookie.com/embed/'+id+'?rel=0'+(play?'&autoplay=1':'');}
function pickVid(btn){vAuto=false;VRthumbs.forEach(function(b){b.classList.remove('on');});btn.classList.add('on');vLoad(btn.dataset.id,true);}
if(VRthumbs.length>1){setInterval(function(){if(!vAuto)return;vIdx=(vIdx+1)%%VRthumbs.length;VRthumbs.forEach(function(b){b.classList.remove('on');});VRthumbs[vIdx].classList.add('on');vLoad(VRthumbs[vIdx].dataset.id,false);},9000);}
(function(){var cards=document.querySelectorAll('.rev-card');if(cards.length<2)return;var i=0;
setInterval(function(){cards[i].classList.remove('on');i=(i+1)%%cards.length;cards[i].classList.add('on');},4200);})();
</script>""".replace("__SUBMIT_URL__", SUBMIT_URL) % {"phone": PHONE}

def msg_button(label="Message the Mechanic", big=True, ghost=False):
    cls = "button " + ("button-ghost" if ghost else "button-red")
    return ('<span class="msg"><button type="button" class="%s msg-toggle" onclick="toggleMsg(this)">%s</button>'
            '<span class="msg-actions"><a class="button button-red" href="%s">WhatsApp</a>'
            '<a class="button button-dark" href="sms:%s">Text</a>'
            '<a class="button button-ghost" href="tel:%s">Call</a></span></span>') % (cls, label, WA, TEL, TEL)

def logo_band(root=""):
    one = "".join('<span class="lchip"><img src="%sassets/logos/%s" alt="%s motorcycle service" loading="lazy"></span>' % (root, f, alt) for f, alt in LOGOS)
    return '<div class="logo-band" aria-label="Brands we service"><div class="logo-wrap"><div class="logo-track">%s%s</div></div></div>' % (one, one)

def partner_rail():
    items = "".join('<a href="%s" target="_blank" rel="sponsored noopener"><b>%s</b><span>Partner &rarr;</span></a>' % (u, n) for n, u in PARTNERS)
    return '<div class="card aff"><h4>Partners</h4>%s</div>' % items

def follow_card():
    return ('<div class="card aff"><h4>Follow</h4>'
            '<a href="%s" target="_blank" rel="me noopener"><b>Instagram</b><span>@hi_tech_motorcycles &rarr;</span></a>'
            '<a href="%s" target="_blank" rel="me noopener"><b>YouTube</b><span>@hitech00BIKE &rarr;</span></a>'
            '</div>') % (IG, YT)

# Rotating Google-reviews widget. Aggregate rating is real (user-supplied).
# Highlight lines are the shop's own framing, not fabricated customer quotes.
REVIEW_HIGHLIGHTS = [
    "Independent Ducati, Harley &amp; sport-bike specialists.",
    "In-house dyno tuning and ECU work.",
    "Straight diagnosis, no guesswork, no parts cannon.",
    "Trusted across Broward &amp; Miami-Dade.",
    "Factory-level repairs without dealership rates.",
]
def reviews_widget():
    cards = "".join('<div class="rev-card%s">%s</div>' % (" on" if i == 0 else "", h) for i, h in enumerate(REVIEW_HIGHLIGHTS))
    return ('<div class="card rev"><h4>Google Reviews</h4>'
            '<div class="rev-score"><span class="rev-num">%s</span><span class="rev-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'
            '<span class="rev-count">%s reviews</span></div>'
            '<div class="rev-rot">%s</div>'
            '<a class="button button-dark" style="width:100%%" href="%s" target="_blank" rel="noopener">Read them on Google</a>'
            '</div>') % (RATING, REVIEW_COUNT, cards, GOOGLE_REVIEWS)

def mobile_bar():
    return ('<div class="mbar"><a class="mbar-call" href="tel:%s">&#128222; Call</a>'
            '<a class="mbar-text" href="sms:%s">&#128172; Text</a>'
            '<a class="mbar-wa" href="%s">WhatsApp</a></div>') % (TEL, TEL, WA)

def subscribe_form(title="Get the next Issue", btn="Subscribe", msg=True):
    m = '<textarea name="message" rows="2" placeholder="What is going on with your bike? (optional)"></textarea>' if msg else ''
    return ('<div class="card subcard"><h4>%s</h4>'
            '<form onsubmit="return subForm(event)">'
            '<input type="text" name="_company" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">'
            '<input name="name" placeholder="Your name" autocomplete="name">'
            '<input name="email" type="email" placeholder="Email" autocomplete="email" required>'
            '<input name="bike" placeholder="Your bike (year / make / model)">'
            '%s'
            '<button class="button button-red" type="submit">%s</button>'
            '<span class="sub-ok"></span></form></div>') % (title, m, btn)

def CSS():
    return """
:root{
 --white:#F5F7FA;--blue:#0057B8;--blue2:#2f86e6;--red:#E30613;--black:#090A0D;
 --silver:#BFC3C8;--panel:#12141B;--panel2:#171A22;--line:rgba(191,195,200,.18);
 --max:1240px;--shadow:0 24px 70px rgba(0,0,0,.55)
}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--black);color:var(--white);font-family:Inter,'Segoe UI',Arial,sans-serif;line-height:1.6;overflow-x:hidden}
body:before{content:"";position:fixed;inset:0;pointer-events:none;z-index:-1;background:
 radial-gradient(circle at 16% -4%,rgba(227,6,19,.20),transparent 34%),
 radial-gradient(circle at 86% 8%,rgba(0,87,184,.24),transparent 38%),
 linear-gradient(90deg,rgba(191,195,200,.04) 1px,transparent 1px);background-size:auto,auto,46px 46px}
a{color:inherit;text-decoration:none}img,video,iframe{max-width:100%;display:block}
.display{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;text-transform:uppercase;letter-spacing:.01em;line-height:1.04}
.button{display:inline-flex;align-items:center;justify-content:center;gap:8px;border:0;border-radius:8px;padding:12px 18px;font-weight:800;text-transform:uppercase;letter-spacing:.04em;font-size:13px;cursor:pointer;line-height:1}
.button-red{background:var(--red);color:#fff;box-shadow:0 10px 26px rgba(227,6,19,.30)}
.button-blue{background:var(--blue);color:#fff}
.button-dark{background:var(--white);color:var(--black)}
.button-ghost{border:1px solid var(--silver);color:var(--white);background:rgba(245,247,250,.06)}
.button:hover{filter:brightness(1.08)}
.msg{display:inline-flex;flex-wrap:wrap;gap:8px;align-items:center}
.msg-actions{display:none;gap:8px;flex-wrap:wrap}
.msg.open .msg-actions{display:inline-flex}
.msg.open .msg-toggle{background:var(--blue)}
.site-header{position:sticky;top:0;z-index:40;display:grid;grid-template-columns:auto 1fr auto;gap:16px;align-items:center;padding:9px clamp(14px,3.5vw,38px);background:rgba(9,10,13,.93);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.brandlogo{display:flex;align-items:center;gap:10px}
.brandlogo img{height:30px;width:auto;background:#fff;padding:5px 9px;border-radius:7px;box-shadow:0 2px 10px rgba(0,0,0,.4)}
.brand{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;font-size:clamp(18px,2.2vw,26px);letter-spacing:.01em;text-transform:uppercase}.brand span{color:var(--red)}
.nav-links{display:flex;gap:6px;justify-content:center;flex-wrap:wrap}
.nav-links a{border:1px solid var(--line);border-radius:6px;padding:7px 10px;color:var(--silver);font-size:12px;text-transform:uppercase;letter-spacing:.05em;font-weight:600}
.nav-links a:hover{border-color:var(--red);color:#fff;background:rgba(227,6,19,.14)}
.header-actions{display:flex;gap:8px}
.logo-band{border-block:1px solid var(--line);background:linear-gradient(90deg,#0d0f14,#111520)}
.logo-wrap{max-width:var(--max);margin:0 auto;overflow:hidden;position:relative;-webkit-mask:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask:linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent)}
.logo-track{display:flex;gap:16px;align-items:center;width:max-content;animation:scrollx 30s linear infinite;padding:10px 0}
.lchip{background:#fff;border-radius:8px;height:46px;min-width:92px;display:flex;align-items:center;justify-content:center;padding:6px 12px}
.lchip img{height:32px;width:auto;object-fit:contain}
@keyframes scrollx{from{transform:translateX(0)}to{transform:translateX(-50%)}}
main{position:relative}
.hero{max-width:var(--max);margin:0 auto;padding:36px clamp(14px,3.5vw,38px) 20px;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(300px,.8fr);gap:20px;align-items:stretch}
.hero-copy{position:relative;padding:clamp(22px,4vw,44px);background:linear-gradient(135deg,rgba(0,87,184,.16),rgba(245,247,250,.04));border:1px solid var(--line);box-shadow:var(--shadow);border-radius:14px;overflow:hidden}
.eyebrow{margin:0 0 10px;color:var(--blue2);font-weight:800;text-transform:uppercase;letter-spacing:.14em;font-size:12px}
.issue-tag{display:inline-flex;gap:8px;align-items:center;border:1px solid rgba(227,6,19,.5);background:rgba(227,6,19,.12);padding:7px 12px;border-radius:999px;color:#ffb3b8;font-size:12px;text-transform:uppercase;letter-spacing:.07em;font-weight:700}
.hero h1{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;margin:16px 0 12px;font-size:clamp(32px,5vw,60px);line-height:1.0;letter-spacing:.01em;text-transform:uppercase}
.hero h1 em{font-style:normal;color:var(--red)}
.hero-lede{max-width:600px;color:var(--silver);font-size:clamp(15px,1.6vw,18px);line-height:1.6}
.hero-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:20px}
.cover-lines{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:26px}
.cover-lines div{border-top:3px solid var(--red);padding-top:9px;color:var(--silver);font-size:12px}
.cover-lines strong{display:block;color:#fff;font-size:14px;text-transform:uppercase;letter-spacing:.02em;font-family:'Arial Narrow',Impact,sans-serif}
.hero-rail{display:grid;grid-template-rows:auto auto;gap:12px;align-content:start}
.video-card{position:relative;aspect-ratio:16/9;border:1px solid var(--line);background:#000;overflow:hidden;box-shadow:var(--shadow);border-radius:14px}
.video-card video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.video-card:before{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 42%,rgba(9,10,13,.86));z-index:1}
.video-cap{position:absolute;left:16px;right:16px;bottom:14px;z-index:2}
.video-cap h2{margin:0;font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;font-size:22px;text-transform:uppercase;line-height:1.05;letter-spacing:.01em}
.video-cap p{color:var(--silver);margin:6px 0 0;font-size:13px}
.contact-card{border:1px solid var(--line);background:linear-gradient(135deg,var(--panel2),var(--panel));padding:18px;box-shadow:var(--shadow);border-radius:14px}
.contact-card h3{margin:0 0 6px;font-size:16px;line-height:1.3}.contact-card p{margin:0 0 12px;color:var(--silver);font-size:13px}
section{max-width:var(--max);margin:0 auto;padding:44px clamp(14px,3.5vw,38px)}
.section-head{display:grid;grid-template-columns:minmax(0,.72fr) minmax(220px,.28fr);gap:18px;align-items:end;margin-bottom:20px}
.section-head h2{margin:0;font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;text-transform:uppercase;font-size:clamp(24px,3.2vw,40px);line-height:1.04;letter-spacing:.01em}
.section-head p{color:var(--silver);margin:0;font-size:14px}
.section-head .bar{height:4px;background:linear-gradient(90deg,var(--red),var(--blue));width:70px;margin-bottom:12px;border-radius:2px}
.cat-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.cat-tile{position:relative;border:1px solid var(--line);overflow:hidden;background:var(--panel);min-height:180px;display:flex;flex-direction:column;justify-content:flex-end;transition:.2s;border-radius:12px}
.cat-tile:hover{border-color:var(--red);transform:translateY(-4px)}
.cat-tile img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.42}
.cat-tile:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 28%,rgba(9,10,13,.92))}
.cat-tile span{position:relative;z-index:2;padding:0 16px}
.ct-h{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;font-size:22px;text-transform:uppercase;letter-spacing:.01em;line-height:1.05}
.ct-p{color:var(--silver);font-size:12px;padding-bottom:16px!important;padding-top:6px!important;line-height:1.45}
/* work split: ledger left (scroll) + reviews/message right */
.work-split{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:22px;align-items:start}
.ledger-scroll{max-height:640px;overflow-y:auto;padding-right:10px;border:1px solid var(--line);border-radius:14px;background:rgba(18,20,27,.5)}
.ledger-scroll::-webkit-scrollbar{width:10px}.ledger-scroll::-webkit-scrollbar-thumb{background:var(--red);border-radius:6px}.ledger-scroll::-webkit-scrollbar-track{background:#15171f}
.ledger-scroll{scrollbar-color:var(--red) #15171f;scrollbar-width:thin}
.lscroll-inner{padding:16px}
.col-head{margin-bottom:14px}
.col-head h2{margin:2px 0 0;font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;text-transform:uppercase;font-size:clamp(22px,3vw,34px);line-height:1.05;letter-spacing:.01em}
.col-head .col-see{display:inline-block;margin-top:8px;color:#fff;font-size:12px;text-transform:uppercase;letter-spacing:.06em;border-bottom:1px solid var(--red);padding-bottom:2px}
.work-rail{display:grid;gap:14px;position:sticky;top:78px}
.split{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:22px;align-items:start}
.mag{background:var(--white);color:var(--black);border:1px solid var(--line);box-shadow:var(--shadow);padding:clamp(20px,3.5vw,38px);border-radius:14px}
.mag .kicker{color:var(--red);font-weight:800;text-transform:uppercase;letter-spacing:.12em;font-size:12px}
.mag h2{font-family:Georgia,serif;font-size:clamp(23px,3vw,36px);line-height:1.12;margin:8px 0 12px;color:var(--black)}
.mag h3{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;text-transform:uppercase;font-size:20px;letter-spacing:.01em;margin:22px 0 8px;color:var(--black)}
.mag p{font-family:Georgia,serif;font-size:16px;line-height:1.72;margin:0 0 14px;color:#1a1d24}
.mag .pull{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;font-size:clamp(19px,2.4vw,28px);line-height:1.1;text-transform:uppercase;letter-spacing:.01em;color:var(--blue);border-left:6px solid var(--red);padding:6px 0 6px 16px;margin:20px 0}
.mag img.mech{width:100%;height:auto;border-radius:10px;border:1px solid rgba(9,10,13,.14);margin:8px 0 16px;background:#0d0f14}
.mag .ascii{background:#0d0f14;color:#9fe8b4;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px;line-height:1.35;padding:14px;border-radius:10px;overflow-x:auto;white-space:pre;margin:12px 0}
.issuetabs{display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap}
.issuetabs button{border:1px solid var(--line);background:var(--panel);color:var(--silver);border-radius:999px;padding:8px 14px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;font-size:12px;cursor:pointer}
.issuetabs button.on{background:var(--red);color:#fff;border-color:var(--red)}
.issuepane{display:none}.issuepane.on{display:block}
.rail{display:grid;gap:14px;position:sticky;top:78px}
.card{border:1px solid var(--line);background:var(--panel);padding:16px;border-radius:12px}
.card h4{margin:0 0 10px;font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;text-transform:uppercase;font-size:17px;letter-spacing:.02em;color:#fff}
.card p{color:var(--silver);font-size:13px}
.aff a{display:block;border:1px solid var(--line);border-radius:8px;padding:10px 12px;margin-bottom:8px;background:rgba(0,87,184,.08)}
.aff a:hover{border-color:var(--red);background:rgba(227,6,19,.10)}
.aff b{display:block;font-size:14px;color:#fff}.aff span{font-size:12px;color:var(--silver)}
.rev .rev-score{display:flex;align-items:center;gap:8px;margin-bottom:10px;flex-wrap:wrap}
.rev-num{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;font-size:30px;color:#fff;line-height:1}
.rev-stars{color:#ffc53d;font-size:17px;letter-spacing:1px}
.rev-count{color:var(--silver);font-size:12px}
.rev-rot{position:relative;min-height:54px;margin-bottom:10px}
.rev-card{display:none;color:var(--silver);font-size:14px;line-height:1.5;border-left:3px solid var(--red);padding-left:12px}
.rev-card.on{display:block}
.subcard form{display:grid;gap:8px}
.subcard input,.subcard textarea{background:var(--black);border:1px solid var(--line);color:#fff;padding:11px 12px;border-radius:8px;font-size:14px;font-family:inherit;resize:vertical}
.subcard input::placeholder,.subcard textarea::placeholder{color:#7f8590}
.hp{position:absolute!important;left:-9999px!important;width:1px!important;height:1px!important;opacity:0!important;pointer-events:none}
.sub-ok{display:none;color:#8ff0a6;font-size:13px;margin:4px 0 0;line-height:1.4}
.brandgroup{margin-bottom:22px}
.brandgroup>h3{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;text-transform:uppercase;font-size:20px;letter-spacing:.02em;margin:0 0 12px;display:flex;align-items:center;gap:10px;color:#fff}
.brandgroup>h3:before{content:"";width:24px;height:4px;background:var(--red);border-radius:2px}
.lgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.lgrid.two{grid-template-columns:repeat(2,1fr)}
.lcard{border:1px solid var(--line);background:linear-gradient(180deg,rgba(0,87,184,.10),rgba(245,247,250,.02));padding:15px;display:grid;gap:5px;transition:.15s;border-radius:12px}
.lcard:hover{border-color:var(--red);transform:translateY(-3px)}
.lc-cat{color:var(--red);font-weight:800;text-transform:uppercase;letter-spacing:.08em;font-size:11px}
.lcard b{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;font-size:19px;text-transform:uppercase;line-height:1.08;letter-spacing:.01em;color:#fff}
.lc-yr{color:var(--blue2);font-size:12px;text-transform:uppercase;letter-spacing:.03em;font-weight:600}
.lc-sym{color:var(--silver);font-size:13px;line-height:1.5}
.lc-meta{color:#8f95a0;font-size:11px;text-transform:uppercase;letter-spacing:.03em}
.ytwrap{position:relative;aspect-ratio:16/9;border-radius:12px;overflow:hidden;border:1px solid var(--line);margin:14px 0;background:#000}
.ytwrap iframe{position:absolute;inset:0;width:100%;height:100%}
.vidgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}
.vidgrid .ytwrap{margin:0}
.vrotor{display:grid;gap:12px}
.vrotor-main{margin:0;max-width:860px;width:100%;margin:0 auto}
.vrotor-strip{display:grid;grid-template-columns:repeat(auto-fit,minmax(118px,1fr));gap:10px}
.vthumb{position:relative;border:2px solid var(--line);background:#0d0f14;border-radius:10px;overflow:hidden;cursor:pointer;padding:0;display:block}
.vthumb img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block;opacity:.72;transition:.15s}
.vthumb span{display:block;padding:7px 8px;font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:var(--silver);font-weight:700;background:#0d0f14}
.vthumb:hover img{opacity:1}
.vthumb.on{border-color:var(--red)}.vthumb.on img{opacity:1}.vthumb.on span{color:#fff}
.fbslot{border:1px dashed var(--blue);background:rgba(0,87,184,.07);border-radius:14px;padding:20px;text-align:center;color:var(--silver)}
.fbslot b{display:block;color:#fff;font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;text-transform:uppercase;font-size:19px;margin-bottom:6px}
.fbslot .embed{aspect-ratio:16/9;background:#0d0f14;border:1px solid var(--line);border-radius:10px;margin-top:12px;display:flex;align-items:center;justify-content:center;color:#5f6570;font-size:13px}
.faq-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.faq-grid details{border:1px solid var(--line);padding:16px;background:var(--panel);border-radius:10px}
.faq-grid summary{font-weight:800;cursor:pointer;color:#fff}.faq-grid p{color:var(--silver);font-size:14px;margin:10px 0 0}
.footer{max-width:var(--max);margin:0 auto;padding:36px clamp(14px,3.5vw,38px) 90px;border-top:1px solid var(--line);display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:22px;color:var(--silver)}
.footer strong{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;color:#fff;font-size:22px;text-transform:uppercase;letter-spacing:.02em;display:block;margin-bottom:8px}
.footer a{display:block;padding:4px 0;color:var(--silver)}.footer a:hover{color:#fff}
.footer iframe{width:100%;height:160px;border:1px solid var(--line);border-radius:10px}
/* mobile sticky call/text bar */
.mbar{display:none}
@media(max-width:820px){
 .mbar{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;position:fixed;left:0;right:0;bottom:0;z-index:60;padding:9px 12px;background:rgba(9,10,13,.97);border-top:1px solid var(--line)}
 .mbar a{text-align:center;padding:12px 6px;border-radius:8px;font-weight:800;text-transform:uppercase;font-size:13px;letter-spacing:.03em}
 .mbar-call{background:var(--blue);color:#fff}.mbar-text{background:var(--white);color:var(--black)}.mbar-wa{background:var(--red);color:#fff}
}
/* article (ledger / landing) */
.wrap{max-width:var(--max);margin:0 auto;padding:28px clamp(14px,3.5vw,38px) 80px}
.crumbs{color:var(--silver);font-size:13px;margin-bottom:12px}.crumbs a:hover{color:#fff}
.lede-grid{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:24px;align-items:start}
.kicker{color:var(--red);font-weight:800;text-transform:uppercase;letter-spacing:.12em;font-size:12px;margin:0 0 8px}
.wrap h1{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;text-transform:uppercase;font-size:clamp(26px,4vw,48px);line-height:1.05;letter-spacing:.01em;margin:6px 0 14px}
.deck{font-size:clamp(15px,1.7vw,19px);color:var(--silver);max-width:720px;line-height:1.6}
.meta-row{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0 8px}
.tag{border:1px solid var(--line);border-radius:999px;padding:6px 11px;font-size:12px;text-transform:uppercase;letter-spacing:.04em;color:var(--silver)}
.tag.red{border-color:rgba(227,6,19,.6);color:#ff8b92}.tag.blue{border-color:rgba(0,87,184,.6);color:#9cc3ff}
.tools{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0;align-items:center}
article.body{background:var(--white);color:var(--black);border:1px solid var(--line);box-shadow:var(--shadow);padding:clamp(20px,3.5vw,44px);margin-top:24px;border-radius:14px}
article.body h2{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;text-transform:uppercase;font-size:clamp(21px,2.6vw,30px);letter-spacing:.01em;margin:26px 0 12px;line-height:1.08;color:var(--black)}
article.body h2:first-child{margin-top:0}
article.body p{font-family:Georgia,serif;font-size:17px;line-height:1.75;margin:0 0 16px;max-width:780px;color:#1a1d24}
article.body .pull{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;font-size:clamp(19px,2.4vw,30px);line-height:1.1;text-transform:uppercase;letter-spacing:.01em;color:var(--blue);border-left:6px solid var(--red);padding:8px 0 8px 16px;margin:24px 0}
ol.steps{counter-reset:s;list-style:none;padding:0;margin:0 0 18px;max-width:780px}
ol.steps li{position:relative;padding:13px 16px 13px 54px;border:1px solid rgba(9,10,13,.14);background:#fff;border-radius:10px;margin-bottom:9px;font-family:Inter,Arial,sans-serif;font-size:15px;line-height:1.5;color:#1a1d24}
ol.steps li:before{counter-increment:s;content:counter(s);position:absolute;left:13px;top:12px;width:28px;height:28px;border-radius:6px;background:var(--blue);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:14px}
.callout{border-left:5px solid var(--red);background:#fff;padding:15px 18px;margin:20px 0;border-radius:0 10px 10px 0}
.callout b{display:block;text-transform:uppercase;letter-spacing:.06em;font-size:12px;color:var(--red);margin-bottom:6px;font-family:Inter,Arial,sans-serif}
.verify{border:1px dashed var(--blue);background:#eef4ff;padding:15px 18px;border-radius:10px;margin:22px 0;font-family:Inter,Arial,sans-serif;font-size:14px;color:#1a1d24}
.verify a{color:var(--blue);text-decoration:underline;word-break:break-all}
.cta-block{margin-top:24px;border:1px solid var(--line);background:linear-gradient(135deg,rgba(227,6,19,.16),rgba(0,87,184,.14));padding:22px;display:grid;gap:12px;border-radius:14px}
.cta-block h3{font-family:'Arial Narrow',Impact,sans-serif;font-weight:700;text-transform:uppercase;font-size:clamp(20px,2.4vw,30px);margin:0;line-height:1.08;color:#fff}
.cta-block p{margin:0;color:var(--silver);font-size:14px}.cta-actions{display:flex;gap:10px;flex-wrap:wrap;margin-top:4px;align-items:center}
.relband a{display:block;color:var(--silver);font-size:13px;padding:6px 0;border-bottom:1px solid var(--line)}.relband a:hover{color:#fff}
@media(max-width:980px){
 .site-header{grid-template-columns:1fr}.nav-links{justify-content:flex-start}
 .hero{grid-template-columns:1fr}.cat-grid{grid-template-columns:repeat(2,1fr)}
 .work-split,.split,.lede-grid{grid-template-columns:1fr}.rail,.work-rail{position:static}
 .lgrid,.lgrid.two{grid-template-columns:1fr}.faq-grid,.section-head{grid-template-columns:1fr}.footer{grid-template-columns:1fr}
 .ledger-scroll{max-height:none}
}
"""
