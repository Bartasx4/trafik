from trafikAPI import Trafikdata


if __name__ == '__main__':
    # 740067036 - Kassavägen
    # 740000705 - Jakobsberg station
    key = '8ae6e256-7abd-48b3-bb82-8b5a13ea8334'
    trafik = Trafikdata(key)
    kassa = trafik.trip(740067036, 740000705)
