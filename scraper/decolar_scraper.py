# scraper/decolar_scraper.py
from scraper.scraper import Scraper

async def scrape_decolar():
    s = Scraper()
    url = "https://www.decolar.com/hotels/results"  # ajuste conforme pagina correta
    selectors = {
        'item': '.property-card',   # selectors de exemplo — ajuste conforme site
        'hotel': '.property-card__title',
        'price': '.price-amount',
        'score': '.review-score',
        'link': 'a'
    }
    return await s.scrape(url, selectors, scroll=True, wait=3)
