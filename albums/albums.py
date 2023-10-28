from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexMusicObject
from yamusic_api.albums.album_data import AlbumData
from yamusic_api.albums.with_tracks import WithTracks
from yamusic_api.albums.by_id import ById
from yamusic_api.utils.parsers import JSONParser

class Albums(YandexMusicObject):

    def __init__(self, token: str, request: Request = Request):
        self.request = Request(token=token)

    def albums(self, album_ids: list) -> AlbumData:
        return AlbumData(
            request=self.request,
            album_ids=album_ids
        ).get()

    def with_tracks(self, album_id: int) -> WithTracks:
        return WithTracks(
            request=self.request,
            album_id=album_id
        ).get()

    def by_id(self, album_id: int) -> ById:
        return ById(
            request=self.request,
            album_id=album_id
        ).get()