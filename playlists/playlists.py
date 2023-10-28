from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexMusicObject
from yamusic_api.playlists.list import List
from yamusic_api.utils.parsers import JSONParser

class Playlists(YandexMusicObject):

    def __init__(self, token: str, request: Request = Request):
        self.request = Request(token=token)

    def list(self, uids: list, kinds: list) -> List:
        return List(
            request=self.request,
            uids=uids,
            kinds=kinds
        ).get()