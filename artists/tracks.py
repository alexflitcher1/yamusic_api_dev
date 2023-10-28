from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser

class Tracks(YandexResposeObject):


    def get(self):
        response = self.request.get(f'/artists/{self.artist_id}/tracks')
        values = JSONParser.common(response)
        super().update(**values)
        return self