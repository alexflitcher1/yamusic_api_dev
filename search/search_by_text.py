from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser

class SearchByText(YandexResposeObject):


    def get(self):
        params = {
            'text': self.text,
            'page': self.page,
            'type': self.type,
            'nococrrect': self.nococrrect
        }
        response = self.request.get(f'/search', params=params)
        values = JSONParser.common(response)
        super().update(**values)
        return self