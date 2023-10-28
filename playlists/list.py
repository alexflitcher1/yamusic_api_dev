from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeListObject
from yamusic_api.utils.parsers import JSONParser


class List(YandexResposeListObject):

    def get(self):
        
        playlist_ids = []

        for i in range(len(self.kinds)):
            playlist_ids.append(f'{self.uids[i]}:{self.kinds[i]}')

        data = {
            'playlistIds': playlist_ids, 
        }

        response = self.request.post('/playlists/list', data=data)

        values = JSONParser.common(response)
        to_ret = self.de_json(values)
        
        self._result = to_ret

        return self
