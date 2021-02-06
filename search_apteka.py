import argparse

import requests

from distance import lonlat_distance
from show_map import show_map
from get_ll_spn import get_ll_spn


def get_organisation(ll):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "2398bcb3-ab43-4f54-85b6-f217451248a5"
    search_params = {
        "apikey": api_key,
        "text": "аптека",
        "lang": "ru_RU",
        "ll": ll,
        "type": "biz"
    }
    response = requests.get(search_api_server, params=search_params)
    if not response:
        pass
    json_response = response.json()
    organization = json_response["features"][0]
    return organization


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("address", type=str, nargs="*")
    args = parser.parse_args()
    address = " ".join(args.address)
    address_ll = get_ll_spn(address)
    organization = get_organisation(address_ll[0])
    org_name = organization["properties"]["CompanyMetaData"]["name"]
    org_address = organization["properties"]["CompanyMetaData"]["address"]
    org_coords = organization["geometry"]["coordinates"]
    org_time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
    lon_lat = address_ll[0].split(',')
    lon, lat = lon_lat
    org_distance = round(lonlat_distance((lon, lat), org_coords))
    delta = "0.005"

    show_map(address_ll[0], spn=",".join([delta, delta]),
             add_params=True, start_pos=org_coords)

    snippet = f"Название: {org_name}\nАдрес: {org_address}\nВремя Работы: {org_time}\nРасстояние: {org_distance}"
    print(snippet)
