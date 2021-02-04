from geocode import geocode


def get_ll_spn(address):
    toponym = geocode(address)
    toponym_coords = toponym["Point"]["pos"]
    lower_corner = toponym["boundedBy"]["Envelope"]["lowerCorner"]
    upper_corner = toponym["boundedBy"]["Envelope"]["upperCorner"]
    left, bottom = map(float, lower_corner.split())
    right, up = map(float, upper_corner.split())
    delta_x = abs(left - right) / 3
    delta_y = abs(bottom - up) / 3
    ll = toponym_coords.replace(' ', ',')
    spn = ','.join([str(delta_x), str(delta_y)])
    return ll, spn
