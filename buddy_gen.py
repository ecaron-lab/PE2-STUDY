import json, sys

INK = '#4e3a5e'
MUTED = '#6f5a80'
ACC = '#a878d8'


def sparkle(x, y, s, c='#ffd166'):
    return (f'<path d="M{x} {y-s} Q{x} {y} {x+s} {y} Q{x} {y} {x} {y+s} Q{x} {y} {x-s} {y} Q{x} {y} {x} {y-s} Z" '
            f'fill="{c}" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"/>')


def zz(x, y):
    return (f'<text x="{x}" y="{y}" font-family="Nunito, sans-serif" font-weight="800" font-size="16" fill="{ACC}">z</text>'
            f'<text x="{x+11}" y="{y-10}" font-family="Nunito, sans-serif" font-weight="800" font-size="12" fill="{ACC}">z</text>'
            f'<text x="{x+19}" y="{y-18}" font-family="Nunito, sans-serif" font-weight="800" font-size="9" fill="{ACC}">z</text>')


def sweat(x, y):
    return f'<path d="M{x} {y} q6 8 0 11 q-6 -3 0 -11 z" fill="#bcd8fb" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>'


def motion(x, y):
    return ''.join(f'<path d="M{x} {y+i*9} h{10-i*3}" stroke="#c9b6e6" stroke-width="3" stroke-linecap="round"/>' for i in range(3))


def bang(x, y):
    return f'<text x="{x}" y="{y}" font-family="Nunito, sans-serif" font-weight="900" font-size="22" fill="{ACC}">!</text>'


def hand(x1, x2, y):
    return (f'<rect x="{x1-9}" y="-12" width="{x2-x1+18}" height="{y+8}" rx="8" fill="#ffe2cf" stroke="{INK}" stroke-width="2.5"/>'
            f'<ellipse cx="{x1}" cy="{y}" rx="5.5" ry="4.5" fill="#ffe2cf" stroke="{INK}" stroke-width="2.5"/>'
            f'<ellipse cx="{x2}" cy="{y}" rx="5.5" ry="4.5" fill="#ffe2cf" stroke="{INK}" stroke-width="2.5"/>')


def shadow(y, rx=28):
    return f'<ellipse cx="60" cy="{y}" rx="{rx}" ry="4" fill="{INK}" opacity="0.08"/>'


def tabbar(y=98):
    return (f'<rect x="4" y="{y}" width="112" height="18" rx="9" fill="#ffffff" stroke="#e2d3f2" stroke-width="2"/>'
            + ''.join(f'<rect x="{x}" y="{y+6}" width="20" height="6" rx="3" fill="#ead9f7"/>' for x in (14, 50, 86)))


def eye(x, y, kind, r=3.6):
    if kind == 'happy':
        return f'<path d="M{x-4} {y+2} Q{x} {y-4} {x+4} {y+2}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>'
    if kind == 'closed':
        return f'<path d="M{x-4} {y} Q{x} {y+4} {x+4} {y}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>'
    if kind == 'down':
        return (f'<circle cx="{x}" cy="{y+2}" r="{r-0.6}" fill="{INK}"/>'
                f'<circle cx="{x+0.9:.1f}" cy="{y+3.3:.1f}" r="1" fill="#ffffff"/>')
    if kind == 'wide':
        r = r + 1.2
    if kind == 'small':
        r = r - 1
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{INK}"/>'
            f'<circle cx="{x+r*0.35:.1f}" cy="{y-r*0.35:.1f}" r="{max(1,r*0.32):.1f}" fill="#ffffff"/>')


def mouth(x, y, kind):
    if kind == 'smile':
        return f'<path d="M{x-5} {y} Q{x} {y+5} {x+5} {y}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>'
    if kind == 'open':
        return f'<path d="M{x-6} {y-1} Q{x} {y+11} {x+6} {y-1} Z" fill="{INK}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/><path d="M{x-3} {y+5} Q{x} {y+3} {x+3} {y+5}" fill="none" stroke="#ff9fc0" stroke-width="2.4" stroke-linecap="round"/>'
    if kind == 'wavy':
        return f'<path d="M{x-7} {y+1} q3.5 -3 7 0 q3.5 3 7 0" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>'
    if kind == 'tongue':
        return (f'<path d="M{x-5} {y} Q{x} {y+4} {x+5} {y}" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>'
                f'<path d="M{x+1} {y+2} q3 6 6 0" fill="#ff8fb5" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>')
    if kind == 'o':
        return f'<ellipse cx="{x}" cy="{y+1}" rx="2.6" ry="3.2" fill="{INK}"/>'
    return ''


