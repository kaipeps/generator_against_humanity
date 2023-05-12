DROP DATABASE IF EXISTS gah_db;
CREATE DATABASE gah_db;
\c gah_db

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT,
    is_admin BOOLEAN
);

CREATE TABLE cards(
    id SERIAL PRIMARY KEY, 
    author_id INTEGER,
    color TEXT,
    text TEXT,
    pick INTEGER,
    public_card BOOLEAN,
    CONSTRAINT author_id 
        FOREIGN KEY(author_id) 
            REFERENCES users(id)
);

CREATE TABLE tags(
    card_id INTEGER,
    comedy BOOLEAN,
    fandom BOOLEAN,
    food BOOLEAN,
    tech BOOLEAN,
    weird BOOLEAN,
    inside_joke BOOLEAN,
    rude BOOLEAN,
    nsfw BOOLEAN,
    CONSTRAINT card_id 
        FOREIGN KEY(card_id) 
            REFERENCES cards(id)
);

CREATE TABLE saves(
    card_id INTEGER,
    user_id INTEGER,
    CONSTRAINT card_user_pair 
        PRIMARY KEY (user_id,card_id)
);

-- SELECT id, first_name, last_name, email, is_admin FROM users
-- SELECT id, author_id, text, pick FROM cards

-- CREATE TABLE public_data(
--     card_id PRIMARY KEY, 
--     save_count INTEGER
-- );
