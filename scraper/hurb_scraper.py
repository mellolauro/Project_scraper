# scraper/hurb_scraper.py
from scraper.scraper import Scraper

async def scrape_hurb():
    s = Scraper()
    url = "https://www.hurb.com/br/hotels/rio-de-janeiro"  # ajuste se necessário
    selectors = {
        'item': '.hotel-card',             # exemplo genérico — ajuste conforme real site
        'hotel': '.hotel-card__name',
        'price': '.hotel-card__price',
        'score': '.hotel-card__rating',
        'link': 'a'
    }
    return await s.scrape(url, selectors, scroll=True, wait=3)
