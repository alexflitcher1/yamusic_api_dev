from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser
from functools import singledispatch

class Dislikes(YandexResposeObject):

    uid: int
    revision: int
    tracks: list

    def get(self):
        response = self.request.get(f'/users/{self.uid}/dislikes/tracks')
        values = JSONParser.dislikes(response)
        super().update(**values)
        return self