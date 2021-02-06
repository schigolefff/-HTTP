import sys
from io import BytesIO

import requests
from PIL import Image


def show_map(ll, spn, start_pos, l="map", add_params=None):
    map_params = {
        "ll": ll,
        "spn": spn,
        "l": l
    }
    new_pos = ','.join([str(pos) for pos in start_pos])
    if add_params:
        map_params["pt"] = ll
        map_params["pt"] = f"{ll},pm2wtl~{new_pos},pm2rdl"
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    if not response:
        print("BAR REQUEST")
        sys.exit(1)
    Image.open(BytesIO(
        response.content)).show()