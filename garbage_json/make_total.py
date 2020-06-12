import csv
import json
from ast import literal_eval

data = []
# genre
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
            'pk': int(genre["id"]), 
            'fields': {"name": genre["name"]}
            }
            data.append(this_data)

# company
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
                'pk': int(production["id"]), 
                'fields': {"name": production["name"]}
                }
                data.append(this_data)

# country
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

# 중복 제외
data = list(map(literal_eval, set(map(str, data))))

# movie_data
with open('movies.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    cnt = -1
    for movie in reader:
        if len(movie) != 23:
            continue
        cnt += 1
        print(cnt)
        if cnt == 0:
            continue
        genres = []
        productions = []
        countries = []
        language = ''
        genre_list = literal_eval(str(movie[3]))
        production_list = literal_eval(str(movie[12]))
        country_list = literal_eval(str(movie[13]))
        language_list = literal_eval(str(movie[17]))
        if type(production_list) != list:
            continue
        if type(countries) != list:
            continue
        for genre in genre_list:
            genres.append(genre["id"])
        for production in production_list:
            productions.append(production["id"])
        for country in country_list:
            countries.append(country["iso_3166_1"])
        for l in language_list:
            language = l['name']
        
        this_data = {
            "model": "movies.movie",
            "pk": int(movie[5]),
            "fields": {
                "budget": float(movie[2]),
                "genre": genres,
                "overview": movie[9],  
                "popularity": float(movie[10]), 
                "poster_path": f'https://image.tmdb.org/t/p/w500/{movie[11]}.jpg',
                "production_companies": productions, 
                "production_countries": countries,
                "release_date": movie[14],
                "revenue": float(movie[15]),
                "runtime": float(movie[16]), 
                "spoken_language": language,
                "tagline": movie[19],
                "title" : movie[20],
                "vote_average": float(movie[22]),
                "vote_count": int(movie[23])
            }
        }
        data.append(this_data)
with open("movie.json", "w") as json_file:
    json.dump(data, json_file)