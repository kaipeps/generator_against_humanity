DROP DATABASE IF EXISTS gah_db;
CREATE DATABASE gah_db;
\c gah_db

CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    password_digest TEXT,
    is_admin BOOLEAN
);

CREATE TABLE cards(
    card_id SERIAL PRIMARY KEY, 
    color TEXT,
    text TEXT,
    author_id INTEGER,
    author_name TEXT,
    pick INTEGER,
    public_card BOOLEAN,
    CONSTRAINT author_id 
        FOREIGN KEY(author_id) 
        REFERENCES users(user_id)
        ON DELETE CASCADE
);

CREATE TABLE saves(
    saved_card_id INTEGER,
    saved_user_id INTEGER,
    CONSTRAINT card_user_pair 
        PRIMARY KEY (saved_card_id,saved_user_id),
    CONSTRAINT card_ref
        FOREIGN KEY(saved_card_id) 
        REFERENCES cards(card_id)
        ON DELETE CASCADE,
    CONSTRAINT user_ref
        FOREIGN KEY(saved_user_id) 
        REFERENCES users(user_id)
        ON DELETE CASCADE
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
    CONSTRAINT card_ref
        FOREIGN KEY(card_id) 
        REFERENCES cards(card_id)
        ON DELETE CASCADE
);

-- SELECT id, first_name, last_name, email, is_admin FROM users
-- SELECT id, author_id, text, pick FROM cards

-- CREATE TABLE public_data(
--     card_id PRIMARY KEY, 
--     save_count INTEGER
-- );
