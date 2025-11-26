# scraper/cvc_scraper.py
from scraper.scraper import Scraper

async def scrape_cvc():
    s = Scraper()
    url = "https://www.cvc.com.br/hoteis/sao-paulo-sp/busca?checkin=2025-12-13&checkout=2025-12-20"

    selectors = {
        'item': 'card-hotel-item',
        'hotel': 'h3.hotel-name',
        'price': '.price-value strong', 
        'score': '.rating-score-badge',
        'link': 'a.hotel-detail-link' 
    }
    
    return await s.scrape(url, selectors, scroll=True, wait=5)