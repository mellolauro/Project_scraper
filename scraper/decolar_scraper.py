# scraper/decolar_scraper.py
from scraper.scraper import Scraper

async def scrape_decolar():
    s = Scraper()
    url = "https://www.decolar.com/accommodations/results/CIT_6574/2025-12-13/2025-12-20/1?from=SB2&facet=city&searchId=99a87252-865b-4820-b995-fa81318f9151"  
    selectors = {
        'item': '.accommodation-card-container', 
        'hotel': '.property-name-title', 
        'price': '.price-block-total .amount',
        'score': '.rating-text .rating-number-container', 
        'link': 'a.accommodation-card-link' 
    }
    return await s.scrape(url, selectors, scroll=True, wait=3)
