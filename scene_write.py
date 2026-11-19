from buddy_gen import mochi, vixx, sparkle, INK, MUTED, ACC
M = mochi('write', 'wm', 175, 'Mochi writing in a tiny notebook with a pencil')
V = vixx('write', 'wv', 185, 'Sir Vixx writing with a purple quill, sword and shield set aside')
import re as _re
M = M.replace('<defs>', '<defs><radialGradient id="mgb" cx=".36" cy=".3" r=".8"><stop offset="0" stop-color="#fff0f6"/><stop offset=".55" stop-color="#ffd3e4"/><stop offset="1" stop-color="#f5b3cd"/></radialGradient>', 1)
M = _re.sub(r'(<ellipse cx="60" cy="[\d.]+" rx="40" ry="33") fill="#ffd3e4"/>', r'\1 fill="url(#mgb)"/>', M, count=1)
V = _re.sub(r'(<ellipse cx="60" cy="60" rx="38" ry="34") fill="#ffb3c1"', r'\1 fill="url(#vgb)"', V, count=1)
V = V.replace('style="display: block; overflow: visible">', 'style="display: block; overflow: visible"><defs><radialGradient id="vgb" cx=".36" cy=".3" r=".8"><stop offset="0" stop-color="#ffe0e6"/><stop offset=".55" stop-color="#ffb3c1"/><stop offset="1" stop-color="#f2909f"/></radialGradient></defs>', 1)
assert 'url(#mgb)' in M and 'url(#vgb)' in V
HW = "font-family=\"Caveat, cursive\" fill=\"#4e3a5e\""
lines_l = ['l0','l1','l2','l3','l4']
lines_r = ['r0','r1','r2','r3','r4']
def page(lines, x0, y0, tilt):
    o = []
    for i, t in enumerate(lines):
        size = 25 if i == 0 else 20
        o.append(f'<text x="{x0}" y="{y0+i*30}" {HW} font-size="{size}" font-weight="{700 if i==0 else 500}" transform="rotate({tilt} {x0} {y0})">{{{{nb.{t}}}}}</text>')
    return ''.join(o)
