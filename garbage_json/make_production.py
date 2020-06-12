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
        if len(movie) > 13:
            production_list = literal_eval(str(movie[12]))
            if type(production_list) != list:
                continue
            for production in production_list:
                this_data = {
                'model': 'movies.production_company', 
                'pk': production["id"], 
                'fields': {"name": production["name"]}
                }
                data.append(this_data)

data = list(map(literal_eval, set(map(str, data))))
with open("company.json", "w") as json_file:
    json.dump(data, json_file)