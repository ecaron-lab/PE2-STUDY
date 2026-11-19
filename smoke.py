import os, subprocess, sys, time
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
PORT = int(os.environ.get('PORT', '8765'))
CHROME = os.environ.get('CHROME')

srv = subprocess.Popen([sys.executable, '-m', 'http.server', str(PORT)], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(1)
fails = []
try:
    with sync_playwright() as p:
        kw = {'args': ['--no-sandbox', '--autoplay-policy=no-user-gesture-required']}
        if CHROME:
            kw['executable_path'] = CHROME
        b = p.chromium.launch(**kw)
        for name, vp in [('phone', {'width': 390, 'height': 844}), ('desktop', {'width': 1280, 'height': 860})]:
            pg = b.new_page(viewport=vp)
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto(f'http://localhost:{PORT}/')
            pg.wait_for_timeout(900)
            if pg.evaluate('route()') != 'start':
                fails.append(f'{name}: app did not open on the start screen')
            pg.click('.goown')
            pg.wait_for_timeout(400)
            for r in ['cards', 'checklist', 'priority', 'piggy', 'log']:
                pg.evaluate(f"location.hash='#{r}'")
                pg.wait_for_timeout(250)
            cid = pg.evaluate('CARDS[0].id')
            pg.evaluate(f"location.hash='#case-{cid}'")
            pg.wait_for_timeout(500)
            pg.click('[data-act=writemode]')
            pg.click('[data-wm=start]')
            pg.wait_for_timeout(800)
            if not pg.evaluate("!!document.getElementById('wmscene')"):
                fails.append(f'{name}: Write mode scene missing')
            pg.click('.wmx')
            pg.click('.gtbtn')
            pg.fill('#gtin', 'smoke goal')
            pg.keyboard.press('Enter')
            pg.wait_for_timeout(300)
            if 'smoke goal' not in pg.evaluate('S.piggy.mine.map(g=>g.t).join()'):
                fails.append(f'{name}: custom goal not added')
            if errs:
                fails.append(f'{name}: page errors {errs[:3]}')
            pg.close()
        b.close()
finally:
    srv.terminate()

print('\n'.join(fails) if fails else 'smoke test passed')
sys.exit(1 if fails else 0)