def svg(inner, size, label):
    return (f'<svg viewBox="0 0 120 120" width="{size}" height="{size}" role="img" aria-label="{label}" '
            f'style="display: block; overflow: visible">{inner}</svg>')


# ---------- Mochi ----------
def minibook(y, quill=False):
    o = (f'<path d="M30 {y} L60 {y+5} L60 {y+20} L30 {y+15} Z" fill="#ffffff" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>'
         f'<path d="M60 {y+5} L90 {y} L90 {y+15} L60 {y+20} Z" fill="#ffffff" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>'
         f'<path d="M35 {y+5} L55 {y+9} M35 {y+9} L52 {y+12.5} M65 {y+9} L84 {y+5} M65 {y+12.5} L78 {y+10}" stroke="#c9b6e6" stroke-width="1.6" stroke-linecap="round"/>')
    if quill:
        o += (f'<g transform="translate(78 {y+9}) rotate(-35)">'
              f'<path d="M0 0 L0 -6 Q-6 -22 2 -34 Q8 -20 3 -6 L3 0 Z" fill="#c7a9f0" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>'
              f'<path d="M1.5 -4 L2 -28" stroke="{INK}" stroke-width="1.2"/></g>')
    else:
        o += (f'<g transform="translate(80 {y+9}) rotate(-40)">'
              f'<rect x="-2.6" y="-26" width="5.2" height="22" rx="1" fill="#ffd166" stroke="{INK}" stroke-width="1.8"/>'
              f'<rect x="-2.6" y="-30" width="5.2" height="5" rx="1.5" fill="#ff9fc0" stroke="{INK}" stroke-width="1.8"/>'
              f'<path d="M-2.6 -4 L0 2 L2.6 -4 Z" fill="#ffe2cf" stroke="{INK}" stroke-width="1.6" stroke-linejoin="round"/></g>')
    return o


