import sys
from io import BytesIO

import requests
from PIL import Image


def show_map(points, l="map", add_params=None):
    map_params = {
        "l": l
    }
    if add_params:
        map_params["pt"] = ""
        for point in points.keys():
            map_params["pt"] += f"{point},{points[point]}~"
        map_params["pt"] = map_params["pt"][:-1].replace(' ', '')
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    if not response:
        print("BAR REQUEST")
        sys.exit(1)
    Image.open(BytesIO(
        response.content)).show()
