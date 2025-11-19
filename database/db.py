# database/db.py
import time
import psycopg2
from psycopg2.extras import execute_values

DB_CONFIG = {
    'host': 'postgres',
    'port': 5432,
    'user': 'user',
    'password': 'password',
    'dbname': 'project'
}

def conectar():
    while True:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            print("Conexão com o banco realizada com sucesso!")
            return conn
        except psycopg2.OperationalError:
            print("Banco não pronto, tentando novamente em 2s...")
            time.sleep(2)

def inserir_hoteis(lista_hoteis):
    """
    Espera uma lista de dicionários com keys:
    'hotel','price','score','link','fonte'(opcional),'cidade'(opcional)
    """
    if not lista_hoteis:
        return

    conn = conectar()
    cur = conn.cursor()
    rows = []
    for h in lista_hoteis:
        rows.append((
            h.get('hotel'),
            h.get('price'),
            h.get('score'),
            h.get('link'),
            h.get('fonte'),
            h.get('cidade')
        ))

    sql = """
    INSERT INTO hoteis (nome, preco, avaliacao, link, fonte, cidade)
    VALUES %s
    """
    execute_values(cur, sql, rows)
    conn.commit()
    cur.close()
    conn.close()

def inserir_pacotes(lista_pacotes):
    """
    Espera lista de dicts com keys: 'nome','preco','link','fonte','cidade'
    """
    if not lista_pacotes:
        return

    conn = conectar()
    cur = conn.cursor()
    rows = []
    for p in lista_pacotes:
        rows.append((
            p.get('nome'),
            p.get('preco'),
            p.get('link'),
            p.get('fonte'),
            p.get('cidade')
        ))

    sql = """
    INSERT INTO pacotes (nome, preco, link, fonte, cidade)
    VALUES %s
    """
    execute_values(cur, sql, rows)
    conn.commit()
    cur.close()
    conn.close()
