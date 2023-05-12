from flask import render_template, request, redirect
from models.card import create_new_card
from services.session_info import current_user

def browse():
    return render_template('cards/browse.html', current_user=current_user())

def saved():
    return render_template('cards/saved.html', current_user=current_user())

def create(user_id):
    card_text = request.form.get('text')
    tags = request.form.get('tags')
    create_new_card(card_text, tags)
    return redirect('')

def delete():
    return redirect('')

def remove():
    return redirect('')

def generator():
    return render_template('cards/generator.html', current_user=current_user())
