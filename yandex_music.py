import abc

class YandexMusicObject(abc.ABC):
    pass

class YandexResposeObject(YandexMusicObject):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def update(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return str(self.__dict__.keys())


class YandexResposeListObject(YandexMusicObject):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self._result = []
    
    def de_json(self, results):
        obj = []
        cls = type(self)
        for result in results:
            this = cls(**result)
            obj.append(this)
        return obj
    
    def __iter__(self):
        return iter(self._result)

    def __len__(self):
        return len(self._result)

    def __getitem__(self, index):
        return self._result[index]

    def __repr__(self):
        return str(self.__dict__.keys())

class YandexMusicError(Exception):
    pass

class PlaylistDoesntExist(YandexMusicError):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors