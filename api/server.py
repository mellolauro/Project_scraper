from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import psycopg2
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
}

def connect():
    return psycopg2.connect(**DB_CONFIG)


@app.get('/hoteis')
def listar_hoteis(limit: int = 200):
    conn = connect()
    df = pd.read_sql(
        f"SELECT * FROM hoteis ORDER BY scraped_at DESC LIMIT {limit}",
        conn
    )
    conn.close()
    return df.to_dict(orient='records')


@app.get('/insights')
def insights_sample():
    # endpoint de exemplo que chamaria ai/insights.py
    return {
        'ok': True,
        'msg': 'Ponto de partida para gerar insights via LLM'
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
