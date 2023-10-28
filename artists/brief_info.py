from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser

class BriefInfo(YandexResposeObject):

    artist: dict
    albums: list
    alsoAlbums: list
    lastReleaseIds: list
    popularTracks: list[dict]
    bandlinkScannerLink: dict
    similarArtists: list
    allCovers: list
    concerts: list
    videos: list
    clips: list
    vinyls: list
    hasPromotions: bool
    lastReleases: list
    stats: dict
    customWave: dict
    playlistIds: list
    playlists: list

    def get(self):
        response = self.request.get(f'/artists/{self.artist_id}/brief-info')
        values = JSONParser.common(response)
        super().update(**values)
        return self