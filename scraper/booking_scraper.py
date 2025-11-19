# scraper/booking_scraper.py
from scraper.scraper import Scraper

async def scrape_booking():
    s = Scraper()
    url = "https://www.booking.com/searchresults.pt-br.html?ss=Rio+de+Janeiro"
    selectors = {
        'item': 'div[data-testid="property-card"]',
        'hotel': 'div[data-testid="title"]',
        'price': 'span[data-testid="price-and-discounted-price"]',
        'score': 'div[data-testid="review-score"]',
        'link': 'a'
    }
    return await s.scrape(url, selectors, scroll=True, wait=4)
