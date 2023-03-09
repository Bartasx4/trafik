from datetime import datetime
from typing import Dict, List

from .code import transport_category
from .product import Product
from .route import Route
from .station import Station
from .trip import Trip


def mine_station(station: Dict):
    if 'StopLocation' in station:
        return mine_station(station['StopLocation'])
    if 'CoordLocation' in station:
        return None
    cls = station['productAtStop'][0]['cls'] if 'productAtStop' in station else ''
    id_ = int(station['extId'])
    lat = station['lat']
    lon = station['lon']
    name = station['name']
    product = mine_data(station['product'], 'PRODUCT') if 'product' in station else {}
    prognosis_type = product['prognosisType'] if 'prognosisType' in product else None
    time = station['time'] if 'time' in station else None
    date = station['date'] if 'date' in station else None
    if all([time, date]):
        time = datetime.fromisoformat(f'{date}T{time}')
    return Station(cls, id_, lat, lon, name, product, prognosis_type, time)


def mine_product(product: Dict):
    category_code = product['catCode']
    cls = product['cls']
    display_nr = product['displayNumber']
    line = product['line']
    line_id = product['lineId']
    match_id = product['matchId']
    name = product['name']
    number = product['num']
    operator_code = product['operatorCode']
    route_idx_from = product['routeIdxFrom']
    route_idx_to = product['routeIdxTo']
    return Product(category_code, cls, display_nr, line, line_id, match_id,
                   name, number, operator_code, route_idx_from, route_idx_to)


def mine_trip(trip: Dict):
    calculation = trip['calculation']
    destination = mine_data(trip['Destination'], 'STATION')
    duration = get_time(trip['duration'])
    idx = trip['idx']
    route = mine_data(trip['LegList']['Leg'], 'ROUTE')
    rt_duration = get_time(trip['rtDuration'])
    service = trip['ServiceDays']
    start = mine_data(trip['Origin'], 'STATION')
    status = trip['TripStatus']
    transfer = 0 if 'transferCount' not in trip else int(trip['transferCount'])
    return Trip(calculation, destination, duration, idx, route, rt_duration, service, start, status, transfer)


def mine_route(routes: Dict):
    if routes['type'] == 'WALK':
        return None
    category = transport_category(routes['category'])
    destination = mine_data(routes['Destination'], 'STATION')
    duration = get_time(routes['duration'])
    idx = routes['idx']
    name = routes['name']
    number = routes['number']
    product = mine_data(routes['Product'], 'PRODUCT')
    start = mine_data(routes['Origin'], 'STATION')
    station = mine_data(routes['Stops']['Stop'], 'STATION')

    status = ''
    for journey_status in ['Planned', 'Replacement', 'Additional', 'Special']:
        if journey_status.startswith(routes['JourneyStatus']):
            status = journey_status
            break

    # status = routes['JourneyStatus']
    return Route(category, destination, duration, idx, name, number, product, start, station, status)


def mine_data(data: Dict | List, data_type: str):
    if isinstance(data, list):
        result = []
        for element in data:
            data = mine_data(element, data_type)
            if data is not None:
                result.append(data)
        return result
    if data_type == 'TRIP':
        return mine_trip(data)
    if data_type == 'PRODUCT':
        return mine_product(data)
    if data_type == 'ROUTE':
        return mine_route(data)
    if data_type == 'STATION':
        return mine_station(data)


# Total travel time in ISO8601 format
# Example: PT9H32M
def get_time(iso8601):
    import re
    hours = '00'
    minutes = '00'
    if h := re.search('\\d+H', iso8601):
        hours = h[0][:-1].rjust(2, '0')
    if m := re.search('\\d+M', iso8601):
        minutes = m[0][:-1].rjust(2, '0')
    return hours + ':' + minutes
