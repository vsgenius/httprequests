import requests
from pprint import pprint
class Superheroapi:
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

if __name__ == '__main__':
    tokenYA = 'AQAAAAAB81f3AADLWzYPyYZ01kzYvRRoDeRxico'
    tokenSH = '2619421814940190'
    path_to_file = ['yauploader.txt','yauploder2.txt']
    print('\nHomework1\n')
    hero = Superheroapi(tokenSH)
    hero.compare_hero(['Hulk','Captain America', 'Thanos'])
    print('\nHomework2\n')
    print( 'List of file to upload:',', '.join(path_to_file))
    uploader = YaUploader(tokenYA)
    result = uploader.upload(path_to_file)