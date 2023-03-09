import random
import urllib.parse
from datetime import datetime
from enum import Enum

from .station import Station
# stopLocationOrCoordLocation
# TechnicalMessages
# requestId


class Request(Enum):

    @staticmethod
    def find(name: str, request_id: int | float = random.random(), max_results: int = 20, lang: str = 'pl') -> str:
        # stopLocationOrCoordLocation
        # TechnicalMessages
        # requestId

        #       TYPE
        # ALL: search in all existing location pools
        # S: Search for station/stops only
        # A: Search for addresses only
        # P: Search for POIs only
        # SA: Search for station/stops and addresses
        # SP: search for station/stops and POIs
        # AP: search for addresses and POIs

        req = f'location.name?' \
              f'input={urllib.parse.quote(name)}&' \
              f'maxNo={max_results}&' \
              f'lang={lang}&' \
              f'format=json&' \
              f'requestId={request_id}&' \
              f'type=S'
        return req

    @staticmethod
    def route(start: Station,
              destination: Station,
              attributes: str = '',
              date: datetime = datetime.today(),
              time: datetime = datetime.today(),
              arrival: bool = False,
              lang: str = 'pl') -> str:
        # operators:
        # 275 - SL
        # categories:
        # 9 - taxi
        start = start if isinstance(start, int) else start.id
        destination = destination if isinstance(destination, int) else destination.id
        date = date.strftime('%Y-%m-%d')
        time = time.strftime('%H:%M:%S')
        req = f'trip?originId={start}&destId={destination}&' \
              f'date={urllib.parse.quote(date)}&' \
              f'time={urllib.parse.quote(time)}&' \
              f'searchForArrival={arrival.real}&' \
              f'lang={lang}&' \
              f'attributes={attributes}&' \
              f'passlist=1&' \
              f'origWalk=0%2C0%2C0%2C0&' \
              f'destWalk=0%2C0%2C0%2C0&' \
              f'unsharp=0&' \
              f'format=json&' \
              f'products=510&' \
              f'operators=275&' \
              f'categories=!9&' \
              f'showPassingPoints=true&' \
              f'requestId={random.random()}'
        return req
