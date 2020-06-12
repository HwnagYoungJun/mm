import csv
import json
from ast import literal_eval

data = []
with open('movies.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    cnt = False
    for movie in reader:
        if not cnt:
            cnt = True
            continue
        if len(movie) > 14:
            countries = literal_eval(str(movie[13]))
            if type(countries) != list:
                continue
            for country in countries:
                this_data = {
                'model': 'movies.production_country', 
                'fields': {"name": country["name"]}
                }
                data.append(this_data)

data = list(map(literal_eval, set(map(str, data))))
with open("country.json", "w") as json_file:
    json.dump(data, json_file)