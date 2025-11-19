# run_all.py
import os
import json
import traceback
import asyncio
import time
from datetime import datetime

from scraper.booking_scraper import scrape_booking
from scraper.hurb_scraper import scrape_hurb
from scraper.decolar_scraper import scrape_decolar
from scraper.cvc_scraper import scrape_cvc

from database.db import inserir_hoteis, inserir_pacotes

LOG_FILE = "/app/logs/scraping.log"
os.makedirs("/app/logs", exist_ok=True)

def log(msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{timestamp}] {msg}"
    print(linha)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linha + "\n")

async def executar_scraper(nome, scraper_coro, insert_func=None):
    try:
        log(f"INICIANDO -> {nome}")
        inicio = time.time()

        # scraper_coro é uma coroutine function sem argumentos
        dados = await scraper_coro()

        duracao = round(time.time() - inicio, 2)
        if not dados:
            log(f"⚠ {nome}: Nenhum dado retornado (duração {duracao}s)")
            return

        # Inserção DB é síncrona - rodar em threadpool para não bloquear loop
        if insert_func:
            await asyncio.to_thread(insert_func, dados)

        log(json.dumps({
            "origem": nome,
            "registros": len(dados),
            "duracao_seg": duracao
        }))
        log(f"FINALIZADO -> {nome} ({len(dados)} registros)\n")

    except Exception:
        log(f"❌ ERRO NO SCRAPER: {nome}")
        log(traceback.format_exc())

async def executar_tudo():
    log("=== INÍCIO DO PIPELINE DE SCRAPING ===")
    intervalo = int(os.getenv("SCRAPER_INTERVALO", "3"))

    await executar_scraper("Booking", scrape_booking, inserir_hoteis)
    await asyncio.sleep(intervalo)

    await executar_scraper("Hurb", scrape_hurb, inserir_hoteis)
    await asyncio.sleep(intervalo)

    await executar_scraper("Decolar", scrape_decolar, inserir_pacotes)
    await asyncio.sleep(intervalo)

    await executar_scraper("CVC", scrape_cvc, inserir_pacotes)

    log("=== PIPELINE FINALIZADO ===")

if __name__ == "__main__":
    asyncio.run(executar_tudo())
