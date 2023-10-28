from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser


class Similar(YandexResposeObject):

    tracks: dict
    similarTracks: dict

    def get(self):
        
        response = self.request.get(
            f'/tracks/{self.track_id}/similar'
        )
        values = JSONParser.common(response)

        
        super().update(**values)

        return self
