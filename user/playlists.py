from yamusic_api.utils.request import Request
from yamusic_api.yandex_music import YandexResposeListObject
from yamusic_api.utils.parsers import JSONParser
from functools import singledispatch

class Playlists(YandexResposeListObject):

    playlistUuid: str
    available: bool
    collective: bool
    cover: dict
    created: str
    customWave: dict
    durationMs: int
    isBanner: bool
    isPremiere: bool
    kind: int
    likesCount: int
    modified: str
    ogImage: str
    owner: dict
    pager: dict
    revision: int
    snapshot: int
    tags: list
    title: str
    trackCount: int
    tracks: list
    uid: int
    visibility: bool

    def get(self):
        if self.fastMode:
            if not len(self.kinds):
                response = self.request.get(
                    f'/users/{self.uid}/playlists/list'
                )

                values = JSONParser.common(response)
                to_ret = self.de_json(values)
                self._result = to_ret
            else:
                params = {
                    'kinds': ','.join(self.kinds), 
                    'mixed': self.mixed, 
                    'rich-tracks': self.rich_tracks
                }
                
                response = self.request.get(
                    f'/users/{self.uid}/playlists',
                    params=params
                )
                
                values = JSONParser.common(response)
                to_ret = self.de_json(values)
                self._result = to_ret
        else:
            if not len(self.kinds):
                response = self.request.get(
                    f'/users/{self.uid}/playlists/list'
                )
                
                values = JSONParser.common(response)
                self.kinds = []
                for kind in values:
                    self.kinds.append(kind['kind'])
                
            for kind in self.kinds:
                response = self.request.get(
                    f'/users/{self.uid}/playlists/{kind}'
                )
                
                values = JSONParser.common(response)
                to_ret = self.de_json([values])[0]
                self._result.append(to_ret)
            
        return self

    def create(self, title: str, visibility: str = 'public'):
        data = {'title': title, 'visibility': visibility}
        response = self.request.post(
            f'/users/{self.uid}/playlists/create', 
            data=data
        )
        
        values = JSONParser.common(response)
        to_ret = self.de_json([values])[0]
        self._result.append(to_ret)

        return self

    def name(self, kind: str, title: str):
        data = {'value': title}
        response = self.request.post(
            f'/users/{self.uid}/playlists/{kind}/name',
            data=data
        )

        values = JSONParser.common(response)
        to_ret = self.de_json([values])[0]

        index = self._search(kind)
        if index is not None:
            self._result[index] = to_ret
        else:
            self._result.append(to_ret)
        
        return self

    def delete(self, kind: str):
        response = self.request.post(
            f'/users/{self.uid}/playlists/{kind}/delete'
        )

        index = self._search(kind)
        if index is not None:
                del self._result[index]
        
        return self
    
    def visibility(self, kind: str, visibility: str):

        data = {'value': visibility}
        response = self.request.post(
            f'/users/{self.uid}/playlists/{kind}/visibility',
            data=data
        )

        index = self._search(kind)
        if index is not None:
            self._result[index].visibility = visibility

        return self

    def change_relative(self, kind: str, tracks: list[dict], action: str = 'insert'):
        
        data = {"diff":{
                        "op": action,
                        "at": 0,
                        "tracks": tracks
                        }
        }
        response = self.request.post(
            f'/users/{self.uid}/playlists/{kind}/change-relative',
            data=data
        )

        return response
    
    def recommendations(self, kind: str) -> dict:
        
        response = self.request.get(f'/users/{self.uid}/playlists/{kind}/recommendations')
        values = JSONParser.common(response)
        return values

    def _search(self, kind):
        obj = None
        for i in range(len(self._result)):
            if self._result[i].kind == int(kind):
                return i
        
        return None