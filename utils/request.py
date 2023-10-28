import requests
import urllib.request

import json

from yamusic_api.utils.parsers import XMLParser
from yamusic_api.yandex_music import YandexMusicError


HEADERS = {'X-Yandex-Music-Client': 'YandexMusicAndroid/24023231', 'User-Agent': 'Yandex-Music-API'}

API_URL = 'https://api.music.yandex.net'

class Request:

    def __init__(self, headers=None, token=None, api=API_URL):
        if headers is None:
             self._headers = HEADERS.copy()
        else:
            self._headers = headers
        
        self.api = api
        self._token = token
        self._headers['Authorization'] = f'OAuth {self._token}'
    

    def get(self, urn: str, params=None):
        if urn[0] != '/':
            url = self.api + '/' + urn
        else:
            url = self.api + urn
        
        return DeJson.de_json(
            requests.request(
                'GET', 
                url, 
                params=params, 
                headers=self._headers
            ).content,
            urn=urn
        )

    def post(self, urn: str, data=None):
        if urn[0] != '/':
            url = self.api + '/' + urn
        else:
            url = self.api + urn

        return DeJson.de_json(
            requests.request(
                'POST', 
                url, 
                headers=self._headers, 
                data=data
            ).content,
            urn=urn
        )

    def download_mp3(self, name: str, url: str):
        xml = XMLParser()
        xmlFile = self._get_xml(url)

        data = xml.download_url_data(xmlFile)

        url = f'https://{data["host"]}/get-mp3/{data["sign"]}/{data["ts"]}{data["path"]}'

        self._download(url, name)

    def _get_xml(self, url: str):
        return requests.get(url).content.decode()

    def de_json(self, data: str):
        return json.loads(data)
    
    def _download(self, url: str, name: str):
        urllib.request.urlretrieve(url, name)


class DeJson:
    
    @staticmethod
    def de_json(data, urn=''):
        data = json.loads(data)
        if urn != '/token':
            if 'result' not in data.keys():
                raise YandexMusicError(f"({data['error']['name']}) {data['error']['message']}")

        return data