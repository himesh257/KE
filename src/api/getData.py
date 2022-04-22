"""
documentation on the news api: https://newsdata.io/docs
actual website: https://newsdata.io/search-news
"""

import requests
import json

api_key = "pub_5786b806a42b7e1083d732696556d095dd9c"

"""
json_data.json file contains data for these queries:
query = ["climate change", "pollution", "Carbon Dioxide", "Carbon Footprint", "greenhouse gas", "Carbon cycleAbatement", "Adaptation", "Adaptation assessment", "Aerosols", "Albedo", "Anthropogenic", "Anthropogenic emissions", "Atlantic Multi-decadal Oscillation (AMO)", "Atmosphere", "Available potential energy"]
"""
 
# Opening JSON file with terms to query
with open('terms.json') as json_file:
    query = json.load(json_file)

count = 1
for q in query:
    print(str(count) + ": " + q)
    url = "https://newsdata.io/api/1/news?apikey=" + api_key + "&q=" + q + "&language=en"

    response = requests.get(url)
    nextPage = response.json()["nextPage"]
    response["query_term"] = q

    # if nextPage is not None, keep querying data for it
    while nextPage:
        new_url = url + "&page=" + str(nextPage)
        new_response = requests.get(new_url)
        new_response["query_term"] = q
        nextPage = new_response.json()["nextPage"]
        print(nextPage)
        
        with open('json_data_terms.json', 'a') as outfile:
            json.dump(new_response.json(), outfile, indent=4, sort_keys=True)

    with open('json_data_terms.json', 'a') as outfile:
        outfile.write(",")
        outfile.close()

    count += 1
