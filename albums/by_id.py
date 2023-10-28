from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser

class ById(YandexResposeObject):

    uid: int
    revision: int
    tracks: list

    def get(self):
        response = self.request.get(f'/albums/{self.album_id}')
        values = JSONParser.common(response)
        super().update(**values)
        return self