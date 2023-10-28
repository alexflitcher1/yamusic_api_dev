from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeListObject
from yamusic_api.utils.parsers import JSONParser


class TrackIds(YandexResposeListObject):

    albums: list[dict]
    artists: list[dict]
    available: bool
    availableForPremiumUsers: bool
    availableFullWithoutPermission: bool
    coverUri: str
    durationMs: int
    fileSize: int
    id: str
    lyricsAvailable: bool
    major: dict
    normalization: dict
    ogImage: str
    previewDurationMs: int
    realId: str
    rememberPosition: bool
    storageDir: str
    title: str
    type: str

    def get(self):
        
        data = {
            'track-ids': self.track_ids, 
            'with-positions': self.with_positions
        }
        response = self.request.post('/tracks', data=data)
        values = JSONParser.common(response)
        to_ret = self.de_json(values)
        self._result = to_ret

        return self
