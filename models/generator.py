import requests
import random

# read from added_packs.txt into list
packs_text = open('implemented_packs.txt', 'r')
packs_data = packs_text.read()
added_packs = packs_data.split('\n')

# read from nsfw_filter.txt into list
# no, you don't want to know. really.
# filter_text = open('nsfw_filter.txt', 'r')
# filter_data = packs_text.read()
# filter_triggers = packs_data.split('\n')

# def nsfw_filtered(cards):
#     for card in cards:
#         for trigger in filter_triggers:
#             if trigger in card['text']:
#                 cards.remove(card)
#     return cards

# Looking at that code you're better off just using the family edition deck, otherwise you'll be waiting all day for it to check every single one of *MINIMUM* 600 cards in the return for 117 phrases. I'm no mathematician but I'm pretty sure that's a lot of checks.

def filtered_packs_string(pack_filters):
    for i in range(len(pack_filters)):
        if '&' in pack_filters[i]:
            pack_filters[i] = pack_filters[i].replace('&', "%26")
    return ','.join(pack_filters)

def get_cards_from_api(pack_filters):
    if pack_filters:
        packs_string = filtered_packs_string(pack_filters)
        api_url = f"https://restagainsthumanity.com/api/v2/cards?packs={packs_string}"
        api_return = requests.get(api_url).json()
        return api_return
    else:
        return None

def append_saved(cards, saved_cards):
    for card in saved_cards['black']:
        cards['black'].append(card)
    for card in saved_cards['white']:
        cards['white'].append(card)
    return cards

def generate_phrase(cards):
    question_card = random.choice(cards['black'])
    phrase = question_card['text']
    answers = random.choices(cards['white'], k = question_card['pick'])
    if phrase.find('_') != -1:
        for answer in answers:
            if answer['text'].endswith('.'):
                answer = answer['text'][:-1]
            else:
                answer = answer['text']
            phrase = phrase.replace('_', answer, 1)
        return phrase
    elif phrase.endswith('?'):
        return f"{phrase}\n{answers[0]['text']}"
