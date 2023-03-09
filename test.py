from trafikAPI import Trafikdata

# Static data https://api.resrobot.se/gtfs/sweden.zip?key={apikey}
# 740067036 - Kassavägen
# 740000705 - Jakobsberg station
# 740000665 - Norrtälje busstation
# 740020749 - T-Centralen T-bana (Stockholm kn)
# 740000049 - Södertälje hamn
# 740000721 - Södertälje centrum station

# '754;754;408935' - 'matchId'
# '754' - line
# '1275075400001' lineId
key = '8ae6e256-7abd-48b3-bb82-8b5a13ea8334'
trafik = Trafikdata(key)
route = trafik.trip(740000049, 740000721)
# kassa = trafik.trip(740067036, 740000705)

# plats = trafik.find('kassav')
# route = trafik.trip(740000665, 740020749)

# ilosc przesiadek
# sprawdzic odwolane
# nie pokazuj chodzenia, taxi itp.
