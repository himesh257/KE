import requests
import json

api_key = "pub_5786b806a42b7e1083d732696556d095dd9c"
#query = "climate change, pollution, Carbon Dioxide, Carbon Footprint, greenhouse gas, Carbon cycle"
query = ["Abatement", "Adaptation", "Adaptation assessment", "Aerosols", "Albedo", "Anthropogenic", "Anthropogenic emissions", "Atlantic Multi-decadal Oscillation (AMO)", "Atmosphere", "Available potential energy"]

"""
print("status: {}".format(response.json()["status"]))
print("total items: {}".format(response.json()["totalResults"]))
print("keys: {}".format(response.json().keys()))
"""

for q in query:
    print(q)
    url = "https://newsdata.io/api/1/news?apikey=" + api_key + "&q=" + q + "&language=en"

    response = requests.get(url)
    nextPage = response.json()["nextPage"]

    with open('json_data.json', 'a') as outfile:
        json.dump(response.json(), outfile, indent=4, sort_keys=True)

    while nextPage:
        new_url = url + "&page=" + str(nextPage)
        new_response = requests.get(new_url)
        nextPage = new_response.json()["nextPage"]
        print(nextPage)
        
        with open('json_data.json', 'a') as outfile:
            json.dump(new_response.json(), outfile, indent=4, sort_keys=True)

