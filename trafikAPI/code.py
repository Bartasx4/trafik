from typing import List


# transportCategory
def transport_category(code: str) -> str:
    transport = {'BLT': 'Regional bus',
                 'BXB': 'Express bus',
                 'BAX': 'Airport Express bus',
                 'BRE': 'Regional bus',
                 'BBL': 'Train replacement bus',
                 'ULT': 'Metro',
                 'JAX': 'Airport Express train',
                 'JEX': 'Express train',
                 'JIC': 'InterCity train',
                 'JLT': 'Local train',
                 'JPT': 'PågaTåg',
                 'JST': 'High - speed train',
                 'JRE': 'Regional train',
                 'SLT': 'Tram',
                 'FLT': 'Lokal ferry',
                 'FUT': 'International ferry'}
    return transport[code]


# catCode - Product category code
def product_category(code: int) -> str:
    product = ['High speed trains, Snabbtåg, Arlanda Express',  # 1
               'Regional trains, InterCity trains',  # 2
               'Express busses, Flygbussar',  # 3
               'Local trains Tåg, PågaTåg, Öresundståg',  # 4
               'Metro, such as tunnelbanan',  # 5
               'Tram such as Spårvagn, Tvärbanan',  # 6
               'Busses',  # 7
               'Ferries and international ferries',  # 8
               'Taxi']  # 9
    return product[code - 1]


# cls - Product class
def product_code(code: int) -> List[str]:
    codes = {1: 'Air traffic',
             2: 'High-speed and express trains',
             4: 'Regional and InterCity trains',
             8: 'Long-distance buses, e.g. ExpressBuss, Flygbussar',
             16: 'Local trains, e.g. Lokaltåg, Pågatåg, Öresundståg',
             32: 'Subways',
             64: 'Trams and light rail',
             128: 'Local buses',
             256: 'Ferries, boats and cruises',
             512: 'Taxi'}
    if code in codes:
        return [codes[code]]
    result = []
    while code > 0:
        for i in codes:
            if i > code:
                ...
