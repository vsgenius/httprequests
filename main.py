import requests
from pprint import pprint
class superheroapi:
    def __init__(self,token):
        self.token = token
    pass
    def superhero_get_info(self,name):
        url = f'https://superheroapi.com/api/{self.token}/search/{name}'
        res = requests.get(url)
        return int(res.json()['results'][0]['powerstats']['intelligence'])

    def compare_hero(self, list_hero):
        int_hero = 0
        for name in list_hero:
            if self.superhero_get_info(name)> int_hero:
                int_hero = self.superhero_get_info(name)
                int_name_hero = name
            print(f'Герой: {name} интеллект:{self.superhero_get_info(name)}')
        print(f'\nСамый умный герой: {int_name_hero}, интеллект: {int_hero}')

if __name__ == '__main__':
    hero = superheroapi('2619421814940190')
    hero.compare_hero(['Hulk','Captain America', 'Thanos'])
