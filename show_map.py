import sys
from io import BytesIO

import requests
from PIL import Image


def show_map(ll, spn, l="map", add_params=None):
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": l
    }
    if add_params:
        map_params["pt"] = ll
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    if not response:
        print("BAR REQUEST")
        sys.exit(1)
    Image.open(BytesIO(
        response.content)).show()
