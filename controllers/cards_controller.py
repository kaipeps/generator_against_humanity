from flask import render_template, request, redirect
from models.card import create_new_card, get_public_cards, get_saved_cards, get_random_question, get_random_answer
from services.session_info import current_user

def index():
    return render_template('cards/index.html', current_user=current_user())

def browse():
    return render_template('cards/browse.html', current_user=current_user())

def saved():
    return render_template('cards/saved.html', current_user=current_user())

def create():
    card_text = request.form.get('text')
    tags = request.form.get('tags')
    create_new_card(card_text, tags)

def generator():
    get_random_question()
    get_random_answer()
    return render_template('cards/generator.html', current_user=current_user())
