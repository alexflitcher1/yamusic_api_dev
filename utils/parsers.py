import json
from yamusic_api.utils import parser
import xml.etree.ElementTree as ET
from hashlib import md5
from yamusic_api.yandex_music import YandexMusicError

SIGN_SALT = 'XGRlBW9FXlekgbPrRHuSiA'


class JSONParser(parser.Parser):

    @staticmethod
    def status(json):
        json['result']['account']['passportPhones'] = json['result']['account']['passport-phones']
        del json['result']['account']['passport-phones']
        return json['result']['account']

    @staticmethod
    def common(json):
        return json['result']

    @staticmethod
    def dislikes(json):
        return json['result']['library']

    def uid(self, json):
        return json['result']['account']['uid']

    def track_id(self, json, start=0, stop=None):
        if stop is None: stop=int(len(json['result']['library']['tracks']))
        ids = []
        for i in range(start, stop):
            ids.append(json['result']['library']['tracks'][i]['id'])
        
        return ids 

    def download_url(self, json):
        return json['result'][0]['downloadInfoUrl']

    @staticmethod
    def artists(artist):
        artists = []
        for arts in artist:
            artists.append(arts['name'])
        return artists
    
    def titles(self, json):
        titles = []
        for tracks in json['result']:
            titles.append(tracks['title'])
        return titles

class XMLParser(parser.Parser):
    def download_url_data(self, xml):
        tree = ET.fromstring(xml)

        host = tree.find('host').text
        path = tree.find('path').text
        ts = tree.find('ts').text
        region = tree.find('region').text
        s = tree.find('s').text


        sign = md5((SIGN_SALT + path[1::] + s).encode('utf-8')).hexdigest()

        data = {'host': host, 'path': path, 'ts': ts, 'region': region, 's': s, 'sign': sign}

        return data