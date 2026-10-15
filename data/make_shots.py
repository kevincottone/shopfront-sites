import asyncio, os, glob
from playwright.async_api import async_playwright
from PIL import Image
import sys
root=sys.argv[1] if len(sys.argv)>1 else "/home/claude/shopfront-sites"
slugs=sorted(os.path.basename(os.path.dirname(p)) for p in glob.glob(f"{root}/preview/*/index.html"))
os.makedirs(f"{root}/shots",exist_ok=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for s in slugs:
            pg=await b.new_page(viewport={"width":390,"height":780},device_scale_factor=2)
            await pg.goto(f"file://{root}/preview/{s}/index.html"); await pg.wait_for_timeout(900)
            # hide the preview banner so the shot looks like a real site
            await pg.add_style_tag(content="[class*=preview-banner],[class*=banner],.pv-banner,.preview-note{display:none!important}")
            await pg.wait_for_timeout(200)
            out=f"{root}/shots/{s}.png"
            await pg.screenshot(path=out,clip={"x":0,"y":0,"width":390,"height":780})
            im=Image.open(out); im.save(out,optimize=True)
            await pg.close()
        await b.close()
    print(len(slugs),"shots")
asyncio.run(main())