def mochi(pose, uid, size, label):
    cy, rx, ry = 70, 40, 33
    tf = ''
    arms = [(20, 80, 0), (100, 80, 0)]
    feet = [(47, 104), (73, 104)]
    eyes, mth, brows = 'open', 'smile', False
    before = after = ''
    if pose == 'walk':
        tf = 'rotate(-5 60 100)'
        feet = [(42, 104), (76, 99)]
        arms = [(22, 72, -30), (99, 86, 20)]
        before = motion(2, 58)
        after = shadow(112)
    elif pose == 'sit':
        cy = 64
        before = tabbar(97)
        feet = [(49, 101), (71, 101)]
        arms = [(22, 74, 0), (98, 74, 0)]
    elif pose == 'write':
        cy = 64
        feet = [(49, 101), (71, 101)]
        arms = []
        eyes, mth = 'down', 'tongue'
        after = minibook(84) + f'<ellipse cx="33" cy="92" rx="8" ry="5.5" fill="#ffd3e4" stroke="{INK}" stroke-width="2.5"/><ellipse cx="80" cy="92" rx="8" ry="5.5" fill="#ffd3e4" stroke="{INK}" stroke-width="2.5"/>' + shadow(108, 34)
    elif pose == 'nap':
        cy, rx, ry = 76, 43, 28
        eyes, mth = 'closed', 'o'
        feet = []
        arms = [(20, 84, 0), (100, 84, 0)]
        after = zz(88, 40) + shadow(108, 34)
    elif pose == 'cheer':
        tf = 'translate(0 -8)'
        arms = [(24, 46, -40), (96, 46, 40)]
        eyes, mth = 'happy', 'open'
        after = sparkle(12, 26, 7) + sparkle(106, 20, 6, '#ffc4dc') + sparkle(108, 62, 5, '#bcd8fb') + shadow(114, 22)
    elif pose == 'worried':
        eyes, mth, brows = 'small', 'wavy', True
        arms = [(50, 90, 0), (70, 90, 0)]
        after = sweat(90, 42) + shadow(110)
    elif pose == 'held':
        tf = 'rotate(6 60 40)'
        cy = 72
        feet = [(48, 112), (72, 110)]
        arms = [(18, 72, -50), (102, 72, 50)]
        eyes, mth = 'wide', 'o'
        after = bang(96, 52)
    else:
        after = shadow(110)
    top = cy - ry
    o = []
    o.append(f'<defs><clipPath id="mb{uid}"><ellipse cx="60" cy="{cy}" rx="{rx}" ry="{ry}"/></clipPath></defs>')
    o.append(before)
    if pose == 'held':
        o.append(hand(52, 68, 24))
    o.append(f'<g transform="{tf}">' if tf else '<g>')
    for fx, fy in feet:
        o.append(f'<ellipse cx="{fx}" cy="{fy}" rx="8" ry="4.5" fill="#f7a8c8" stroke="{INK}" stroke-width="2.5"/>')
    for ax, ay, rot in arms:
        o.append(f'<ellipse cx="{ax}" cy="{ay}" rx="8" ry="5.5" transform="rotate({rot} {ax} {ay})" fill="#ffd3e4" stroke="{INK}" stroke-width="2.5"/>')
    o.append(f'<ellipse cx="60" cy="{cy}" rx="{rx}" ry="{ry}" fill="#ffd3e4"/>')
    cl = cy + 10
    o.append(f'<g clip-path="url(#mb{uid})"><rect x="0" y="{cl}" width="120" height="60" fill="#ffffff"/>'
             f'<path d="M60 {cl} L53 {cl+13} M60 {cl} L67 {cl+13}" stroke="#ddd0ea" stroke-width="2" fill="none"/>'
             f'<path d="M73 {cl+12} h9" stroke="#ddd0ea" stroke-width="2"/></g>')
    o.append(f'<ellipse cx="60" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<path d="M45 {cl} Q49 {cl+12} 60 {cl+12} Q71 {cl+12} 75 {cl}" fill="none" stroke="#8a79a0" stroke-width="2.4" stroke-linecap="round"/>'
             f'<path d="M60 {cl+12} v4" stroke="#8a79a0" stroke-width="2.4"/><circle cx="60" cy="{cl+19}" r="3.2" fill="#d6cde3" stroke="#8a79a0" stroke-width="2"/>')
    o.append(f'<path d="M60 {top+1} V{top-7}" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>'
             f'<ellipse cx="54" cy="{top-8}" rx="6" ry="3.4" transform="rotate(25 54 {top-8})" fill="#b7e3c4" stroke="{INK}" stroke-width="2"/>'
             f'<ellipse cx="66" cy="{top-8}" rx="6" ry="3.4" transform="rotate(-25 66 {top-8})" fill="#b7e3c4" stroke="{INK}" stroke-width="2"/>')
    ey = cy - 6
    o.append(f'<ellipse cx="40" cy="{cy+3}" rx="6" ry="3.4" fill="#ff9fc0" opacity="0.6"/><ellipse cx="80" cy="{cy+3}" rx="6" ry="3.4" fill="#ff9fc0" opacity="0.6"/>')
    if brows:
        o.append(f'<path d="M41 {ey-8} L52 {ey-13} M79 {ey-8} L68 {ey-13}" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>')
    o.append(eye(48, ey, eyes) + eye(72, ey, eyes))
    o.append(mouth(60, cy, mth))
    o.append('</g>')
    o.append(after)
    return svg(''.join(o), size, label)


