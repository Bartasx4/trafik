from typing import List, Dict

from .product import Product
from .route import Route
from .station import Station


class Trip:

    def __init__(self, calculation, destination, duration, idx, route, rt_duration, service, start, status, transfer):
        self._calculation = calculation
        self._destination = destination
        self._duration = duration
        self._idx = idx
        self._route = route
        self._rt_duration = rt_duration
        self._service = service
        self._start = start
        self._status = status
        self._transfer = transfer

    @property
    def calculation(self):
        return self._calculation

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
    def route(self):
        return self._route

    @property
    def rt_duration(self):
        return self._rt_duration

    @property
    def service(self):
        return self._service

    @property
    def start(self):
        return self._start

    @property
    def status(self):
        return self._status

    @property
    def transfer(self):
        return self._transfer

    def __repr__(self):
        return f'[{self.start.name}] -> [{self.destination.name}]'

    def __str__(self):
        return f'<{self.__module__}> [{self.start.name}] -> [{self.destination.name}]'
