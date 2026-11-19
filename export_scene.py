import re, json
s = open('dev/concept/project/Writing.dc.html').read()
a = s.index('<svg viewBox="0 0 960 600"')
b = s.rindex('</svg>', 0, s.index('<div style="position: absolute; left: 32px')) + 6
svg = s[a:b]
svg = re.sub(r'\s(width|height)="(960|600)"', '', svg, count=2)
svg = svg.replace('<svg viewBox="0 0 960 600"', '<svg viewBox="0 0 960 600" class="wsvg" preserveAspectRatio="xMidYMid slice"', 1)
ids = set(re.findall(r'\bid="([\w-]+)"', svg))
for i in sorted(ids, key=len, reverse=True):
    svg = svg.replace(f'id="{i}"', f'id="ws-{i}"').replace(f'url(#{i})', f'url(#ws-{i})')
assert svg.count('>STROKE</text>') == 1 and svg.count('>Management</text>') == 1
svg = svg.replace('>STROKE</text>', '>{{caseU}}</text>').replace('>Management</text>', '>{{secN}}</text>')
svg = svg.replace('>{{timer}}</text>', ' id="ws-timer">{{timer}}</text>', 1) if False else svg
svg = re.sub(r'(<text [^>]*)>\{\{timer\}\}</text>', r'\1 id="ws-timer">{{timer}}</text>', svg, count=1)
svg = re.sub(r'(<circle cx="75" cy="140" r="44" fill="none" stroke="url\(#ws-arc\)"[^>]*?)stroke-dashoffset="70"', r'\1stroke-dashoffset="{{arcOff}}" id="ws-parc"', svg, count=1)
assert 'id="ws-parc"' in svg and 'id="ws-timer"' in svg, 'ids'
svg = svg.replace('font-family="Caveat, cursive"', 'font-family="Caveat, \'Segoe Print\', \'Bradley Hand\', cursive"')
svg = re.sub(r'\n+', '', svg)
dc = s[s.index('const LIGHT'):s.index('const PAGES')]
lt = dc[:dc.index('function phase')]
holes = sorted(set(re.findall(r'\{\{([\w.]+)\}\}', svg)))
open('dev/tools/wscene.js', 'w').write('const WS_SVG=' + json.dumps(svg) + ';\n' + lt.replace('const LIGHT', 'const WS_LIGHT'))
print(len(svg), holes)