# ---------- Ruby (red blood cell) ----------
def ruby(pose, uid, size, label):
    tf = ''
    legs = [((50, 96), (48, 110)), ((70, 96), (72, 110))]
    arms = [((24, 66), (14, 80)), ((96, 66), (106, 80))]
    clip = (100, 74, 0)
    eyes, mth, brows = 'open', 'smile', False
    before = after = ''
    cy = 64
    if pose == 'walk':
        tf = 'rotate(-8 60 70)'
        legs = [((50, 96), (40, 108)), ((70, 96), (80, 106))]
        arms = [((24, 66), (12, 56)), ((96, 66), (106, 80))]
        before = motion(0, 50)
        after = shadow(114) + f'<circle cx="30" cy="110" r="3" fill="#eadff5"/><circle cx="24" cy="106" r="2" fill="#eadff5"/>'
    elif pose == 'sit':
        cy = 60
        before = tabbar(96)
        legs = [((50, 90), (47, 106)), ((70, 90), (73, 106))]
        arms = [((24, 62), (50, 84)), ((96, 62), (70, 84))]
        clip = (51, 80, 0)
    elif pose == 'nap':
        tf = 'rotate(-14 60 70)'
        eyes, mth = 'closed', 'o'
        legs = [((50, 96), (44, 108)), ((70, 96), (76, 108))]
        arms = [((24, 66), (16, 82)), ((96, 66), (104, 82))]
        clip = None
        after = zz(90, 34) + shadow(114, 34) + f'<g transform="rotate(-70 98 108)"><rect x="90" y="100" width="14" height="18" rx="2" fill="#ffffff" stroke="{INK}" stroke-width="2"/></g>'
    elif pose == 'cheer':
        tf = 'translate(0 -6)'
        arms = [((24, 60), (12, 38)), ((96, 60), (108, 38))]
        eyes, mth = 'happy', 'open'
        clip = None
        after = (f'<g transform="rotate(20 104 12)"><rect x="97" y="2" width="14" height="18" rx="2" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
                 f'<rect x="101" y="0" width="6" height="4" rx="1" fill="#c7a9f0" stroke="{INK}" stroke-width="1.5"/></g>'
                 + sparkle(14, 20, 7) + sparkle(84, 8, 5, '#ffc4dc') + shadow(116, 22))
    elif pose == 'worried':
        eyes, mth, brows = 'small', 'wavy', True
        legs = [((54, 96), (57, 110)), ((66, 96), (63, 110))]
        arms = [((24, 66), (48, 88)), ((96, 66), (72, 88))]
        clip = (53, 84, 0)
        after = sweat(92, 34) + shadow(114)
    elif pose == 'held':
        tf = 'rotate(5 60 30)'
        legs = [((50, 96), (44, 116)), ((70, 96), (76, 116))]
        arms = [((24, 66), (8, 58)), ((96, 66), (112, 58))]
        eyes, mth = 'wide', 'o'
        clip = None
        after = bang(98, 48)
    else:
        after = shadow(114)
    o = [before]
    if pose == 'held':
        o.append(hand(52, 68, 30))
    o.append(f'<g transform="{tf}">' if tf else '<g>')
    for (a, b) in legs:
        o.append(f'<path d="M{a[0]} {a[1]} L{b[0]} {b[1]}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
                 f'<ellipse cx="{b[0]}" cy="{b[1]+1}" rx="5" ry="3" fill="{INK}"/>')
    for (a, b) in arms:
        o.append(f'<path d="M{a[0]} {a[1]} L{b[0]} {b[1]}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
                 f'<circle cx="{b[0]}" cy="{b[1]}" r="3" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
    o.append(f'<ellipse cx="60" cy="{cy}" rx="38" ry="34" fill="#ffb3c1" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<ellipse cx="60" cy="{cy+2}" rx="21" ry="16" fill="#ffd6de" stroke="#f08aa0" stroke-width="2"/>')
    o.append(f'<path d="M31 {cy-12} Q35 {cy-24} 47 {cy-28}" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="0.85"/>')
    o.append(f'<ellipse cx="34" cy="{cy+7}" rx="5.5" ry="3.2" fill="#ff8aa6" opacity="0.55"/><ellipse cx="86" cy="{cy+7}" rx="5.5" ry="3.2" fill="#ff8aa6" opacity="0.55"/>')
    ey = cy - 1
    if brows:
        o.append(f'<path d="M47 {ey-7} L55 {ey-10} M73 {ey-7} L65 {ey-10}" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>')
    o.append(eye(53, ey, eyes, 3.2) + eye(67, ey, eyes, 3.2))
    o.append(mouth(60, cy + 6, mth))
    if clip:
        x, y, r = clip
        o.append(f'<g transform="rotate({r} {x+7} {y+9})"><rect x="{x}" y="{y}" width="14" height="18" rx="2" fill="#ffffff" stroke="{INK}" stroke-width="2"/>'
                 f'<rect x="{x+4}" y="{y-2}" width="6" height="4" rx="1" fill="#c7a9f0" stroke="{INK}" stroke-width="1.5"/>'
                 f'<path d="M{x+3} {y+7} h8 M{x+3} {y+11} h8 M{x+3} {y+15} h5" stroke="#c9b6e6" stroke-width="1.5"/></g>')
    o.append('</g>')
    o.append(after)
    return svg(''.join(o), size, label)


# ---------- Hoot (owl) ----------
def hoot(pose, uid, size, label):
    tf = ''
    cy = 66
    wings = 'side'
    feet_y = 103
    eyes, brows = 'open', False
    before = after = ''
    if pose == 'walk':
        tf = 'rotate(-6 60 100)'
        before = motion(0, 54)
        after = shadow(112)
    elif pose == 'sit':
        cy = 60
        feet_y = 97
        before = tabbar(97)
    elif pose == 'nap':
        tf = 'rotate(8 60 100)'
        eyes = 'closed'
        after = zz(90, 30) + shadow(110)
    elif pose == 'cheer':
        tf = 'translate(0 -6)'
        wings = 'up'
        eyes = 'happy'
        after = sparkle(12, 24, 7) + sparkle(108, 18, 6, '#ffc4dc') + sparkle(106, 60, 5, '#bcd8fb') + shadow(114, 22)
    elif pose == 'worried':
        wings = 'hug'
        eyes, brows = 'small', True
        after = sweat(94, 30) + shadow(110)
    elif pose == 'held':
        tf = 'rotate(5 60 26)'
        wings = 'flap'
        feet_y = 109
        eyes = 'wide'
        after = bang(100, 50)
    else:
        after = shadow(110)
    top = cy - 38
    o = [before]
    if pose == 'held':
        o.append(hand(52, 68, 22))
    o.append(f'<g transform="{tf}">' if tf else '<g>')
    o.append(f'<path d="M36 {top+14} L31 {top-6} L48 {top+5} Z M84 {top+14} L89 {top-6} L72 {top+5} Z" fill="#c7a9f0" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>')
    if wings == 'up':
        o.append(f'<path d="M30 {cy-6} Q12 {cy-26} 22 {cy-42} Q34 {cy-26} 36 {cy-8} Z M90 {cy-6} Q108 {cy-26} 98 {cy-42} Q86 {cy-26} 84 {cy-8} Z" fill="#c7a9f0" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>')
    elif wings == 'flap':
        o.append(f'<path d="M28 {cy-4} Q6 {cy-12} 3 {cy-28} Q18 {cy-20} 33 {cy-10} Z M92 {cy-4} Q114 {cy-12} 117 {cy-28} Q102 {cy-20} 87 {cy-10} Z" fill="#c7a9f0" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>')
    for fx in (50, 70):
        o.append(f'<path d="M{fx} {feet_y} l-4 6 M{fx} {feet_y} l0 7 M{fx} {feet_y} l4 6" stroke="#f0a35e" stroke-width="3" stroke-linecap="round"/>')
    o.append(f'<ellipse cx="60" cy="{cy}" rx="34" ry="38" fill="#d9c2f7" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<ellipse cx="60" cy="{cy+14}" rx="20" ry="20" fill="#f3ecfd"/>'
             f'<path d="M51 {cy+10} l3 3 l3 -3 M63 {cy+10} l3 3 l3 -3 M57 {cy+20} l3 3 l3 -3" fill="none" stroke="#c3abe6" stroke-width="2" stroke-linecap="round"/>')
    if wings == 'side':
        o.append(f'<path d="M27 {cy-4} Q16 {cy+12} 28 {cy+26} Q34 {cy+14} 33 {cy-2} Z M93 {cy-4} Q104 {cy+12} 92 {cy+26} Q86 {cy+14} 87 {cy-2} Z" fill="#c7a9f0" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>')
    elif wings == 'hug':
        o.append(f'<path d="M29 {cy-2} Q36 {cy+20} 56 {cy+22} Q44 {cy+8} 36 {cy-4} Z M91 {cy-2} Q84 {cy+20} 64 {cy+22} Q76 {cy+8} 84 {cy-4} Z" fill="#c7a9f0" stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>')
    o.append(f'<path d="M30 {top+18} Q60 {top-2} 90 {top+18}" fill="none" stroke="#8a79a0" stroke-width="2.4" stroke-linecap="round"/>'
             f'<circle cx="60" cy="{top+9}" r="5" fill="#e8f1fb" stroke="{INK}" stroke-width="2"/><path d="M58 {top+7} l2 -1" stroke="#ffffff" stroke-width="1.6" stroke-linecap="round"/>')
    ey = cy - 10
    for ex in (48, 72):
        o.append(f'<circle cx="{ex}" cy="{ey}" r="11" fill="#ffffff" stroke="{INK}" stroke-width="2.5"/>')
        if eyes == 'open':
            o.append(f'<circle cx="{ex+1}" cy="{ey+1}" r="5" fill="{INK}"/><circle cx="{ex+3}" cy="{ey-1}" r="1.6" fill="#ffffff"/>')
        elif eyes == 'wide':
            o.append(f'<circle cx="{ex}" cy="{ey}" r="6.2" fill="{INK}"/><circle cx="{ex+2.4}" cy="{ey-2.4}" r="2" fill="#ffffff"/>')
        elif eyes == 'small':
            o.append(f'<circle cx="{ex}" cy="{ey+3}" r="3.2" fill="{INK}"/>')
        elif eyes == 'happy':
            o.append(f'<path d="M{ex-5} {ey+2} Q{ex} {ey-5} {ex+5} {ey+2}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>')
        elif eyes == 'closed':
            o.append(f'<path d="M{ex-5} {ey} Q{ex} {ey+5} {ex+5} {ey}" fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>')
    o.append(f'<path d="M59 {ey-1} Q60 {ey-4} 61 {ey-1}" fill="none" stroke="{INK}" stroke-width="2.5"/>')
    if brows:
        o.append(f'<path d="M37 {ey-14} L49 {ey-18} M83 {ey-14} L71 {ey-18}" stroke="{INK}" stroke-width="2.4" stroke-linecap="round"/>')
    o.append(f'<path d="M56 {ey+10} L64 {ey+10} L60 {ey+17} Z" fill="#ffc98a" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>')
    o.append('</g>')
    o.append(after)
    return svg(''.join(o), size, label)


# ---------- Sir Vixx (knighted red blood cell) ----------
def sword(x, y, rot):
    return (f'<g transform="translate({x} {y}) rotate({rot})">'
            f'<path d="M-2.6 -4 L-2.6 -30 L0 -36 L2.6 -30 L2.6 -4 Z" fill="#eef1f7" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>'
            f'<path d="M0 -30 V-7" stroke="#cfd5e3" stroke-width="1.4"/>'
            f'<rect x="-8.5" y="-6" width="17" height="4.5" rx="2.2" fill="#c7a9f0" stroke="{INK}" stroke-width="2"/>'
            f'<rect x="-2" y="-1.5" width="4" height="8" rx="1.5" fill="{INK}"/>'
            f'<circle cx="0" cy="8.5" r="2.6" fill="#ffd166" stroke="{INK}" stroke-width="1.6"/></g>')


def shield(x, y, rot=0, s=1):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">'
            f'<path d="M-10 -11 H10 V-2 Q10 10 0 15 Q-10 10 -10 -2 Z" fill="#ffffff" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/>'
            f'<ellipse cx="0" cy="0.5" rx="5.5" ry="5" fill="#ffb3c1" stroke="{INK}" stroke-width="1.6"/>'
            f'<ellipse cx="0" cy="1" rx="2.4" ry="2" fill="#ffd6de"/></g>')


