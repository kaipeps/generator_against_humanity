from flask import render_template, request, redirect
from models.card import get_saved_cards, create_new_card, edit_card, delete_card, remove_from_saved, get_public_cards
from models.user import generate_author_name
from services.session_info import current_user

def saved(user_id):
    saved_cards = get_saved_cards(user_id)
    return render_template('cards/saved.html', current_user = current_user(), cards = saved_cards)

def create(user_id):
    author_name = generate_author_name(user_id)
    color = request.form.get('color')
    text = request.form.get('text')
    pick = request.form.get('pick')
    public_card = request.form.get('public')
    create_new_card(color, text, user_id, author_name, pick, public_card)
    return redirect(f'/cards/saved/{user_id}')

def edit(card_id):
    color = request.form.get('color')
    text = request.form.get('text')
    pick = request.form.get('pick')
    public_card = request.form.get('public')
    edit_card(card_id, color, text, pick, public_card)
    user = current_user()
    return redirect(f"/cards/saved/{user['id']}")

def delete(card_id):
    delete_card(card_id)
    user = current_user()
    return redirect(f"/cards/saved/{user['id']}")

def remove(user_id, card_id):
    remove_from_saved(user_id, card_id)
    return redirect(f'/cards/saved/{user_id}')

def browse():
    public_cards = get_public_cards()
    return render_template('cards/index.html', cards = public_cards, current_user = current_user())

def generator():
    return render_template('cards/generator.html', current_user = current_user())
