import asyncio
from playwright.async_api import async_playwright

class Scraper:
        def __init__(self, timeout=30):
                self.timeout = timeout

        async def _launch_browser(self, p):
                browser = await p.chromium.launch(
                headless=True,
                args=[
                "--disable-gpu",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-setuid-sandbox",
                "--no-zygote"
                ]
        )
                context = await browser.new_context()
                page = await context.new_page()
                return browser, context, page

        async def scrape(self, url, selectors, scroll=False, wait=3):
                async with async_playwright() as p:
                        browser, context, page = await self._launch_browser(p)

                        await page.goto(url, timeout=self.timeout * 1000)
                        await page.wait_for_timeout(wait * 1000)


                        if scroll:
                                await page.evaluate("""
                                        new Promise(resolve => {
                                        let totalHeight = 0;
                                        const distance = 500;
                                        const timer = setInterval(() => {
                                        window.scrollBy(0, distance);
                                        totalHeight += distance;
                                        if (totalHeight >= document.body.scrollHeight) {
                                        clearInterval(timer);
                                        resolve();
                                        }
                                }, 200);
                        });
                        """)

                items = await page.query_selector_all(selectors['item'])
                results = []

                for item in items:
                        try:
                                hotel = await item.query_selector(selectors['hotel'])
                                hotel = await hotel.inner_text() if hotel else None

                                price = await item.query_selector(selectors['price'])
                                price = await price.inner_text() if price else None

                                score = await item.query_selector(selectors['score'])
                                score = await score.inner_text() if score else None

                                link = await item.query_selector(selectors['link'])
                                link = await link.get_attribute("href") if link else None

                                results.append({
                                        "hotel": hotel,
                                        "price": price,
                                        "score": score,
                                        "link": link
                                })
                        except Exception as e:
                                print("Erro no item:", e)
                                continue

                        await browser.close()
                        return results
