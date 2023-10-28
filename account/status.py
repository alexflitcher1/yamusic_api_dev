from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser


class Status(YandexResposeObject):

    uid: int
    now: str
    login: str
    region: int
    fullName: str
    secondName: str
    firstName: str
    displayName: str
    serviceAvailable: bool
    hostedUser: bool
    passportPhones: list
    registeredAt: str
    child: bool
    nonOwnerFamilyMember: bool

    def get(self):
        response = self.request.get('/account/status')
        values = JSONParser.status(response)
        super().update(**values)
        return self