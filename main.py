import requests
from pprint import pprint
class Superheroapi:
    def __init__(self,token):
        self.token = token
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
            print(f'Hero name: {name} intelligence:{self.superhero_get_info(name)}')
        print(f'\nMost intelligent hero: {int_name_hero}, intelligence: {int_hero}')

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json','Authorization': f'OAuth {self.token}'}

    def get_href(self,path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        res=requests.get(url, headers=self.get_headers(), params={'path': path,'overwrite':True})
        return res.json()['href']

    def upload(self, file_path: str):
        for file in file_path:
            path = self.get_href(f'/Netology/{file}')
            res = requests.put(path, open(file,'rb'), headers=self.get_headers(),)
            if res.status_code == 201:
                print(f'File {file} success upload')

class StackUploader:
    def get_list_id(self, name_lang):
        params = {'fromdate': '1644364800', 'creation':'1644537600', 'order':'desc','sort':'activity','site':'stackoverflow'}
        url = 'https://api.stackexchange.com/2.3/questions'
        res = requests.get(url, params=params)
        data = res.json()
        name = False
        for line in data['items']:
            if name_lang.lower() in line['tags'] or name_lang.capitalize() in line['tags']:
                print(f'Questions with the {name_lang} Tag: "{line["title"]}"')
                name = True
        return f'No questions with the {name_lang} Tag' if name == False else print()

if __name__ == '__main__':
    tokenYA = 'AQAAAAAB81f3AADLWzYPyYZ01kzYvRRoDeRxico'
    tokenSH = '2619421814940190'
    path_to_file = ['yauploader.txt','yauploder2.txt']
    print('\nHomework:1\n')
    hero = Superheroapi(tokenSH)
    hero.compare_hero(['Hulk','Captain America', 'Thanos'])
    print('\nHomework:2\n')
    print( 'List of file to upload:',', '.join(path_to_file))
    uploader = YaUploader(tokenYA)
    result = uploader.upload(path_to_file)
    print('\nHomework:3\n')
    stack = StackUploader()
    stack.get_list_id('Python')

