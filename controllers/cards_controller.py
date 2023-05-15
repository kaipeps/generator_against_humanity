from flask import render_template, request, redirect
from models.card import get_saved_cards, create_new_card, save_card_to_user, get_card_by_id, edit_card, delete_card, remove_from_saved, get_public_cards
from models.user import generate_author_name
from services.session_info import current_user

def saved(user_id):
    saved_cards = get_saved_cards(user_id)
    return render_template('cards/saved.html', current_user = current_user(), cards = saved_cards)

def new():
    return render_template('cards/new.html', current_user = current_user())

def create(user_id):
    author_name = generate_author_name(user_id)
    color = request.form.get('color')
    text = request.form.get('text')
    pick = request.form.get('pick')
    public_card = request.form.get('public')
    create_new_card(color, text, user_id, author_name, pick, public_card)
    return redirect(f'/cards/saved/{user_id}')

def edit(card_id):
    card = get_card_by_id(card_id)
    return render_template('cards/edit.html', card = card, current_user = current_user())

def update(card_id):
    color = request.form.get('color')
    text = request.form.get('text')
    pick = request.form.get('pick')
    public_card = request.form.get('public')
    edit_card(color, text, pick, public_card, card_id)
    current = current_user()
    return redirect(f"/cards/saved/{current['user_id']}")

def delete(card_id):
    delete_card(card_id)
    current = current_user()
    return redirect(f"/cards/saved/{current['user_id']}")

def remove(user_id, card_id):
    remove_from_saved(user_id, card_id)
    return redirect(f'/cards/saved/{user_id}')

def browse():
    public_cards = get_public_cards()
    return render_template('cards/index.html', cards = public_cards, current_user = current_user())

def save(card_id):
    current = current_user()
    save_card_to_user(card_id, current['user_id'])
    return redirect('/cards/browse')
