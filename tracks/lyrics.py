from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser


class Lyrics(YandexResposeObject):

    def get(self):
        
        params = {
            'timeStamp': self.time_stamp,
            'format': self.format,
            'sign': self.sign
        }

        response = self.request.get(
            f'/tracks/{self.track_id}/lyrics',
            params=params
        )
        values = JSONParser.common(response)

        
        super().update(**values)

        return self
