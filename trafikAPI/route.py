from typing import List

from .product import Product
from .station import Station


class Route:

    def __init__(self, category, destination, duration, idx, name, number, product, start, station, status):
        self._category: str = category
        self._destination: Station = destination
        self._duration: str = duration
        self._idx: int = idx
        self._name: str = name
        self._number: str = number
        self._product: Product = product
        self._start: Station = start
        self._station: List[Station] = station
        self._status: str = status

    @property
    def category(self):
        return self._category

    @property
    def destination(self):
        return self._destination

    @property
    def duration(self):
        return self._duration

    @property
    def idx(self):
        return self._idx

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @property
    def product(self):
        return self._product

    @property
    def start(self):
        return self._start

    @property
    def station(self):
        return self._station

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return f'[{self.start.name}] -> [{self.destination.name}]'

    def __str__(self):
        return f'<{self.__module__}> [{self.start.name}] -> [{self.destination.name}]'
