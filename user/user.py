from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexMusicObject
from yamusic_api.user.playlists import Playlists
from yamusic_api.user.dislikes import Dislikes
from yamusic_api.user.likes import Likes
from yamusic_api.utils.parsers import JSONParser

class User(YandexMusicObject):

    def __init__(self, uid: int, token: str, request: Request = Request):
        self.request = Request(token=token)
        self.uid = uid

    def playlists(self, fastMode: bool = True, kinds: list = [], 
    mixed: bool = False, rich_tracks: bool = False) -> Playlists:
        return Playlists(
            kinds=kinds, 
            mixed=mixed, 
            rich_tracks=False, 
            request=self.request, 
            uid=self.uid, 
            fastMode=fastMode
        ).get()

    def dislikes(self) -> Dislikes:
        return Dislikes(
            uid=self.uid,
            request=self.request
        ).get()

    def likes(self) -> Likes:
        return Likes(
            uid=self.uid,
            request=self.request
        ).get()