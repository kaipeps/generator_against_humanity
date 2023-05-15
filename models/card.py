from db.db import sql

def get_saved_cards(user_id):
    saved_cards = sql(f'SELECT * FROM cards INNER JOIN saves ON saved_card_id = card_id WHERE saved_user_id = {user_id}')
    return saved_cards

def create_new_card(color, text, author_id, author_name, pick, public_card):
    sql('INSERT INTO cards (color, text, author_id, author_name, pick, public_card) VALUES (%s, %s, %s, %s, %s, %s); INSERT INTO saves (saved_card_id, saved_user_id) SELECT card_id, author_id FROM cards WHERE card_id = (SELECT MAX(card_id) FROM cards) RETURNING *', [color, text, author_id, author_name, pick, public_card])

def save_card_to_user(card_id, user_id):
    sql('INSERT INTO saves (saved_card_id, saved_user_id) VALUES (%s, %s) RETURNING *', [card_id, user_id])

def edit_card(card_id, color, text, author_id, author_name, pick, public_card):
    sql('UPDATE cards SET color = %s, text = %s, author_id = %s, author_name = %s, pick = %s, public_card = %s WHERE card_id = %s RETURNING *', [color, text, author_id, author_name, pick, public_card, card_id])

def delete_card(card_id):
    sql(f'DELETE FROM cards WHERE card_id = {card_id} RETURNING *')

def remove_from_saved(user_id, card_id):
    sql(f'DELETE FROM saved WHERE user_id = {user_id} AND card_id = {card_id} RETURNING *')

def get_public_cards():
    public_cards = sql('SELECT * FROM cards WHERE public_card = TRUE')
    return public_cards