svg = f'''<svg viewBox="0 0 960 600" width="960" height="600" role="img" aria-label="First-person view of writing notes at a desk. Sir Vixx and Mochi sit beside the notebook writing in their own tiny books, while the phone shows the Write mode timer.">
<defs>
<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{{{{L.wall1}}}}"/><stop offset="1" stop-color="{{{{L.wall2}}}}"/></linearGradient>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{{{{L.sky1}}}}"/><stop offset="1" stop-color="{{{{L.sky2}}}}"/></linearGradient>
<linearGradient id="desk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f8e8dc"/><stop offset="1" stop-color="#f0d9c9"/></linearGradient>
<linearGradient id="scr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff6fa"/><stop offset=".55" stop-color="#f7f0ff"/><stop offset="1" stop-color="#eef5ff"/></linearGradient>
<linearGradient id="arc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffb3cf"/><stop offset=".5" stop-color="#c7a9f0"/><stop offset="1" stop-color="#9ec5f5"/></linearGradient>
<radialGradient id="glow" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#fff3c4" stop-opacity=".75"/><stop offset="1" stop-color="#fff3c4" stop-opacity="0"/></radialGradient>
<linearGradient id="cone" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff1b8" stop-opacity=".55"/><stop offset="1" stop-color="#fff1b8" stop-opacity="0"/></linearGradient>
<radialGradient id="vig" cx=".5" cy=".55" r=".75"><stop offset=".55" stop-color="#1b1640" stop-opacity="0"/><stop offset="1" stop-color="#1b1640" stop-opacity=".55"/></radialGradient>
<radialGradient id="warm"><stop offset="0" stop-color="#ffe9a8" stop-opacity=".55"/><stop offset="1" stop-color="#ffe9a8" stop-opacity="0"/></radialGradient>
<radialGradient id="cool"><stop offset="0" stop-color="#e9dcff" stop-opacity=".45"/><stop offset="1" stop-color="#e9dcff" stop-opacity="0"/></radialGradient>
<clipPath id="winclip"><rect x="620" y="40" width="250" height="190" rx="18"/></clipPath>
<linearGradient id="haze" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{{{{L.sky2}}}}" stop-opacity="0"/><stop offset="1" stop-color="{{{{L.sky2}}}}" stop-opacity=".55"/></linearGradient>
<filter id="soft" x="-30%" y="-80%" width="160%" height="260%"><feGaussianBlur stdDeviation="8"/></filter>
<radialGradient id="nbglow" cx=".5" cy=".45" r=".6"><stop offset="0" stop-color="#fff4cf" stop-opacity=".55"/><stop offset="1" stop-color="#fff4cf" stop-opacity="0"/></radialGradient>
</defs>
<rect width="960" height="600" fill="url(#wall)"/>
<g clip-path="url(#winclip)">
<rect x="620" y="40" width="250" height="190" fill="url(#sky)"/>
<g opacity="{{{{L.starOp}}}}"><circle cx="650" cy="70" r="1.8" fill="#fffbe6"/><circle cx="690" cy="110" r="1.4" fill="#fffbe6"/><circle cx="712" cy="60" r="2" fill="#fffbe6"/><circle cx="770" cy="150" r="1.5" fill="#fffbe6"/><circle cx="840" cy="170" r="1.8" fill="#fffbe6"/><circle cx="860" cy="60" r="1.4" fill="#fffbe6"/><circle cx="660" cy="170" r="1.3" fill="#fffbe6"/><circle cx="735" cy="190" r="1.6" fill="#fffbe6"/></g>
<circle cx="800" cy="{{{{L.sunY}}}}" r="38" fill="{{{{L.sun}}}}" opacity="{{{{L.haloOp}}}}" filter="url(#soft)"/>
<circle cx="800" cy="{{{{L.sunY}}}}" r="22" fill="{{{{L.sun}}}}" opacity="{{{{L.sunOp}}}}"/>
<path d="M818 66 a22 22 0 1 0 14 34 a18 18 0 1 1 -14 -34 Z" fill="#fff6d8" opacity="{{{{L.moonOp}}}}"/>
<circle cx="822" cy="84" r="34" fill="#fff6d8" opacity="{{{{L.moonOp}}}}" filter="url(#soft)" fill-opacity=".25"/>
<g fill="{{{{L.cloud}}}}" opacity="{{{{L.cloudOp}}}}"><circle cx="650" cy="96" r="12"/><circle cx="664" cy="90" r="15"/><circle cx="680" cy="96" r="12"/><circle cx="666" cy="102" r="12"/><circle cx="640" cy="101" r="8"/><circle cx="690" cy="102" r="8"/><circle cx="752" cy="128" r="10"/><circle cx="763" cy="123" r="12"/><circle cx="776" cy="128" r="10"/><circle cx="765" cy="133" r="10"/><circle cx="744" cy="132" r="6"/><circle cx="784" cy="133" r="6"/><circle cx="700" cy="70" r="7"/><circle cx="708" cy="66" r="9"/><circle cx="718" cy="70" r="7"/><circle cx="710" cy="74" r="7"/><circle cx="694" cy="73" r="5"/><circle cx="724" cy="74" r="5"/></g>
<g stroke="#6b5a7a" stroke-width="1.6" fill="none" stroke-linecap="round" opacity="{{{{L.birdOp}}}}"><path d="M672 120 q4 -4 8 0 q4 -4 8 0"/><path d="M692 108 q3 -3 6 0 q3 -3 6 0"/></g>
<path d="M620 168 Q660 132 702 156 Q740 120 790 150 Q830 128 870 146 V232 H620 Z" fill="{{{{L.hill1}}}}"/>
<rect x="620" y="140" width="250" height="92" fill="url(#haze)"/>
<path d="M620 192 Q668 170 712 186 Q760 166 812 184 Q842 174 870 182 V232 H620 Z" fill="{{{{L.hill2}}}}"/>
<rect x="626" y="182" width="22" height="50" fill="{{{{L.city}}}}"/><path d="M624 182 L637.0 171 L650 182 Z" fill="{{{{L.roof}}}}"/><rect x="650" y="170" width="18" height="62" fill="{{{{L.city}}}}"/><path d="M650 170 Q659.0 156 668 170 Z" fill="{{{{L.roof}}}}"/><rect x="670" y="190" width="26" height="42" fill="{{{{L.city}}}}"/><rect x="685.6" y="181" width="5" height="9" fill="{{{{L.roof}}}}"/><rect x="698" y="176" width="20" height="56" fill="{{{{L.city}}}}"/><path d="M696 176 L708.0 165 L720 176 Z" fill="{{{{L.roof}}}}"/><rect x="720" y="196" width="24" height="36" fill="{{{{L.city}}}}"/><path d="M720 196 Q732.0 182 744 196 Z" fill="{{{{L.roof}}}}"/><rect x="746" y="166" width="18" height="66" fill="{{{{L.city}}}}"/><rect x="756.8" y="157" width="5" height="9" fill="{{{{L.roof}}}}"/><rect x="766" y="184" width="26" height="48" fill="{{{{L.city}}}}"/><path d="M764 184 L779.0 173 L794 184 Z" fill="{{{{L.roof}}}}"/><rect x="794" y="174" width="20" height="58" fill="{{{{L.city}}}}"/><path d="M794 174 Q804.0 160 814 174 Z" fill="{{{{L.roof}}}}"/><rect x="816" y="192" width="24" height="40" fill="{{{{L.city}}}}"/><rect x="830.4" y="183" width="5" height="9" fill="{{{{L.roof}}}}"/><rect x="842" y="178" width="26" height="54" fill="{{{{L.city}}}}"/><path d="M840 178 L855.0 167 L870 178 Z" fill="{{{{L.roof}}}}"/>
<g opacity="{{{{L.cityLit}}}}"><rect x="630" y="204" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="640" y="214" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="656" y="184" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="658" y="198" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="680" y="212" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="692" y="220" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="712" y="194" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="712" y="208" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="754" y="208" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="766" y="218" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="784" y="182" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="784" y="196" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="792" y="210" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="810" y="200" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="820" y="214" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="842" y="190" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="852" y="204" width="4" height="5" rx="1" fill="#ffe7a0"/><rect x="842" y="218" width="4" height="5" rx="1" fill="#ffe7a0"/></g>
<g fill="{{{{L.tree}}}}"><circle cx="634" cy="222" r="14"/><circle cx="652" cy="226" r="11"/><circle cx="742" cy="224" r="13"/><circle cx="760" cy="228" r="10"/><circle cx="856" cy="222" r="14"/></g>
<path d="M640 230 L700 40 L716 40 L656 230 Z M672 230 L732 40 L740 40 L680 230 Z" fill="#ffffff" opacity=".16"/>
</g>
<rect x="620" y="40" width="250" height="190" rx="18" fill="none" stroke="#e6dcf3" stroke-width="8"/>
<path d="M745 40 V230 M620 135 H870" stroke="#e6dcf3" stroke-width="6"/>
<path d="M570 30 H920" stroke="#c7a9f0" stroke-width="6" stroke-linecap="round"/><circle cx="568" cy="30" r="7" fill="#d9c2f7" stroke="#4e3a5e" stroke-width="1.6"/><circle cx="922" cy="30" r="7" fill="#d9c2f7" stroke="#4e3a5e" stroke-width="1.6"/>
<path d="M584 30 L646 30 Q634 98 616 146 Q630 194 634 242 L580 242 Q588 194 596 146 Q586 96 584 30 Z" fill="#ffd9e8" stroke="#d9a3bd" stroke-width="1.8" stroke-linejoin="round"/><path d="M584 30 L598 30 Q598 100 600 146 Q594 196 592 242 L580 242 Q588 194 596 146 Q586 96 584 30 Z" fill="#f4b9d0" opacity=".7"/><path d="M600 34 Q604 100 604 144 M616 34 Q614 96 609 144 M631 34 Q624 96 613 144 M604 152 Q600 200 596 238 M612 152 Q614 200 616 238" fill="none" stroke="#efb2cb" stroke-width="2" stroke-linecap="round"/><ellipse cx="606" cy="148" rx="13" ry="5" fill="#c7a9f0" stroke="#4e3a5e" stroke-width="1.6"/>
<path d="M906 30 L844 30 Q856 98 874 146 Q860 194 856 242 L910 242 Q902 194 894 146 Q904 96 906 30 Z" fill="#ffd9e8" stroke="#d9a3bd" stroke-width="1.8" stroke-linejoin="round"/><path d="M906 30 L892 30 Q892 100 890 146 Q896 196 898 242 L910 242 Q902 194 894 146 Q904 96 906 30 Z" fill="#f4b9d0" opacity=".7"/><path d="M890 34 Q886 100 886 144 M874 34 Q876 96 881 144 M859 34 Q866 96 877 144 M886 152 Q890 200 894 238 M878 152 Q876 200 874 238" fill="none" stroke="#efb2cb" stroke-width="2" stroke-linecap="round"/><ellipse cx="884" cy="148" rx="13" ry="5" fill="#c7a9f0" stroke="#4e3a5e" stroke-width="1.6"/>
<path d="M630 236 L860 236" stroke="#e6dcf3" stroke-width="10" stroke-linecap="round"/>
<g transform="rotate(-4 470 120)"><rect x="420" y="70" width="110" height="96" rx="6" fill="#fff3a8" stroke="#ead98a" stroke-width="2"/>
<text x="434" y="104" {HW} font-size="22" font-weight="700">Next:</text><text x="434" y="134" {HW} font-size="20">{{{{next}}}}</text><circle cx="475" cy="78" r="5" fill="#ff9fc0" stroke="{INK}" stroke-width="1.5"/></g>
<path d="M0 352 H960 V600 H0 Z" fill="url(#desk)"/>
<path d="M0 352 H960" stroke="#e8cdb9" stroke-width="5"/>
<g>
<path d="M570 352 Q570 334 600 334 Q630 334 630 352 Z" fill="#ffc4dc" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
<ellipse cx="600" cy="352" rx="32" ry="7" fill="#f7a8c8" stroke="{INK}" stroke-width="3"/>
<path d="M600 336 L624 270 L566 240" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M600 336 L624 270 L566 240" fill="none" stroke="#ffd3e4" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M606 322 L620 284" stroke="{INK}" stroke-width="1.6" stroke-dasharray="3 3"/>
<circle cx="600" cy="336" r="6" fill="#ffc4dc" stroke="{INK}" stroke-width="2.5"/>
<circle cx="624" cy="270" r="6.5" fill="#ffc4dc" stroke="{INK}" stroke-width="2.5"/>
<g transform="translate(562 240) rotate(28)">
<path d="M-11 -6 Q0 -14 11 -6 L30 38 L-30 38 Z" fill="#ffc4dc" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
<path d="M-4 -6 L-16 32" stroke="#ffe3ee" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="0" cy="38" rx="30" ry="8" fill="{{{{L.bulb}}}}" stroke="{INK}" stroke-width="3"/>
<ellipse cx="0" cy="38" rx="11" ry="4" fill="#ffffff" opacity=".85"/>
</g>
<circle cx="566" cy="240" r="6" fill="#ffc4dc" stroke="{INK}" stroke-width="2.5"/>
</g>
<g transform="translate(26 150) rotate(-6 70 160)">
<ellipse cx="75" cy="354" rx="84" ry="9" fill="#3b2a4a" opacity=".12"/>
<rect x="58" y="290" width="34" height="48" rx="8" fill="#c7a9f0" stroke="{INK}" stroke-width="3"/>
<path d="M66 296 V332" stroke="#e6d7fa" stroke-width="4" stroke-linecap="round"/>
<rect x="4" y="332" width="142" height="18" rx="9" fill="#d9c2f7" stroke="{INK}" stroke-width="3"/>
<path d="M18 337 H120" stroke="#f1e8fd" stroke-width="3" stroke-linecap="round"/>
<circle cx="75" cy="314" r="9" fill="#e6d7fa" stroke="{INK}" stroke-width="2.5"/>
<circle cx="75" cy="314" r="3" fill="{INK}"/>
<rect x="0" y="0" width="150" height="300" rx="24" fill="{INK}"/>
<rect x="8" y="8" width="134" height="284" rx="18" fill="url(#scr)"/>
<text x="24" y="44" font-family="Nunito, sans-serif" font-size="10" font-weight="800" fill="{ACC}" letter-spacing="1">STROKE</text>
<text x="24" y="66" font-family="Nunito, sans-serif" font-size="17" font-weight="900" fill="{INK}">Management</text>
<circle cx="75" cy="140" r="44" fill="none" stroke="#c7a9f0" stroke-opacity=".2" stroke-width="9"/>
<circle cx="75" cy="140" r="44" fill="none" stroke="url(#arc)" stroke-width="9" stroke-linecap="round" stroke-dasharray="276.5" stroke-dashoffset="70" transform="rotate(-90 75 140)"/>
<text x="75" y="150" text-anchor="middle" font-family="Nunito, sans-serif" font-size="27" font-weight="900" fill="{INK}">{{{{timer}}}}</text>
<rect x="20" y="206" width="110" height="46" rx="10" fill="#ffffff"/>
<path d="M30 220 h80 M30 232 h66 M30 244 h74" stroke="#e3d6f2" stroke-width="5" stroke-linecap="round"/>
<rect x="20" y="262" width="50" height="20" rx="10" fill="#ffffff"/><rect x="78" y="262" width="52" height="20" rx="10" fill="#e6d7fa"/>
<path d="M-6 284 H156 V298 Q156 308 146 308 H4 Q-6 308 -6 298 Z" fill="#c7a9f0" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
<path d="M6 291 H140" stroke="#e6d7fa" stroke-width="3" stroke-linecap="round"/>
</g>
<g filter="url(#soft)" opacity="{{{{L.shOp}}}}"><ellipse cx="300" cy="420" rx="110" ry="14" fill="#3b2a4a"/><ellipse cx="830" cy="438" rx="90" ry="12" fill="#3b2a4a"/><ellipse cx="520" cy="612" rx="260" ry="26" fill="#3b2a4a"/></g>
<g transform="translate(908 476)">
<path d="M-38 0 H38 L32 66 Q31 78 18 78 H-18 Q-31 78 -32 66 Z" fill="#bcd8fb" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
<path d="M36 14 q22 2 18 24 q-3 16 -21 16" fill="none" stroke="{INK}" stroke-width="3"/>
<ellipse cx="0" cy="2" rx="36" ry="7" fill="#c49a7c" stroke="{INK}" stroke-width="2.5"/>
<path class="{{{{steamCls}}}}" d="M-12 -14 q-8 -12 0 -24 M6 -12 q-8 -12 0 -24" fill="none" stroke="#d8c8e8" stroke-width="3" stroke-linecap="round"/>
</g>
<g transform="translate(300 398) rotate(-2 225 105)">

<path d="M0 10 Q110 -6 225 18 Q340 -6 450 10 L455 214 Q340 196 225 222 Q110 196 -5 214 Z" fill="#ead9f7" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
<path d="M6 4 Q112 -10 225 12 L225 214 Q112 192 4 206 Z" fill="#ffffff" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M444 4 Q338 -10 225 12 L225 214 Q338 192 446 206 Z" fill="#ffffff" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M225 12 V214" stroke="#d9c9ea" stroke-width="3"/>
{''.join(f'<path d="M22 {44+i*30} Q115 {34+i*30} 212 {50+i*30} M238 {50+i*30} Q335 {34+i*30} 430 {44+i*30}" fill="none" stroke="#e7f0fb" stroke-width="2"/>' for i in range(6))}
<rect x="30" y="72" width="168" height="16" rx="4" fill="#fff07a" opacity=".75" transform="rotate(-2 30 72)"/>
{page(lines_l, 30, 46, -2)}
{page(lines_r, 244, 52, -1)}
</g>
<g transform="translate(168 232)">{V}</g>
<g transform="translate(730 256)">{M}</g>
<rect width="960" height="600" fill="{{{{L.tint}}}}" opacity="{{{{L.tintOp}}}}"/>
<rect width="960" height="600" fill="url(#vig)" opacity="{{{{L.vigOp}}}}"/>
<g transform="translate(300 398) rotate(-2 225 105)">

<path d="M0 10 Q110 -6 225 18 Q340 -6 450 10 L455 214 Q340 196 225 222 Q110 196 -5 214 Z" fill="#ead9f7" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
<path d="M6 4 Q112 -10 225 12 L225 214 Q112 192 4 206 Z" fill="#ffffff" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M444 4 Q338 -10 225 12 L225 214 Q338 192 446 206 Z" fill="#ffffff" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>
<path d="M225 12 V214" stroke="#d9c9ea" stroke-width="3"/>
{''.join(f'<path d="M22 {44+i*30} Q115 {34+i*30} 212 {50+i*30} M238 {50+i*30} Q335 {34+i*30} 430 {44+i*30}" fill="none" stroke="#e7f0fb" stroke-width="2"/>' for i in range(6))}
<rect x="30" y="72" width="168" height="16" rx="4" fill="#fff07a" opacity=".75" transform="rotate(-2 30 72)"/>
{page(lines_l, 30, 46, -2)}
{page(lines_r, 244, 52, -1)}
</g>
<ellipse cx="528" cy="500" rx="250" ry="120" fill="url(#nbglow)" opacity="{{{{L.nbOp}}}}"/>
<g opacity="{{{{L.faceOp}}}}"><ellipse cx="300" cy="320" rx="80" ry="70" fill="url(#warm)"/><ellipse cx="790" cy="345" rx="80" ry="70" fill="url(#warm)"/><ellipse cx="100" cy="300" rx="110" ry="160" fill="url(#cool)"/></g>
<path d="M540 284 L330 600 L760 600 Z" fill="url(#cone)" opacity="{{{{L.glowOp}}}}"/>
<ellipse cx="560" cy="470" rx="300" ry="140" fill="url(#glow)" opacity="{{{{L.glowOp}}}}"/>
<g transform="translate(166 162)"><rect x="{{{{bv.x}}}}" y="0" width="{{{{bv.w}}}}" height="42" rx="16" fill="#ffffff" stroke="#efe3f7" stroke-width="2"/><path d="M78 42 l10 12 l8 -12 Z" fill="#ffffff"/>
<text x="93" y="27" text-anchor="middle" font-family="Nunito, sans-serif" font-size="14" font-weight="800" fill="{INK}">{{{{bv.t}}}}</text></g>
<g transform="translate(724 188)"><rect x="{{{{bm.x}}}}" y="0" width="{{{{bm.w}}}}" height="42" rx="16" fill="#ffffff" stroke="#efe3f7" stroke-width="2"/><path d="M88 42 l10 12 l8 -12 Z" fill="#ffffff"/>
<text x="{{{{bm.cx}}}}" y="27" text-anchor="middle" font-family="Nunito, sans-serif" font-size="14" font-weight="800" fill="{INK}">{{{{bm.t}}}}</text></g>
{sparkle(380, 236, 8)}{sparkle(712, 236, 7, '#ffc4dc')}{sparkle(898, 300, 6, '#bcd8fb')}
</svg>'''
html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Writing together</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&amp;family=Nunito:wght@400;600;700;800;900&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:{ACC}}}a:hover{{color:{INK}}}
.hit:hover{{box-shadow:inset 0 0 0 2px rgba(255,255,255,.55);background:rgba(255,255,255,.08)}}
.hit:focus-visible{{outline:3px dashed #a878d8;outline-offset:2px}}
.hit:active{{background:rgba(255,255,255,.18)}}
.puff{{animation:puff 1.4s ease-out 2}}
@keyframes puff{{0%{{opacity:0;transform:translateY(6px)}}30%{{opacity:1}}100%{{opacity:0;transform:translateY(-14px)}}}}
</style>
</helmet>
<div style="width: 960px; height: 600px; position: relative; overflow: hidden; font-family: Nunito, system-ui, sans-serif; color: {INK}">
{svg}
<div style="position: absolute; left: 32px; top: 26px; display: flex; flex-direction: column; gap: 2px">
<span style="font-size: 12px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: {MUTED}">Write mode</span>
<h1 style="margin: 0; font-size: 34px; line-height: 1.1; font-weight: 900; color: {INK}">Writing together</h1>
</div>
<button class="hit" aria-label="Turn the notebook page" onClick="{{{{tap.notebook}}}}" style="position: absolute; left: 300px; top: 396px; width: 456px; height: 206px; padding: 0; border: 0; border-radius: 18px; background: transparent; cursor: pointer"></button>
<button class="hit" aria-label="Switch the lamp on or off" onClick="{{{{tap.lamp}}}}" style="position: absolute; left: 512px; top: 200px; width: 132px; height: 162px; padding: 0; border: 0; border-radius: 18px; background: transparent; cursor: pointer"></button>
<button class="hit" aria-label="Change the time of day" onClick="{{{{tap.window}}}}" style="position: absolute; left: 620px; top: 40px; width: 250px; height: 192px; padding: 0; border: 0; border-radius: 18px; background: transparent; cursor: pointer"></button>
<button class="hit" aria-label="Start or pause the timer" onClick="{{{{tap.phone}}}}" style="position: absolute; left: 18px; top: 140px; width: 170px; height: 360px; padding: 0; border: 0; border-radius: 18px; background: transparent; cursor: pointer"></button>
<button class="hit" aria-label="Take a sip of tea" onClick="{{{{tap.mug}}}}" style="position: absolute; left: 858px; top: 440px; width: 102px; height: 124px; padding: 0; border: 0; border-radius: 18px; background: transparent; cursor: pointer"></button>
<button class="hit" aria-label="Change the next topic" onClick="{{{{tap.sticky}}}}" style="position: absolute; left: 414px; top: 64px; width: 124px; height: 108px; padding: 0; border: 0; border-radius: 18px; background: transparent; cursor: pointer"></button>
<button class="hit" aria-label="Talk to Sir Vixx" onClick="{{{{tap.vixx}}}}" style="position: absolute; left: 184px; top: 246px; width: 162px; height: 176px; padding: 0; border: 0; border-radius: 18px; background: transparent; cursor: pointer"></button>
<button class="hit" aria-label="Talk to Mochi" onClick="{{{{tap.mochi}}}}" style="position: absolute; left: 748px; top: 272px; width: 146px; height: 160px; padding: 0; border: 0; border-radius: 18px; background: transparent; cursor: pointer"></button>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"time":{{"editor":"enum","options":["Auto","Day","Evening","Twilight","Night"],"default":"Auto"}},"$preview":{{"width":960,"height":600}}}}'>
const LIGHT = {{
  Day: {{ wall1: '#fff4f9', wall2: '#f1eaff', sky1: '#8fc6ff', sky2: '#dcefff', sun: '#fff1a8', sunY: 82, sunOp: 1, haloOp: 0.35, moonOp: 0, starOp: 0, cloud: '#ffffff', cloudOp: 0.95, tint: '#ffffff', tintOp: 0, glowOp: 0.15, bulb: '#fff8e0', city: '#f4e3ee', cityLit: 0, shOp: 0.08, vigOp: 0, faceOp: 0, nbOp: 0, hill1: '#b9d7f0', hill2: '#a8d4bd', roof: '#f2a7b5', tree: '#8cc7a0', birdOp: 1 }},
  Evening: {{ wall1: '#fff0e6', wall2: '#f8e3ef', sky1: '#ff9e7a', sky2: '#ffd9a0', sun: '#ffb062', sunY: 198, sunOp: 1, haloOp: 0.4, moonOp: 0, starOp: 0, cloud: '#ffd0c2', cloudOp: 0.9, tint: '#ff9a5c', tintOp: 0.1, glowOp: 0.45, bulb: '#fff1b8', city: '#d98fa0', cityLit: 0.35, shOp: 0.12, vigOp: 0.12, faceOp: 0.4, nbOp: 0.5, hill1: '#eeb0bd', hill2: '#d695ad', roof: '#e38f8f', tree: '#b97c9c', birdOp: 0.8 }},
  Twilight: {{ wall1: '#eee3fa', wall2: '#ded3f3', sky1: '#5d63bd', sky2: '#f2a3c6', sun: '#ffb062', sunY: 240, sunOp: 0, haloOp: 0, moonOp: 0.75, starOp: 0.5, cloud: '#c9a6e0', cloudOp: 0.6, tint: '#6e5ac0', tintOp: 0.14, glowOp: 0.7, bulb: '#ffe98a', city: '#4a4791', cityLit: 0.75, shOp: 0.16, vigOp: 0.35, faceOp: 0.7, nbOp: 0.8, hill1: '#8f81cc', hill2: '#7064b4', roof: '#8473c6', tree: '#5d539c', birdOp: 0 }},
  Night: {{ wall1: '#e4dcf4', wall2: '#d3cbea', sky1: '#171b45', sky2: '#363b85', sun: '#ffb062', sunY: 240, sunOp: 0, haloOp: 0, moonOp: 1, starOp: 1, cloud: '#4a4f97', cloudOp: 0.5, tint: '#1e1e5a', tintOp: 0.24, glowOp: 0.95, bulb: '#ffe066', city: '#232660', cityLit: 1, shOp: 0.22, vigOp: 0.6, faceOp: 1, nbOp: 1, hill1: '#2e3374', hill2: '#252966', roof: '#363b80', tree: '#1d2152', birdOp: 0 }}
}};
function phase(d) {{
  const h = d.getHours() + d.getMinutes() / 60;
  if (h >= 7.25 && h < 18.25) return 'Day';
  if (h >= 18.25 && h < 19.25) return 'Evening';
  if ((h >= 19.25 && h < 20) || (h >= 6.5 && h < 7.25)) return 'Twilight';
  return 'Night';
}}
const PAGES = [
  {{ l0: 'Stroke · Mx', l1: 'IV alteplase 0.9 mg/kg', l2: '(max 90 mg) <4.5 h', l3: 'thrombectomy LVO', l4: 'up to 24 h selected', r0: 'aspirin + clopidogrel', r1: '× 21 days (minor/TIA)', r2: 'swallow screen!', r3: 'statin, BP, AF → DOAC', r4: 'rehab' }},
  {{ l0: 'DKA · Mx', l1: 'IV 0.9% saline', l2: 'FRIII 0.1 U/kg/h', l3: 'add K+ if 3.5–5.5', l4: 'glucose <14 → +10% dex', r0: 'hourly CBG, ketones', r1: 'VBG: pH, HCO3, K+', r2: 'resolved: ketones <0.6', r3: '+ pH >7.3', r4: 'find the trigger!' }},
  {{ l0: 'HFrEF · Mx', l1: 'ACEi / ARNI', l2: '+ β-blocker', l3: '+ MRA', l4: '+ SGLT2 inhibitor', r0: 'loop diuretic', r1: 'for congestion', r2: 'daily weights', r3: 'echo: EF ≤40%', r4: 'device if EF ≤35%' }}
];
const TOPICS = ['Complications', 'Investigations', 'Key facts', 'History', 'Examination'];
const TIMES = ['Day', 'Evening', 'Twilight', 'Night'];
const LINES = {{
  vixx: ['I shall guard thy focus', 'Onward, squire!', 'A fine page indeed', 'Hold the line!', 'Quill and shield ready', 'Huzzah!'],
  mochi: ['Writing with you!', 'You’re doing great', 'Little by little', 'Drink some water?', 'Hehe, that tickles', 'Pretty notes!']
}};
const bub = (t, cx) => ({{ t, w: Math.round(t.length * 7.6 + 30), x: Math.round(cx - (t.length * 7.6 + 30) / 2), cx }});
class Component extends DCLogic {{
constructor(p) {{ super(p); this.state = {{ lamp: true, time: null, page: 0, topic: 0, left: 600, running: false, done: false, vi: 0, mi: 0, steam: 0 }}; }}
componentDidMount() {{
  this.tick = setInterval(() => {{
    if (this.state.running) {{
      const left = this.state.left - 1;
      if (left <= 0) this.setState({{ left: 0, running: false, done: true, vi: -1, mi: -1 }});
      else this.setState({{ left }});
    }} else if (Date.now() % 60000 < 1000) this.forceUpdate();
  }}, 1000);
}}
componentWillUnmount() {{ clearInterval(this.tick); clearTimeout(this.st); }}
renderVals() {{
  const S = this.state, pt = this.props.time ?? 'Auto';
  const key = S.time || (pt === 'Auto' ? phase(new Date()) : pt);
  let L = LIGHT[key] || LIGHT.Day;
  if (!S.lamp) L = {{ ...L, glowOp: 0, faceOp: 0, nbOp: 0, bulb: '#d9d2e3' }};
  const m = Math.floor(S.left / 60), sec = S.left % 60;
  const vt = S.vi < 0 ? 'Victory, scribe!' : LINES.vixx[S.vi % LINES.vixx.length];
  const mt = S.mi < 0 ? 'Yay, page done!' : S.steam && S.mi === 3 ? 'Ahh, warm tea' : LINES.mochi[S.mi % LINES.mochi.length];
  return {{
    L, nb: PAGES[S.page % PAGES.length], next: TOPICS[S.topic % TOPICS.length],
    timer: S.done ? 'Done!' : m + ':' + String(sec).padStart(2, '0'),
    steamCls: S.steam ? 'puff' : '',
    bv: bub(vt, 93), bm: bub(mt, 80),
    tap: {{
      lamp: () => this.setState({{ lamp: !S.lamp }}),
      window: () => this.setState({{ time: TIMES[(TIMES.indexOf(key) + 1) % TIMES.length] }}),
      phone: () => S.done ? this.setState({{ done: false, left: 600, running: true, vi: 0, mi: 0 }}) : this.setState({{ running: !S.running }}),
      notebook: () => this.setState({{ page: S.page + 1 }}),
      sticky: () => this.setState({{ topic: S.topic + 1 }}),
      vixx: () => this.setState({{ vi: Math.max(0, S.vi) + 1 }}),
      mochi: () => this.setState({{ mi: Math.max(0, S.mi) + 1 }}),
      mug: () => {{ clearTimeout(this.st); this.setState({{ steam: S.steam + 1, mi: 3 }}); this.st = setTimeout(() => this.setState({{ steam: 0 }}), 2900); }}
    }}
  }};
}}
}}
</script>
</body>
</html>
'''
open('dev/concept/project/Writing.dc.html', 'w').write(html)
