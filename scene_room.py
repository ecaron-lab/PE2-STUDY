import re
from buddy_gen import mochi, vixx, sparkle, INK
def shade(M, V):
    M = M.replace('<defs>', '<defs><radialGradient id="rmb" cx=".36" cy=".3" r=".8"><stop offset="0" stop-color="#fff0f6"/><stop offset=".55" stop-color="#ffd3e4"/><stop offset="1" stop-color="#f0a9c4"/></radialGradient>', 1)
    M = re.sub(r'(<ellipse cx="60" cy="[\d.]+" rx="40" ry="33") fill="#ffd3e4"/>', r'\1 fill="url(#rmb)"/>', M, count=1)
    V = re.sub(r'(<ellipse cx="60" cy="60" rx="38" ry="34") fill="#ffb3c1"', r'\1 fill="url(#rvb)"', V, count=1)
    V = V.replace('style="display: block; overflow: visible">', 'style="display: block; overflow: visible"><defs><radialGradient id="rvb" cx=".36" cy=".3" r=".8"><stop offset="0" stop-color="#ffe0e6"/><stop offset=".55" stop-color="#ffb3c1"/><stop offset="1" stop-color="#ee8a9a"/></radialGradient></defs>', 1)
    assert 'url(#rmb)' in M and 'url(#rvb)' in V
    return M, V
M, V = shade(mochi('write', 'rm', 96, 'Mochi writing in a tiny notebook'), vixx('write', 'rv', 104, 'Sir Vixx writing with a quill'))
H = lambda k: '{{L.' + k + '}}'
LN = '#6b4a5a'
bld = [(392,300,46,'#f6c9b8'),(436,278,40,'#f3dcc0'),(474,312,52,'#e9c3d6'),(524,268,38,'#f6d8b0'),(560,296,50,'#d9c9ec'),(608,284,34,'#f6c9b8'),
       (644,262,44,'#f3dcc0'),(686,300,52,'#e9c3d6'),(736,276,40,'#f6d8b0'),(774,306,46,'#d9c9ec'),(818,270,40,'#f6c9b8'),(856,298,44,'#f3dcc0')]
city = []
lit = []
for i,(x,y,w,c) in enumerate(bld):
    city.append(f'<rect x="{x}" y="{y}" width="{w}" height="{404-y}" fill="{c}"/>')
    city.append(f'<path d="M{x-4} {y} L{x+w/2} {y-16-(i%3)*6} L{x+w+4} {y} Z" fill="{["#e58f7f","#d98aa6","#b99ad6"][i%3]}"/>')
    city.append(f'<rect x="{x+w*0.62}" y="{y}" width="{w*0.38}" height="{404-y}" fill="#6b4a7a" opacity=".12"/>')
    for r in range(3):
        for cidx in range(2):
            wx, wy = x + 8 + cidx*(w-24), y + 14 + r*26
            if wy < 392:
                city.append(f'<rect x="{wx}" y="{wy}" width="8" height="11" rx="1.5" fill="#fff6ea" opacity=".75"/>')
                if (i + r + cidx) % 3 != 1:
                    lit.append(f'<rect x="{wx}" y="{wy}" width="8" height="11" rx="1.5" fill="#ffd77a"/>')
stars = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fffbe6"/>' for x,y,r in [(420,70,1.6),(470,120,1.2),(520,60,1.8),(600,100,1.3),(700,70,1.6),(760,130,1.2),(820,60,1.8),(870,110,1.3),(560,160,1.1),(670,150,1.4)])
books = ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{100-y if sh==0 else 214-y}" rx="2" fill="{c}" stroke="{LN}" stroke-width="1.5"/>'
    for x,y,w,c,sh in [(30,46,16,'#ffb3c1',0),(46,40,14,'#bcd8fb',0),(60,52,18,'#d9c2f7',0),(78,44,12,'#ffe08a',0),(96,58,30,'#bde8cf',0),
                       (36,152,18,'#d9c2f7',1),(54,146,14,'#ffb3c1',1),(68,158,16,'#ffd3a8',1),(118,150,14,'#bcd8fb',1),(132,160,20,'#ffb3c1',1)])
