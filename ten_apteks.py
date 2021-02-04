import requests

from show_map import show_map

if __name__ == '__main__':
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "2398bcb3-ab43-4f54-85b6-f217451248a5"
    search_params = {
        "apikey": api_key,
        "text": "аптека",
        "lang": "ru_RU",
        "ll": "37.588392,55.734036",
        "type": "biz"
    }
    response = requests.get(search_api_server, params=search_params)
    json_response = response.json()
    organizations = json_response["features"]
    if len(organizations) > 10:
        organizations = organizations[:10]

    orgs = {}

    colors = {
        "everyday": "pm2gnl",
        "intervals": "pm2dbm",
        "nothing": "pm2grl"
    }

    for org in organizations:
        org_coords = org["geometry"]["coordinates"]
        coords = f"{org_coords[0]}, {org_coords[1]}"
        org_time = org["properties"]["CompanyMetaData"]["Hours"]["text"]
        if "круглосуточно" in org_time:
            orgs[coords] = colors["everyday"]
        elif org_time:
            orgs[coords] = colors["intervals"]
        else:
            orgs[coords] = colors["nothing"]
    show_map(points=orgs, add_params=True)