def vixx(pose, uid, size, label):
    tf = ''
    cy = 64
    legs = [((50, 96), (48, 110)), ((70, 96), (72, 110))]
    arms = [((24, 66), (14, 80)), ((96, 66), (106, 80))]
    sw = (106, 80, 18)
    sh = (14, 80, 0, 1)
    helm_rot = 0
    cape = True
    eyes, mth, brows = 'open', 'smile', False
    before = after = ''
    if pose == 'walk':
        tf = 'rotate(-8 60 70)'
        legs = [((50, 96), (40, 108)), ((70, 96), (80, 106))]
        arms = [((24, 66), (16, 74)), ((96, 66), (108, 66))]
        sw = (108, 66, 70)
        sh = (16, 74, -10, 1)
        before = motion(0, 50)
        after = shadow(114) + '<circle cx="30" cy="110" r="3" fill="#eadff5"/><circle cx="24" cy="106" r="2" fill="#eadff5"/>'
    elif pose == 'sit':
        cy = 60
        before = tabbar(96)
        legs = [((50, 90), (47, 106)), ((70, 90), (73, 106))]
        arms = [((24, 62), (16, 76)), ((96, 62), (104, 76))]
        sw = (104, 76, 0)
        sh = (16, 76, 0, 0.9)
    elif pose == 'write':
        cy = 60
        legs = [((50, 90), (47, 106)), ((70, 90), (73, 106))]
        arms = [((24, 62), (34, 88)), ((96, 62), (80, 88))]
        sw = None
        sh = None
        eyes, mth = 'down', 'smile'
        before = sword(110, 76, 180) + shield(10, 92, -8, 0.95)
        after = minibook(86, quill=True) + shadow(112, 40)
    elif pose == 'nap':
        tf = 'rotate(-14 60 70)'
        eyes, mth = 'closed', 'o'
        legs = [((50, 96), (44, 108)), ((70, 96), (76, 108))]
        arms = [((24, 66), (16, 82)), ((96, 66), (104, 82))]
        sw = None
        sh = (16, 84, 20, 0.9)
        helm_rot = -18
        after = zz(92, 30) + shadow(114, 34) + sword(86, 112, -90)
    elif pose == 'cheer':
        tf = 'translate(0 -6)'
        arms = [((24, 60), (12, 40)), ((96, 60), (108, 40))]
        sw = (108, 40, 10)
        sh = (12, 40, -15, 0.9)
        eyes, mth = 'happy', 'open'
        after = sparkle(30, 10, 6) + sparkle(84, 4, 5, '#ffc4dc') + shadow(116, 22)
    elif pose == 'worried':
        eyes, mth, brows = 'small', 'wavy', True
        legs = [((54, 96), (57, 110)), ((66, 96), (63, 110))]
        arms = [((24, 66), (42, 86)), ((96, 66), (104, 80))]
        sw = (104, 80, 8)
        sh = (42, 86, 0, 1.15)
        after = sweat(94, 22) + shadow(114)
    elif pose == 'held':
        tf = 'rotate(5 60 22)'
        legs = [((50, 96), (44, 116)), ((70, 96), (76, 116))]
        arms = [((24, 66), (8, 58)), ((96, 66), (112, 74))]
        sw = (112, 74, 170)
        sh = (8, 58, -30, 0.9)
        eyes, mth = 'wide', 'o'
        after = bang(100, 40)
    else:
        after = shadow(114)
    top = cy - 34
    o = [before]
    if pose == 'held':
        o.append(hand(54, 66, 6))
    o.append(f'<g transform="{tf}">' if tf else '<g>')
    if cape:
        o.append(f'<path d="M30 {cy-14} Q16 {cy+22} 26 {cy+40} L94 {cy+40} Q104 {cy+22} 90 {cy-14} Z" fill="#c7a9f0" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>')
    for (a, b) in legs:
        o.append(f'<path d="M{a[0]} {a[1]} L{b[0]} {b[1]}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>'
                 f'<ellipse cx="{b[0]}" cy="{b[1]+1}" rx="5.5" ry="3.2" fill="#b9c1d3" stroke="{INK}" stroke-width="1.8"/>')
    for (a, b) in arms:
        o.append(f'<path d="M{a[0]} {a[1]} L{b[0]} {b[1]}" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    o.append(f'<ellipse cx="60" cy="{cy}" rx="38" ry="34" fill="#ffb3c1" stroke="{INK}" stroke-width="3"/>')
    o.append(f'<ellipse cx="60" cy="{cy+2}" rx="21" ry="16" fill="#ffd6de" stroke="#f08aa0" stroke-width="2"/>')
    o.append(f'<path d="M30 {cy-6} Q32 {cy-16} 38 {cy-22}" fill="none" stroke="#ffffff" stroke-width="3" stroke-linecap="round" opacity="0.85"/>')
    o.append(f'<ellipse cx="34" cy="{cy+7}" rx="5.5" ry="3.2" fill="#ff8aa6" opacity="0.55"/><ellipse cx="86" cy="{cy+7}" rx="5.5" ry="3.2" fill="#ff8aa6" opacity="0.55"/>')
    ey = cy - 1
    if brows:
        o.append(f'<path d="M47 {ey-7} L55 {ey-10} M73 {ey-7} L65 {ey-10}" stroke="{INK}" stroke-width="2.2" stroke-linecap="round"/>')
    o.append(eye(53, ey, eyes, 3.2) + eye(67, ey, eyes, 3.2))
    o.append(mouth(60, cy + 6, mth))
    o.append(f'<g transform="rotate({helm_rot} 60 {top+4})">'
             f'<path d="M60 {top-16} Q66 {top-32} 82 {top-28} Q71 {top-24} 65 {top-14} Z" fill="#c7a9f0" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>'
             f'<path d="M43 {top+7} Q43 {top-16} 60 {top-16} Q77 {top-16} 77 {top+7} Z" fill="#e6e9f2" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>'
             f'<path d="M60 {top-15} V{top+5}" stroke="#cfd5e3" stroke-width="2"/>'
             f'<rect x="40" y="{top+3}" width="40" height="7" rx="3.5" fill="#cfd5e3" stroke="{INK}" stroke-width="2"/>'
             f'<path d="M49 {top-8} Q51 {top-12} 55 {top-13}" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/></g>')
    if sh:
        o.append(shield(*sh))
    if sw:
        o.append(sword(*sw))
    o.append('</g>')
    o.append(after)
    return svg(''.join(o), size, label)


POSES = [
    ('walk', 'Walks', 'Strolls along the bottom of the screen'),
    ('sit', 'Sits', 'Perches on the tab bar while you study'),
    ('nap', 'Naps', 'Dozes off when the app sits idle'),
    ('cheer', 'Cheers', 'Celebrates when you rate a card Solid'),
    ('worried', 'Frets', 'Gets anxious when Shaky cards pile up'),
    ('held', 'Picked up', 'Dangles when you drag it around'),
]

CHARS = {
    'mochi': dict(fn=mochi, file='Main.dc.html', label='Concept A', name='Mochi', bg='#ffe4ee', chip='#ffd3e4',
                  desc='A squishy rice-cake blob in a tiny white coat, with a stethoscope it can barely reach. Soft-spoken and encouraging, it waddles along your tabs and never judges a Shaky card.',
                  traits=['Gentle', 'Encouraging', 'Waddles']),
    'ruby': dict(fn=vixx, file='Ruby.dc.html', label='Concept B', name='Sir Vixx', bg='#ffe6ea', chip='#ffd0da',
                 desc='The same pink red blood cell, now knighted. A plumed helm, a little cape, a sword and a shield with a cell on it. Gallant, a bit dramatic, and charges straight at every Shaky card.',
                 traits=['Brave', 'Dramatic', 'Charges in'],
                 captions={'walk': ('Charges', 'Gallops along the bottom of the screen, sword first'),
                           'sit': ('Stands guard', 'Keeps watch from the tab bar while you study'),
                           'nap': ('Naps', 'Dozes off with his helm askew when the app sits idle'),
                           'cheer': ('Cheers', 'Raises his sword when you rate a card Solid'),
                           'worried': ('Takes cover', 'Hides behind his shield when Shaky cards pile up'),
                           'held': ('Picked up', 'Dangles, sword and all, when you drag him')}),
    'hoot': dict(fn=hoot, file='Hoot.dc.html', label='Concept C', name='Hoot', bg='#ede4fb', chip='#ddcdf7',
                 desc='A night-owl registrar with oversized glasses and a head mirror. Calm, a little sleepy, and good company for late revision sessions.',
                 traits=['Calm', 'Wise', 'Night owl']),
}


def artboard(key):
    c = CHARS[key]
    fn = c['fn']
    hero = fn('idle', key + 'h', 220, c['name'] + ' standing')
    cells = ''.join(
        f'<div style="background: #ffffff; border: 1px solid #f1e6f4; border-radius: 20px; padding: 12px 12px 14px; display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center">'
        f'<div style="width: 104px; height: 104px">{fn(p, key + p, 104, c["name"] + " " + t.lower())}</div>'
        f'<strong style="font-size: 15px; color: {INK}">{t}</strong>'
        f'<span style="font-size: 12.5px; line-height: 1.35; color: {MUTED}">{d}</span></div>'
        for p, t, d in [(p, *c.get('captions', {}).get(p, (t, d))) for p, t, d in POSES])
    chips = ''.join(f'<span style="background: {c["chip"]}; color: {INK}; font-size: 13px; font-weight: 700; padding: 6px 12px; border-radius: 999px">{t}</span>' for t in c['traits'])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{c["label"]}: {c["name"]}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:{ACC}}}a:hover{{color:{INK}}}
