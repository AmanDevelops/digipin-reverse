from exceptions import *

def get_latlng_by_digipin(v_digipin: str) -> dict:
    v_digipin = v_digipin.replace("-", "")

    if len(v_digipin) != 10:
        raise InvalidDigiPinException

    L = [
        ["F", "C", "9", "8"],
        ["J", "3", "2", "7"],
        ["K", "4", "5", "6"],
        ["L", "M", "P", "T"],
    ]

    min_lat, max_lat = 2.50, 38.50
    min_lng, max_lng = 63.50, 99.50

    for lvl in range(10):
        digipin_char = v_digipin[lvl]
        ri = ci = -1
        found = False

        lat_div_by = 4
        lng_div_by = 4
        lat_div_val = (max_lat - min_lat) / lat_div_by
        lng_div_val = (max_lng - min_lng) / lng_div_by

        for r in range(lat_div_by):
            for c in range(lng_div_by):
                if L[r][c] == digipin_char:
                    ri, ci = r, c
                    found = True
                    break
            if found:
                break

        if not found:
            raise InvalidDigiPinException

        lat1 = max_lat - lat_div_val * (ri + 1)
        lat2 = max_lat - lat_div_val * ri
        lng1 = min_lng + lng_div_val * ci
        lng2 = min_lng + lng_div_val * (ci + 1)

        min_lat, max_lat = lat1, lat2
        min_lng, max_lng = lng1, lng2

    c_lat = (min_lat + max_lat) / 2
    c_lng = (min_lng + max_lng) / 2

    return c_lng, c_lat
