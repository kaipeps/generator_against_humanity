CREATE DATABASE gah_db
\c gah_db

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password TEXT,
    cards_saved TEXT
);

CREATE TABLE cards(
    id SERIAL PRIMARY KEY, 
    author_id FOREIGN KEY REFERENCES users(id),
    color TEXT,
    text TEXT,
    pick INTEGER,
    tags TEXT,
    public_card BOOLEAN
);

CREATE TABLE public_data(
    public_key SERIAL PRIMARY KEY,
    card_id FOREIGN KEY REFERENCES cards(id),
    save_count INTEGER
);
