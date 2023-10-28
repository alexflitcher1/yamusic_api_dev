from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser
from functools import singledispatch

class Likes(YandexResposeObject):

    uid: int
    revision: int
    tracks: list

    def get(self):
        response = self.request.get(f'/users/{self.uid}/likes/tracks')
        values = JSONParser.dislikes(response)
        super().update(**values)
        return self

    def remove(self, tracks: list):
        tracks = ','.join(tracks)
        data = {'track-ids': tracks}
        response = self.request.post(
            f'/users/{self.uid}/likes/tracks/remove',
            data=data
        )
        return self.get()

    def add_multiple(self, tracks: list):
        tracks = ','.join(tracks)
        data = {'track-ids': tracks}
        response = self.request.post(
            f'/users/{self.uid}/likes/tracks/add-multiple',
            data=data
        )
        return self.get()