# similar approach: navegar na página do hotel e coletar textos de avaliações
from playwright.sync_api import sync_playwright
import time


def scrape_reviews(hotel_url, limit=50):
    p = sync_playwright().start()
browser = p.chromium.launch(headless=True)
page = browser.new_page()
page.goto(hotel_url)
time.sleep(3)


reviews = []
# Seletores variam por site; aqui é um esqueleto
nodes = page.query_selector_all('.review_comment')
for i, n in enumerate(nodes):
    if i >= limit: break
try:
    text = n.inner_text().strip()
except:
    text = None
reviews.append(text)


browser.close()
p.stop()
#return reviews