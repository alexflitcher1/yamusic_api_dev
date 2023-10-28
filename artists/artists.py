from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexMusicObject
from yamusic_api.artists.tracks_ids_by_rating import TracksIdsByRating
from yamusic_api.artists.brief_info import BriefInfo
from yamusic_api.artists.direct_albums import DirectAlbums
from yamusic_api.artists.tracks import Tracks
from yamusic_api.utils.parsers import JSONParser

class Artists(YandexMusicObject):

    def __init__(self, token: str, request: Request = Request):
        self.request = Request(token=token)

    def tracks_ids_by_rating(self, artist_id: int) -> TracksIdsByRating:
        return TracksIdsByRating(
            request=self.request,
            artist_id=artist_id
        ).get()

    def brief_info(self, artist_id) -> BriefInfo:
        return BriefInfo(
            request=self.request,
            artist_id=artist_id
        ).get()

    def tracks(self, artist_id) -> Tracks:
        return Tracks(
            request=self.request,
            artist_id=artist_id
        ).get()

    def direct_albums(self, artist_id) -> DirectAlbums:
        return DirectAlbums(
            request=self.request,
            artist_id=artist_id
        ).get()

    
