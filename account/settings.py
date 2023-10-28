from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser


class Settings(YandexResposeObject):

    uid: int
    lastFmScrobblingEnabled: bool
    facebookScrobblingEnabled: bool
    shuffleEnabled: bool
    addNewTrackOnPlaylistTop: bool
    volumePercents: int
    userMusicVisibility: str
    userSocialVisibility: str
    serviceAvailable: bool
    adsDisabled: bool
    modified: str
    rbtDisabled: str
    theme: str
    promosDisabled: bool
    autoPlayRadio: bool
    syncQueueEnabled: bool
    explicitForbidden: bool
    childModEnabled: bool
    wizardIsPassed: bool

    def get(self):
        response = self.request.get('/account/settings')
        values = JSONParser.common(response)
        super().update(**values)
        return self

    def save(self, *args, **kwargs):
        self.request.post('/account/settings', kwargs)
        super().update(**kwargs)
        return self

