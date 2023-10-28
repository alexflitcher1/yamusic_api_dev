from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser


class Supplement(YandexResposeObject):

    id: int
    lyrics: dict
    videos: dict
    radioIsAvailable: bool
    description: str

    def get(self):
        
        response = self.request.get(
            f'/tracks/{self.track_id}/supplement'
        )
        values = JSONParser.common(response)

        if 'lyrics' not in values.keys(): values['lyrics'] = {}
        if 'videos' not in values.keys(): values['videos'] = {}
        
        if 'description' not in values.keys():
            values['description'] = ''

        if 'radioIsAvailable' not in values.keys(): 
            values['radioIsAvailable'] = False
        
        super().update(**values)

        return self
