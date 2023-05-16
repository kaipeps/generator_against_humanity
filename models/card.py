from db.db import sql

def get_saved_cards(user_id):
    saved_cards = sql(f'SELECT * FROM cards INNER JOIN saves ON saved_card_id = card_id WHERE saved_user_id = {user_id}')
    return saved_cards

def create_new_card(color, text, author_id, author_name, pick, public_card):
    sql('INSERT INTO cards (color, text, author_id, author_name, pick, public_card) VALUES (%s, %s, %s, %s, %s, %s); INSERT INTO saves (saved_card_id, saved_user_id) SELECT card_id, author_id FROM cards WHERE card_id = (SELECT MAX(card_id) FROM cards) RETURNING *', [color, text, author_id, author_name, pick, public_card])

def get_card_by_id(card_id):
    cards = sql(f'SELECT * FROM cards WHERE card_id = {card_id}')
    return cards[0]

def edit_card(color, text, pick, public_card, card_id):
    sql('UPDATE cards SET color = %s, text = %s, pick = %s, public_card = %s WHERE card_id = %s RETURNING *', [color, text, pick, public_card, card_id])

def delete_card(card_id):
    sql(f'DELETE FROM cards WHERE card_id = {card_id} RETURNING *')

def remove_from_saved(user_id, card_id):
    sql(f'DELETE FROM saved WHERE user_id = {user_id} AND card_id = {card_id} RETURNING *')

def get_saves(user_id):
    saves = sql(f'SELECT saved_card_id FROM saves WHERE saved_user_id = {user_id}')
    saved_card_ids = []
    for save in saves:
        saved_card_ids.append(save['saved_card_id'])
    return saved_card_ids

def get_public_cards():
    public_cards = sql('SELECT * FROM cards WHERE public_card = TRUE ORDER BY card_id')
    return public_cards

def save_card_to_user(card_id, user_id):
    sql('INSERT INTO saves (saved_card_id, saved_user_id) VALUES (%s, %s) RETURNING *', [card_id, user_id])

def get_saved_black_cards(user_id):
    saved_black_cards = sql(f"SELECT text, author_name, pick FROM cards INNER JOIN saves ON saved_card_id = card_id WHERE color = 'black' AND saved_user_id = {user_id}")
    return saved_black_cards

def get_saved_white_cards(user_id):
    saved_white_cards = sql(f"SELECT text, author_name, pick FROM cards INNER JOIN saves ON saved_card_id = card_id WHERE color = 'white' AND saved_user_id = {user_id}")
    return saved_white_cards
