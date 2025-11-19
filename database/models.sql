CREATE TABLE IF NOT EXISTS hoteis (
id SERIAL PRIMARY KEY,
nome TEXT,
preco NUMERIC,
avaliacao TEXT,
link TEXT,
fonte TEXT,
cidade TEXT,
scraped_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE IF NOT EXISTS pacotes (
id SERIAL PRIMARY KEY,
origem TEXT,
destino TEXT,
preco NUMERIC,
dias INT,
empresa TEXT,
link TEXT,
scraped_at TIMESTAMP DEFAULT NOW()
);


CREATE TABLE IF NOT EXISTS avaliacoes (
id SERIAL PRIMARY KEY,
hotel_id INT REFERENCES hoteis(id),
texto TEXT,
nota NUMERIC,
fonte TEXT,
scraped_at TIMESTAMP DEFAULT NOW()
);