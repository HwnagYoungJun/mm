import csv
import json
from ast import literal_eval

data = []
with open('movies.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    cnt = -1
    for movie in reader:
        if len(movie) != 24:
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
        if movie[15] == '' or movie[16] == '':
            continue
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