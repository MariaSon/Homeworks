import requests


url = 'https://superheroapi.com/api/2619421814940190/search/'

heroes_dict = {}


def cleverest_hero(heroes):
    for hero in heroes:
        href = url + hero
        info_heroes = requests.get(href).json()
        for k, v in info_heroes.items():
            if k == 'results':
                for elements in v:
                    for key, value in elements.items():
                        if key == 'powerstats':
                            for stats, num in value.items():
                                if stats == 'intelligence':
                                    heroes_dict[hero] = num
    print(f'{max(heroes_dict)} - is the most intelligence')


cleverest_hero(['Hulk', 'Captain_America', 'Thanos'])




