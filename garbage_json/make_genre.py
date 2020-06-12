import csv
import pandas as pd
import json
import numpy as np
from ast import literal_eval

data = []
with open('movies.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    cnt = False
    for movie in reader:
        if not cnt:
            cnt = True
            continue
        genre_list = literal_eval(str(movie[3]))
        for genre in genre_list:
            this_data = {
            'model': 'movies.genre', 
            'pk': genre["id"], 
            'fields': {"name": genre["name"]}
            }
            data.append(this_data)

data = list(map(literal_eval, set(map(str, data))))
with open("genre.json", "w") as json_file:
    json.dump(data, json_file)