</style>
</helmet>
<div style="width: 960px; height: 600px; box-sizing: border-box; padding: 40px; display: flex; gap: 32px; background: #fffafc; font-family: Nunito, system-ui, sans-serif; color: {INK}">
<div style="width: 360px; flex: none; box-sizing: border-box; border-radius: 28px; background: {c["bg"]}; padding: 28px; display: flex; flex-direction: column; gap: 12px">
<span style="font-size: 12px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: {MUTED}">{c["label"]}</span>
<div style="display: flex; justify-content: center">{hero}</div>
<h1 style="margin: 0; font-size: 40px; line-height: 1.1; font-weight: 900; color: {INK}">{c["name"]}</h1>
<p style="margin: 0; font-size: 15px; line-height: 1.45; color: {INK}">{c["desc"]}</p>
<div style="display: flex; flex-wrap: wrap; gap: 8px">{chips}</div>
</div>
<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 16px">
<div style="display: flex; flex-direction: column; gap: 4px">
<h2 style="margin: 0; font-size: 24px; font-weight: 800; color: {INK}">How {c["name"]} moves</h2>
<span style="font-size: 14px; color: {MUTED}">Six poses it would switch between inside the app</span>
</div>
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px">{cells}</div>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":960,"height":600}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''


if __name__ == '__main__':
    key, out = sys.argv[1], sys.argv[2]
    open(out, 'w').write(artboard(key))
