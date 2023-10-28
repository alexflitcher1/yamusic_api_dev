from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexMusicObject
from yamusic_api.account.status import Status
from yamusic_api.account.settings import Settings 
from yamusic_api.utils.parsers import JSONParser

class Account(YandexMusicObject):

    def __init__(self, token: str, request: Request = Request):
        self.request = Request(token=token)

    def status(self) -> Status:
        return Status(request=self.request).get()
    
    def settings(self) -> Settings:
        return Settings(request=self.request).get()
