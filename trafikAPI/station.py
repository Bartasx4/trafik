from datetime import datetime


class Station:

    def __init__(self, cls, id_, lat, lon, name, product, prognosis_type, time):
        self._cls: str = cls
        self._id: str = id_
        self._lat: str = lat
        self._lon: str = lon
        self._name: str = name
        self._product: str = product
        self._prognosis_type: str = prognosis_type
        self._time: float = time

    @property
    def cls(self):
        return self._cls

    @property
    def id(self):
        return self._id

    @property
    def lat(self):
        return self._lat

    @property
    def lon(self):
        return self._lon

    @property
    def name(self):
        return self._name

    @property
    def product(self):
        return self._product

    @property
    def prognosis_type(self):
        return self._prognosis_type

    @property
    def time(self):
        return self._time

    def __repr__(self):
        return f'<{self.name}>'

    def __str__(self):
        return f'<{self.__module__}> {self.name}'
