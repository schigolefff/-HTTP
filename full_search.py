import sys

from get_ll_spn import get_ll_spn
from geocode import geocode
from show_map import show_map


def get_coordinates(address):
    toponym = geocode(address)
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = map(float,
                                               toponym_coodrinates.split(" "))
    return toponym_longitude, toponym_lattitude


toponym_to_find = " ".join(sys.argv[1:])
toponym_longitude, toponym_lattitude = get_coordinates(toponym_to_find)

delta_x = delta_y = "0.005"
spn = ",".join([delta_x, delta_y])

ll = ",".join([str(toponym_longitude), str(toponym_lattitude)])
show_map(ll, spn)

ll, spn = get_ll_spn(toponym_to_find)
show_map(ll, spn, add_params=True)
