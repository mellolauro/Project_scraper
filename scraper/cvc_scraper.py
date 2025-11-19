# scraper/cvc_scraper.py
from scraper.scraper import Scraper

async def scrape_cvc():
    s = Scraper()
    url = "https://www.cvc.com.br/hoteis"  # ajustar se necessário
    selectors = {
        'item': '.hotel-item',   # selectors de exemplo — ajuste conforme site
        'hotel': '.hotel-item__name',
        'price': '.hotel-item__price',
        'score': '.rating',
        'link': 'a'
    }
    return await s.scrape(url, selectors, scroll=True, wait=3)
