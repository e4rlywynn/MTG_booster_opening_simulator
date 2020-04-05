import requests
import json
import random

s = requests.Session()
all_cards = s.get('https://www.mtgjson.com/files/AllPrintings.json').json()

mtg_set = 'M20' # here we select MTG set name from AllPrintings file by MTGJSON community
quality = 'normal' # card image quality in accordance to scryfall.com API, 'small', 'normal', 'large', or 'png'

set_cards = all_cards[mtg_set]['cards']

common_cards = []
uncommon_cards = []
rare_mythic_cards = []
lands = []
tokens = []

for set_card in set_cards:
    
    if set_card['supertypes'] == ['Basic']:
        lands.append(set_card['scryfallId'])

    elif set_card['rarity'] == 'common':
        common_cards.append(set_card['scryfallId'])
        
    elif set_card['rarity'] == 'uncommon':
        uncommon_cards.append(set_card['scryfallId'])
        
    else:
        rare_mythic_cards.append(set_card['scryfallId'])
        
for token in all_cards[mtg_set]['tokens']:
    
    tokens.append(token['scryfallId'])
        
common_cards_imgs = [s.get(f'https://api.scryfall.com/cards/{scry_id}').json()['image_uris'][quality]
                     for scry_id in tqdm_notebook(common_cards)]

uncommon_cards_imgs = [s.get(f'https://api.scryfall.com/cards/{scry_id}').json()['image_uris'][quality]
                     for scry_id in tqdm_notebook(uncommon_cards)]

rare_mythic_cards_imgs = [s.get(f'https://api.scryfall.com/cards/{scry_id}').json()['image_uris'][quality]
                     for scry_id in tqdm_notebook(rare_mythic_cards)]

lands_imgs = [s.get(f'https://api.scryfall.com/cards/{scry_id}').json()['image_uris'][quality]
                     for scry_id in tqdm_notebook(lands)]

tokens_imgs = [s.get(f'https://api.scryfall.com/cards/{scry_id}').json()['image_uris'][quality]
                     for scry_id in tqdm_notebook(tokens)]
                     
booster = random.sample(lands_imgs, 1) +\
            random.sample(tokens_imgs, 1) +\
            random.sample(common_cards_imgs, 10) +\
            random.sample(uncommon_cards_imgs, 3) +\
            random.sample(rare_mythic_cards_imgs, 1)
            
