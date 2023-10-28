from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeObject
from yamusic_api.utils.parsers import JSONParser


class DownloadInfo(YandexResposeObject):

    codec: str
    gain: bool
    downloadInfoUrl: str
    direct: bool
    bitrateInKbps: int

    def get(self):
        
        response = self.request.get(
            f'/tracks/{self.track_id}/download-info'
        )
        values = JSONParser.common(response)[0]
        super().update(**values)

        return self
