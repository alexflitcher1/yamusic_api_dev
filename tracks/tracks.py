from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexMusicObject
from yamusic_api.tracks.track_ids import TrackIds
from yamusic_api.tracks.download_info import DownloadInfo
from yamusic_api.tracks.supplement import Supplement
from yamusic_api.tracks.similar import Similar
from yamusic_api.tracks.lyrics import Lyrics
from yamusic_api.utils.parsers import JSONParser

class Tracks(YandexMusicObject):

    def __init__(self, token: str, request: Request = Request):
        self.request = Request(token=token)

    def tracks(self, track_ids: list, 
    with_positions: bool = False) -> TrackIds:
        return TrackIds(
            request=self.request,
            track_ids=track_ids,
            with_positions=with_positions
        ).get()

    def download_info(self, track_id: int) -> DownloadInfo:
        return DownloadInfo(
            request=self.request, 
            track_id=track_id
        ).get()

    def supplement(self, track_id: int) -> Supplement:
        return Supplement(
            request=self.request,
            track_id=track_id
        ).get()

    def similar(self, track_id: int) -> Similar:
        return Similar(
            request=self.request,
            track_id=track_id
        ).get()

    def lyrics(self, track_id: int, format: str = 'LRC') -> Lyrics:
        pass

    
    