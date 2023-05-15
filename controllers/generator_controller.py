from flask import render_template, request
from models.generator import added_packs, get_cards_from_api, append_saved, generate_phrase
from models.card import get_saved_cards, get_saved_black_cards, get_saved_white_cards
from services.session_info import current_user

def new():
    return added_packs
    return render_template('generator/new.html', packs = added_packs)

def result():
    pack_filters = request.form.getlist('filter')
    api_cards = get_cards_from_api(pack_filters)
    user = current_user()
    if current_user():
        if api_cards:
            saved_cards = get_saved_cards(user['user_id'])
            all_cards = append_saved(api_cards, saved_cards)
        else: 
            all_cards = {'black': get_saved_black_cards(user['user_id']), 'white': get_saved_white_cards(user['user_id'])}
    phrase = generate_phrase(all_cards)
    return render_template('generator/result.html', phrase = phrase, current_user = current_user())