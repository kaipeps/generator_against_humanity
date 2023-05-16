from flask import render_template, request
from models.generator import added_packs, get_cards_from_api, append_saved, generate_phrase
from models.card import get_saved_black_cards, get_saved_white_cards
from services.session_info import current_user

# read from pack_labels.txt into list
packs_text = open('pack_labels.txt', 'r')
packs_data = packs_text.read()
pack_labels = packs_data.split('\n')

def new():
    return render_template('generator/new.html', packs = added_packs, labels = pack_labels, current_user = current_user())

def result():
    pack_filters = request.form.getlist('filter')
    include_saved = request.form.get('saved-cards')
    api_cards = get_cards_from_api(pack_filters)
    print(include_saved)
    if include_saved == 'true':
        user = current_user()
        saved_cards = {'black': get_saved_black_cards(user['user_id']), 'white': get_saved_white_cards(user['user_id'])}
        if api_cards:
            all_cards = append_saved(api_cards, saved_cards)
        else:
            all_cards = saved_cards
        phrase = generate_phrase(all_cards)
    elif api_cards:
        phrase = generate_phrase(api_cards)
    else:
        all_cards = None
        phrase = "You didn't select any packs! Go back and try again"
    return render_template('generator/result.html', phrase = phrase, current_user = current_user())

def surprise():
    api_cards = get_cards_from_api(added_packs)
    user = current_user()
    if user:
        saved_cards = {'black': get_saved_black_cards(user['user_id']), 'white': get_saved_white_cards(user['user_id'])}
        all_cards = append_saved(api_cards, saved_cards)
        phrase = generate_phrase(all_cards)
    else:
        phrase = generate_phrase(api_cards)
    return render_template('generator/result.html', phrase = phrase, current_user = current_user())
