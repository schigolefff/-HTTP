import math


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b

    radians_lattitude = math.radians((float(a_lat) + float(b_lat)) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)

    dx = abs(float(a_lon) - float(b_lon)) * degree_to_meters_factor * lat_lon_factor
    dy = abs(float(a_lat) - float(b_lat)) * degree_to_meters_factor

    distance = math.sqrt(dx * dx + dy * dy)

    return distance
