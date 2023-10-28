from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeListObject
from yamusic_api.utils.parsers import JSONParser


class AlbumData(YandexResposeListObject):

    id: int
    title: str
    metaType: str
    year: int
    releaseDate: str
    coverUri: str
    ogImage: str
    genre: str
    trackCount: int
    recent: bool
    veryImportant: bool
    artists: list[dict]
    labels: list[dict]
    available: bool
    availableForPremiumUsers: bool
    availableForMobile: bool
    availablePartially: bool
    bests: list

    def get(self):
        
        album_ids = ','.join(self.album_ids)

        data = {
            'album-ids': album_ids, 
        }

        response = self.request.post('/albums', data=data)

        values = JSONParser.common(response)
        to_ret = self.de_json(values)
        
        self._result = to_ret

        return self
