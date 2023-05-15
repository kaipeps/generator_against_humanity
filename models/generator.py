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

def filtered_packs_string(packs_filter = []):
    selected = []
    for i in range(len(added_packs)):
        if packs_filter[i]:
            if '&' in added_packs[i]:
                selected.append(added_packs[i].replace('&', "%26"))
            else:
                selected.append(added_packs[i])
    return ','.join(selected)

def get_cards_from_api(packs_filter):
    if any(packs_filter):
        packs_string = filtered_packs_string(packs_filter)
        api_return = requests.get(f"https://restagainsthumanity.com/api/v2/cards?packs={packs_string}&color=black")
        return api_return
    else:
        return None

def append_saved(cards, saved_cards):
    for card in saved_cards:
        if card['color'] == 'black':
            del card['color']
            cards['black'].append(card)
        elif card['color'] == 'white':
            del card['color']
            cards['white'].append(card)
    return cards

def generate_phrase(cards):
    question_card = random.choice(cards['black'])
    phrase = question_card['text']
    answers = random.choices(cards['white'], question_card['pick'])
    if '_' in phrase:
        for answer in answers:
            if answer['text'].endswith('.'):
                answer = answer['text'][:-1]
            phrase.replace('_', answer)
        return phrase
    elif phrase.endswith('?'):
        return f"{phrase}<br>{answers[0]['text']}"
