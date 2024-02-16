from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexMusicObject
from yamusic_api.utils.parsers import JSONParser
from yamusic_api.search.search_by_text import SearchByText

class Search(YandexMusicObject):

    def __init__(self, token: str, request: Request = Request):
        self.request = Request(token=token)

    def search(self, text: str, page: int = 0, type: str = "all", nococrrect: bool = False):
        return SearchByText(
            request=self.request,
            text=text,
            page=page,
            type=type,
            nococrrect=nococrrect
        ).get()