import gzip
from pathlib import Path
from google.transit import gtfs_realtime_pb2
import urllib.request

key = 'cdad8136d5e9455f8c341135464a2fed'

DIRECTORY = 'datafiles/'
Service = {'alerts': {'path': DIRECTORY + 'ServiceAlerts.pb',
                      'url': 'https://opendata.samtrafiken.se/gtfs-rt/sl/ServiceAlerts.pb?key='},
           'updates': {'path': DIRECTORY + 'TripUpdates.pb',
                       'url': 'https://opendata.samtrafiken.se/gtfs-rt/sl/TripUpdates.pb?key='},
           'positions': {'path': DIRECTORY + 'VehiclePositions.pb',
                         'url': 'https://opendata.samtrafiken.se/gtfs-rt/sl/VehiclePositions.pb?key='}}
STATIC = {'path': DIRECTORY + 'static.zip',
          'url': 'https://api.resrobot.se/gtfs/sweden.zip?key='}


class Trafikdata:

    def __init__(self, key, update=False):
        self._key = key
        for service in Service:
            Service[service]['url'] += self._key
        STATIC['url'] += self._key
        self._alerts = gtfs_realtime_pb2.FeedMessage()
        self._updates = gtfs_realtime_pb2.FeedMessage()
        self._positions = gtfs_realtime_pb2.FeedMessage()
        if update:
            self.update()
        else:
            self.__open()

    @property
    def alerts(self):
        return self._alerts

    @property
    def updates(self):
        return self._updates

    @property
    def positions(self):
        return self._positions

    def read(self, service, items=0):
        feed = None
        if service == 'alerts':
            feed = self.alerts
        elif service == 'updates':
            feed = self.updates
        elif service == 'positions':
            feed = self.positions
        for i, entity in enumerate(feed.entity):
            if i >= items != 0:
                break
            print(entity)
            if entity.HasField('trip_update'):
                print(entity.trip_update)

    def update(self):
        self.__remove_files()
        alerts = self.__download(Service['alerts']['url'])
        updates = self.__download(Service['updates']['url'])
        positions = self.__download(Service['positions']['url'])
        self.__save_file(Service['alerts']['path'], alerts)
        self.__save_file(Service['updates']['path'], updates)
        self.__save_file(Service['positions']['path'], positions)
        self._alerts.ParseFromString(alerts)
        self._updates.ParseFromString(updates)
        self._positions.ParseFromString(positions)

    def update_static(self):
        static = self.__download(STATIC['url'], decompress=False)
        self.__save_file(STATIC['path'], static)

    @staticmethod
    def __download(url, decompress=True):
        headers = {'Accept-encoding': 'br, gzip, deflate',
                   'Content-Type': 'application/octet-stream',
                   'Transfer-Encoding': 'chunked',
                   'Content-Encoding': 'gzip',
                   'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1;de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
        # web = urllib.request.urlopen(url, headers=header)
        req = urllib.request.Request(url, headers=headers)
        web = urllib.request.urlopen(req)
        result = web.read()
        if decompress:
            result = gzip.decompress(result)
        return result

    def __open(self, update=False):
        if not all([Path(Service['alerts']['path']).is_file(),
                    Path(Service['updates']['path']).is_file(),
                    Path(Service['positions']['path']).is_file()])\
                or update:
            self.update()
            return
        self._alerts.ParseFromString(self.__open_file(Service['alerts']['path']))
        self._updates.ParseFromString(self.__open_file(Service['updates']['path']))
        self._positions.ParseFromString(self.__open_file(Service['positions']['path']))

    @staticmethod
    def __open_file(path):
        if not Path(path).is_file():
            return
        with open(path, 'rb') as file:
            content = file.read()
        return content

    @staticmethod
    def __remove_files():
        path = Path(DIRECTORY)
        if not path.is_dir():
            path.mkdir()
            return
        for file in path.iterdir():
            if file.is_file():
                file.unlink()

    @staticmethod
    def __save_file(path, content):
        with open(path, 'wb') as file:
            file.write(content)