leaf = lambda x,y,r,s,c: f'<path d="M0 0 Q{s*0.5} {-s*0.35} {s} 0 Q{s*0.5} {s*0.35} 0 0 Z" transform="translate({x} {y}) rotate({r})" fill="{c}"/>'
svg = f'''<svg viewBox="0 0 960 600" width="960" height="600" role="img" aria-label="Over-the-shoulder view of a student writing at a desk by a big window, with Mochi and Sir Vixx writing beside her.">
<defs>
<linearGradient id="rw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{H('wall1')}"/><stop offset="1" stop-color="{H('wall2')}"/></linearGradient>
<linearGradient id="rs" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{H('sky1')}"/><stop offset="1" stop-color="{H('sky2')}"/></linearGradient>
<linearGradient id="rd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eebf93"/><stop offset="1" stop-color="#d89f74"/></linearGradient>
<linearGradient id="beam" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{H('beam')}" stop-opacity=".9"/><stop offset="1" stop-color="{H('beam')}" stop-opacity="0"/></linearGradient>
<radialGradient id="pool"><stop offset="0" stop-color="#ffe7a6" stop-opacity=".9"/><stop offset="1" stop-color="#ffe7a6" stop-opacity="0"/></radialGradient>
<radialGradient id="bloom"><stop offset="0" stop-color="{H('beam')}" stop-opacity=".8"/><stop offset="1" stop-color="{H('beam')}" stop-opacity="0"/></radialGradient>
<radialGradient id="rvig" cx=".5" cy=".5" r=".75"><stop offset=".5" stop-color="#1b1236" stop-opacity="0"/><stop offset="1" stop-color="#1b1236" stop-opacity=".7"/></radialGradient>
<linearGradient id="hair" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6e4648"/><stop offset="1" stop-color="#3f262c"/></linearGradient>
<linearGradient id="knit" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d7c4f3"/><stop offset="1" stop-color="#a68fd0"/></linearGradient>
<clipPath id="win"><rect x="380" y="40" width="520" height="364" rx="6"/></clipPath>
<filter id="blur6" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="blur2"><feGaussianBlur stdDeviation="2"/></filter>
</defs>
<rect width="960" height="600" fill="url(#rw)"/>
<g>
<rect x="20" y="100" width="200" height="10" rx="3" fill="#c98f6c" stroke="{LN}" stroke-width="1.5"/>
<rect x="20" y="214" width="200" height="10" rx="3" fill="#c98f6c" stroke="{LN}" stroke-width="1.5"/>
{books}
<g transform="translate(176 72)"><path d="M-14 28 H14 L10 46 H-10 Z" fill="#f2a98f" stroke="{LN}" stroke-width="1.5"/>{leaf(0,28,-120,26,'#7fbf8f')}{leaf(0,28,-60,26,'#8fcf9c')}{leaf(0,28,-95,30,'#6fae80')}</g>
<rect x="150" y="160" width="40" height="54" rx="4" fill="#fff3a8" stroke="{LN}" stroke-width="1.5" transform="rotate(-4 170 187)"/>
</g>
<g clip-path="url(#win)">
<rect x="380" y="40" width="520" height="364" fill="url(#rs)"/>
<g opacity="{H('starOp')}">{stars}</g>
<circle cx="760" cy="{H('sunY')}" r="30" fill="{H('sun')}" opacity="{H('sunOp')}"/>
<circle cx="760" cy="{H('sunY')}" r="70" fill="{H('sun')}" opacity="{H('haloOp')}" filter="url(#blur6)"/>
<path d="M792 92 a26 26 0 1 0 16 40 a21 21 0 1 1 -16 -40 Z" fill="#fff6d8" opacity="{H('moonOp')}"/>
<path d="M420 150 q24 -20 48 0 q20 -16 40 0 Z M640 120 q18 -14 36 0 q14 -10 28 0 Z" fill="{H('cloud')}" opacity="{H('cloudOp')}"/>
{''.join(city)}
<rect x="380" y="40" width="520" height="364" fill="{H('cityTint')}" opacity="{H('cityTintOp')}"/>
<g opacity="{H('lit')}">{''.join(lit)}</g>
</g>
<rect x="380" y="40" width="520" height="364" rx="6" fill="none" stroke="#c48e6e" stroke-width="12"/>
<path d="M640 40 V404 M380 214 H900" stroke="#c48e6e" stroke-width="9"/>
<path d="M386 46 V398 M646 46 V208" stroke="#e2b291" stroke-width="2"/>
<rect x="364" y="398" width="552" height="14" rx="4" fill="#d6a07c" stroke="{LN}" stroke-width="1.5"/>
<path d="M342 20 Q382 120 360 250 Q352 330 372 420 L322 420 Q336 300 318 160 Q312 70 330 20 Z" fill="#ffd3e4" stroke="{LN}" stroke-width="1.5"/>
<path d="M336 30 Q356 140 340 260" fill="none" stroke="#f3b6cd" stroke-width="5" stroke-linecap="round"/>
<path d="M926 20 Q904 140 920 260 Q928 340 914 420 L960 420 L960 20 Z" fill="#ffd3e4" stroke="{LN}" stroke-width="1.5"/>
<ellipse cx="640" cy="230" rx="330" ry="210" fill="url(#bloom)" opacity="{H('bloomOp')}"/>
<path d="M412 410 L960 410 L960 486 L0 486 L0 410 Z" fill="url(#rd)"/>
<path d="M0 410 H960" stroke="#f6d4b4" stroke-width="3"/>
<path d="M0 486 H960 V600 H0 Z" fill="#c78a62"/>
<path d="M0 486 H960" stroke="{LN}" stroke-width="2"/>
<g opacity="{H('beamOp')}"><path d="M560 44 L640 44 L430 486 L300 486 Z" fill="url(#beam)"/><path d="M700 44 L760 44 L600 486 L500 486 Z" fill="url(#beam)"/><path d="M820 44 L860 44 L760 486 L690 486 Z" fill="url(#beam)"/></g>
<g>
<ellipse cx="96" cy="446" rx="38" ry="9" fill="#ffc4dc" stroke="{LN}" stroke-width="2"/>
<path d="M96 442 L74 330 L176 262" fill="none" stroke="{LN}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M96 442 L74 330 L176 262" fill="none" stroke="#ffc4dc" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="74" cy="330" r="7" fill="#ffc4dc" stroke="{LN}" stroke-width="2"/>
<path d="M164 240 L224 236 Q236 276 208 296 L156 282 Z" fill="#ffc4dc" stroke="{LN}" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M170 248 L214 246" stroke="#ffe3ee" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="184" cy="290" rx="26" ry="8" transform="rotate(16 184 290)" fill="{H('bulb')}"/>
</g>
<ellipse cx="560" cy="452" rx="240" ry="56" fill="url(#pool)" opacity="{H('lampOp')}"/>
<g transform="translate(470 418)">
<path d="M0 6 Q44 -2 88 8 Q132 -2 176 6 L184 44 Q132 36 88 46 Q44 36 -8 44 Z" fill="#fffdf8" stroke="{LN}" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M88 8 V46" stroke="#e6d6ea" stroke-width="2"/>
<path d="M12 18 Q46 13 80 19 M12 26 Q44 21 76 27 M12 34 Q40 30 66 35 M98 19 Q132 13 166 18 M98 27 Q126 22 150 26" stroke="#9a8aa8" stroke-width="1.4" fill="none" stroke-linecap="round"/>
<rect x="10" y="14" width="44" height="6" rx="2" fill="#fff07a" opacity=".7"/>
</g>
<g transform="translate(398 344)">
<path d="M8 74 L-2 90 H44 L34 74 Z" fill="#d9c2f7" stroke="{LN}" stroke-width="1.8"/>
<rect x="0" y="0" width="42" height="76" rx="7" fill="#4e3a5e"/>
<rect x="3" y="3" width="36" height="70" rx="5" fill="#fbf4ff"/>
<circle cx="21" cy="32" r="12" fill="none" stroke="#ead9f7" stroke-width="3.5"/>
<path d="M21 20 A12 12 0 1 1 9.6 35.7" fill="none" stroke="#c7a9f0" stroke-width="3.5" stroke-linecap="round"/>
<text x="21" y="35.5" text-anchor="middle" font-family="Nunito, sans-serif" font-size="8.5" font-weight="900" fill="#4e3a5e">7:24</text>
<rect x="8" y="52" width="26" height="4" rx="2" fill="#e6d7fa"/><rect x="8" y="60" width="18" height="4" rx="2" fill="#e6d7fa"/>
</g>
<ellipse cx="420" cy="438" rx="44" ry="18" fill="#bfd4ff" opacity="{H('screenOp')}" filter="url(#blur6)"/>
<g transform="translate(672 398)">
<path d="M0 0 H30 L27 28 Q26 34 18 34 H12 Q4 34 3 28 Z" fill="#bcd8fb" stroke="{LN}" stroke-width="1.8"/>
<path d="M30 7 q11 1 9 12 q-2 7 -10 7" fill="none" stroke="{LN}" stroke-width="1.8"/>
<path d="M10 -6 q-5 -8 0 -16 M20 -5 q-5 -8 0 -16" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".7"/>
</g>
<g filter="url(#blur2)" opacity=".18"><ellipse cx="755" cy="432" rx="44" ry="6" fill="#3b2a4a"/><ellipse cx="850" cy="434" rx="48" ry="6" fill="#3b2a4a"/></g>
<g transform="translate(707 340)">{M}</g>
<g transform="translate(798 330)">{V}</g>
<g transform="translate(910 404)"><path d="M-22 0 H22 L17 40 H-17 Z" fill="#f2a98f" stroke="{LN}" stroke-width="1.8"/>{leaf(0,0,-150,60,'#6fae80')}{leaf(0,0,-110,70,'#7fbf8f')}{leaf(0,0,-75,64,'#8fcf9c')}{leaf(0,0,-40,50,'#6fae80')}{leaf(0,0,-125,48,'#9bd8a8')}</g>
<g>
<rect x="282" y="352" width="36" height="46" fill="#f2c3a6"/>
<path d="M300 392 C250 392 196 404 168 440 C140 476 128 540 124 600 L476 600 C472 540 462 480 440 446 C416 408 352 392 300 392 Z" fill="url(#knit)" stroke="{LN}" stroke-width="2"/>
<path d="M300 392 C250 392 196 404 168 440 C140 476 128 540 124 600 L230 600 C222 540 226 470 262 420 Z" fill="#9682c4" opacity=".35"/>
<path d="M254 400 Q300 418 346 400" fill="none" stroke="#9c86c9" stroke-width="9" stroke-linecap="round"/>
<path d="M300 420 V600" stroke="#9c86c9" stroke-width="3" opacity=".6"/>
<path d="M430 440 Q470 478 548 452" fill="none" stroke="{LN}" stroke-width="48" stroke-linecap="round"/>
<path d="M430 440 Q470 478 548 452" fill="none" stroke="#c5b0ec" stroke-width="44" stroke-linecap="round"/>
<path d="M444 424 Q484 452 548 434" fill="none" stroke="#e4d8fb" stroke-width="6" stroke-linecap="round" opacity=".8"/>
<ellipse cx="566" cy="448" rx="16" ry="11" fill="#f6cdb4" stroke="{LN}" stroke-width="1.8"/>
<path d="M560 448 L592 424" stroke="{LN}" stroke-width="6" stroke-linecap="round"/><path d="M560 448 L592 424" stroke="#c7a9f0" stroke-width="3.5" stroke-linecap="round"/>
<path d="M190 446 Q240 486 330 478" fill="none" stroke="{LN}" stroke-width="44" stroke-linecap="round"/>
<path d="M190 446 Q240 486 330 478" fill="none" stroke="#a993d2" stroke-width="40" stroke-linecap="round"/>
<ellipse cx="234" cy="314" rx="8" ry="13" fill="#f2c3a6" stroke="{LN}" stroke-width="1.6"/>
<ellipse cx="366" cy="314" rx="8" ry="13" fill="#f6cdb4" stroke="{LN}" stroke-width="1.6"/>
<path d="M234 300 C234 236 268 214 300 214 C332 214 366 236 366 300 C366 350 338 376 300 376 C262 376 234 350 234 300 Z" fill="url(#hair)" stroke="{LN}" stroke-width="2"/>
<path d="M268 244 Q300 228 340 248" fill="none" stroke="#8d6264" stroke-width="5" stroke-linecap="round" opacity=".7"/>
<path d="M300 220 Q296 290 300 360 M276 228 Q262 290 270 352 M326 228 Q340 290 332 352" fill="none" stroke="#2f1c22" stroke-width="1.6" opacity=".45"/>
<ellipse cx="300" cy="352" rx="24" ry="9" fill="#ffb3cf" stroke="{LN}" stroke-width="1.8"/>
<circle cx="300" cy="380" r="27" fill="url(#hair)" stroke="{LN}" stroke-width="2"/>
<path d="M286 368 Q300 362 314 370" fill="none" stroke="#8d6264" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<g opacity="{H('rimOp')}" fill="none" stroke="{H('rim')}" stroke-linecap="round"><path d="M340 232 Q366 262 364 310" stroke-width="4"/><path d="M420 420 Q452 448 466 500" stroke-width="4"/><path d="M322 368 Q328 384 320 398" stroke-width="3"/></g>
</g>
<g>
<rect x="150" y="512" width="300" height="26" rx="12" fill="#b77d5a" stroke="{LN}" stroke-width="2"/>
<path d="M162 518 H436" stroke="#d29c76" stroke-width="3" stroke-linecap="round"/>
{''.join(f'<rect x="{x}" y="536" width="16" height="70" rx="5" fill="#a96f4d" stroke="{LN}" stroke-width="2"/>' for x in (196,262,328,394))}
</g>
<g opacity="{H('dustOp')}" fill="#fff8e6">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x,y,r in [(520,180,1.8),(560,260,1.2),(610,140,1.5),(680,230,1.3),(720,170,1.9),(590,330,1.2),(500,300,1.5),(770,260,1.2)])}</g>
<rect width="960" height="600" fill="{H('tint')}" opacity="{H('tintOp')}"/>
<ellipse cx="200" cy="300" rx="190" ry="190" fill="url(#pool)" opacity="{H('lampHalo')}"/>
<ellipse cx="560" cy="450" rx="200" ry="60" fill="url(#pool)" opacity="{H('lampHalo')}"/>
<rect width="960" height="600" fill="url(#rvig)" opacity="{H('vigOp')}"/>
<g fill="#3f7a5a" opacity=".92">{leaf(-10,600,-40,120,'#3f7a5a')}{leaf(10,600,-70,140,'#4f8f68')}{leaf(40,600,-20,100,'#356b4f')}{leaf(960,600,-140,130,'#3f7a5a')}{leaf(940,600,-110,150,'#4f8f68')}{leaf(930,600,-165,110,'#356b4f')}</g>
{sparkle(700, 326, 6)}{sparkle(906, 318, 5, '#ffc4dc')}
</svg>'''
LIGHT = '''const LIGHT = {
  Day: { wall1: '#fff3ea', wall2: '#f7e6ef', sky1: '#8ec5ff', sky2: '#e3f1ff', sun: '#fff1a8', sunY: 90, sunOp: 1, haloOp: 0.35, moonOp: 0, starOp: 0, cloud: '#ffffff', cloudOp: 0.95, cityTint: '#ffffff', cityTintOp: 0, lit: 0, beam: '#fffaf0', beamOp: 0.35, bloomOp: 0.35, bulb: '#fff8e0', lampOp: 0.1, lampHalo: 0, screenOp: 0, rim: '#fff3d0', rimOp: 0.7, dustOp: 0.8, tint: '#ffffff', tintOp: 0, vigOp: 0.1 },
  Evening: { wall1: '#ffe8d4', wall2: '#f6d4dc', sky1: '#ff8f6b', sky2: '#ffd394', sun: '#ffb062', sunY: 330, sunOp: 1, haloOp: 0.5, moonOp: 0, starOp: 0, cloud: '#ffc2b0', cloudOp: 0.9, cityTint: '#ff9a62', cityTintOp: 0.18, lit: 0.35, beam: '#ffc27a', beamOp: 0.5, bloomOp: 0.55, bulb: '#fff1b8', lampOp: 0.45, lampHalo: 0.15, screenOp: 0.2, rim: '#ffb46a', rimOp: 1, dustOp: 1, tint: '#ff8a4c', tintOp: 0.1, vigOp: 0.3 },
  Twilight: { wall1: '#eadff6', wall2: '#d9cdef', sky1: '#585fb8', sky2: '#f2a2c4', sun: '#ffb062', sunY: 420, sunOp: 0, haloOp: 0, moonOp: 0.7, starOp: 0.5, cloud: '#c6a2de', cloudOp: 0.6, cityTint: '#5a4a9a', cityTintOp: 0.35, lit: 0.8, beam: '#f2a2c4', beamOp: 0.15, bloomOp: 0.3, bulb: '#ffe98a', lampOp: 0.8, lampHalo: 0.35, screenOp: 0.5, rim: '#f2a2c4', rimOp: 0.8, dustOp: 0.3, tint: '#5e4ab8', tintOp: 0.16, vigOp: 0.5 },
  Night: { wall1: '#e0d6f2', wall2: '#cfc4e8', sky1: '#131737', sky2: '#2e347a', sun: '#ffb062', sunY: 420, sunOp: 0, haloOp: 0, moonOp: 1, starOp: 1, cloud: '#454a94', cloudOp: 0.5, cityTint: '#151845', cityTintOp: 0.6, lit: 1, beam: '#9fb3ff', beamOp: 0.08, bloomOp: 0.15, bulb: '#ffe066', lampOp: 1, lampHalo: 0.55, screenOp: 0.9, rim: '#a9b8ff', rimOp: 0.6, dustOp: 0, tint: '#1a1a52', tintOp: 0.3, vigOp: 0.75 }
};
function phase(d) {
  const h = d.getHours() + d.getMinutes() / 60;
  if (h >= 7.25 && h < 18.25) return 'Day';
  if (h >= 18.25 && h < 19.25) return 'Evening';
  if ((h >= 19.25 && h < 20) || (h >= 6.5 && h < 7.25)) return 'Twilight';
  return 'Night';
}
class Component extends DCLogic {
componentDidMount() { this.tick = setInterval(() => this.forceUpdate(), 60000); }
componentWillUnmount() { clearInterval(this.tick); }
renderVals() {
const t = this.props.time ?? 'Auto';
return { L: LIGHT[t === 'Auto' ? phase(new Date()) : t] || LIGHT.Day };
}
}'''
html = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Write mode study room</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&amp;display=swap" rel="stylesheet">
<style>
body{margin:0}
a{color:#a878d8}a:hover{color:#4e3a5e}
</style>
</helmet>
<div style="width: 960px; height: 600px; position: relative; overflow: hidden; font-family: Nunito, system-ui, sans-serif; color: #4e3a5e">
''' + svg + '''
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"time":{"editor":"enum","options":["Auto","Day","Evening","Twilight","Night"],"default":"Auto"},"$preview":{"width":960,"height":600}}'>
''' + LIGHT + '''
</script>
</body>
</html>
'''
open('dev/concept/project/StudyRoom.dc.html', 'w').write(html)
