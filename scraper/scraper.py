import asyncio
from playwright.async_api import async_playwright

class Scraper:
        def __init__(self, timeout=10):
                self.timeout = timeout

        async def scrape(self, url, selectors, scroll=False, wait=0):
                async with async_playwright() as p:
                        browser = await p.chromium.launch(headless=True)
                        page = await browser.new_page()

                        await page.goto(url, timeout=self.timeout * 1000)

                        if scroll:
                                await page.evaluate("window.scrollBy(0, document.body.scrollHeight);")

                        if wait:
                                await page.wait_for_timeout(wait * 1000)

                        items = await page.query_selector_all(selectors["item"])
                        results = []

                        for item in items:
                                hotel_el = await item.query_selector(selectors.get("hotel"))
                                price_el = await item.query_selector(selectors.get("price"))
                                score_el = await item.query_selector(selectors.get("score"))
                                link_el = await item.query_selector(selectors.get("link"))

                results.append({
                        "hotel": await hotel_el.inner_text() if hotel_el else None,
                        "price": await price_el.inner_text() if price_el else None,
                        "score": await score_el.inner_text() if score_el else None,
                        "link": await link_el.get_attribute("href") if link_el else None
                })

                await browser.close()
                return results
