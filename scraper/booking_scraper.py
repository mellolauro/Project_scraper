# scraper/booking_scraper.py
from scraper.scraper import Scraper
import asyncio

async def scrape_booking():
    s = Scraper(timeout=40)  # Booking é mais lento → aumentar timeout

    url = (
        "https://www.booking.com/searchresults.pt-br.html"
        "?ss=S%C3%A3o+Paulo%2C+Estado+de+S%C3%A3o+Paulo%2C+Brasil"
        "&checkin=2025-12-20"
        "&checkout=2025-12-21"
        "&group_adults=1"
        "&no_rooms=1"
        "&group_children=0"
        "&order=price"
    )

    # Selectors mais estáveis (Booking troca muito)
    selectors = {
        "item": 'div[data-testid="property-card"]',
        "hotel": 'div[data-testid="title"]',
        # fallback de preço usado pelo booking em outras versões
        "price": (
            'span[data-testid="price-and-discounted-price"], '
            'span[data-testid="price-for-x-nights"]'
        ),
        "score": (
            'div[data-testid="review-score"] span, '
            'div[data-testid="review-score"]'
        ),
        "link": 'a[data-testid="title-link"]'
    }

    # Tentativas (Booking bloqueia com frequência)
    for tentativa in range(3):
        try:
            print(f"[Booking] Tentando scraping ({tentativa + 1}/3)...")
            return await s.scrape(url, selectors, scroll=True, wait=3)

        except Exception as e:
            print(f"[Booking] Erro na tentativa {tentativa + 1}: {e}")
            await asyncio.sleep(3)

    print("[Booking] Falha após 3 tentativas.")
    return []   # Evita crash do pipeline
