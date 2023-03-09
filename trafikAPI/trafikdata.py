import json
import random
import urllib.request
import urllib.parse

from datetime import datetime
from typing import Dict

from .mine_data import mine_data
from .request import Request
from .station import Station


class Trafikdata:
    """ Trafikdata
    Methods:
    Args:
    input The name, or a part of the name, of the station that should be looked up.
    """
    API_URL = 'https://api.resrobot.se/v2.1/'

    def __init__(self, key):
        self._key = key
        random.seed()

    def arrival(self, station):
        ...

    def departure(self, station):
        ...

    def find(self, name, request_id=random.random(), max_results=20, lang='pl'):
        request = Request.find(name, request_id, max_results, lang)
        url = self.API_URL + request
        response = self.__send_request(url)
        return mine_data(response['stopLocationOrCoordLocation'], 'STATION')

    def nearby(self, lot, lat):
        ...

    def trip(self, start: Station | int,
             destination: Station | int,
             attributes: str = '',
             date: datetime = datetime.today(),
             time: datetime = datetime.today(),
             arrival: bool = False,
             lang: str = 'pl'):
        request = Request.route(start, destination, attributes, date, time, arrival, lang)
        url = self.API_URL + request
        response = self.__send_request(url)
        return mine_data(response['Trip'], 'TRIP')

    def __send_request(self, url: str) -> Dict:
        url += '&accessId=' + self._key
        headers = {'accept': 'application/json'}
        req = urllib.request.Request(url, headers=headers)
        web = urllib.request.urlopen(req)
        return json.load(web)
