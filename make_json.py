import csv
import json
from ast import literal_eval

# {"model": "movies.movie", "pk": 11, "fields": {"title": "\uc2a4\ud0c0\uc6cc\uc988 \uc5d0\ud53c\uc18c\ub4dc 4: \uc0c8\ub85c\uc6b4 \ud76c\ub9dd", "original_title": "Star Wars", "release_date": "1997-04-12", "popularity": 69.107, "vote_count": 13591, "vote_average": 8.2, "adult": false, "overview": "\uacf5\ud654\uad6d\uc774 \ubd95\uad34\ud558\uace0 \uc81c\uad6d\uc774 \uc218\ub9bd\ub41c \ub4a4 20\ub144, \uc81c\ub2e4\uc774 \uae30\uc0ac\ub2e8\uc740 \uc804\uba78\ud558\uace0 \uac15\ub825\ud55c \uc81c\uad6d\uad70\uc758 \ud6a1\ud3ec\uc5d0 \uc740\ud558\uacc4\ub294 \uacf5\ud3ec\uc5d0 \ud729\uc2f8\uc5ec \uc788\ub2e4. \uadf8\ub7ec\ub358 \uc911 \uacf5\ud654\uad6d \uc7ac\uac74\uc744 \ub178\ub9ac\ub294 \ubc18\ub780\uad70\uc774 \uc81c\uad6d\uad70\uc758 \ube44\ubc00\ubcd1\uae30 \ub370\uc2a4\uc2a4\ud0c0 \uc124\uacc4\ub3c4\ub97c \ud6d4\uccd0 \ub2ec\uc544\ub098\uace0 \uc81c\uad6d\uad70\uc740 \uc774\ub97c \ucad3\ub294\ub2e4. \ud558\uc9c0\ub9cc \uacb0\uad6d \uc81c\uad6d\uc758 \uc190\uc5d0 \ubd99\uc7a1\ud788\uac8c \ub41c \uadf8\ub4e4\uc740 \ub4dc\ub85c\uc774\ub4dc R2-D2\uc5d0 \uc124\uacc4\ub3c4\ub97c \ub123\uc5b4\uc11c R2\uc758 \uce5c\uad6c C-3PO\uc640 \ud0c8\ucd9c\uc2dc\ud0a4\ub294 \ub370 \uc131\uacf5\ud558\uace0, \ub450 \ub4dc\ub85c\uc774\ub4dc \ucf64\ube44\ub294 \ud0c0\ud22c\uc778\uc758 \uc2dc\uace8 \ub9c8\uc744\uc5d0\uc11c \uc219\ubd80\uc640 \ud568\uaed8 \uc0b4\uace0 \uc788\ub358 \uccad\ub144 \ub8e8\ud06c \uc2a4\uce74\uc774\uc6cc\ucee4\uc5d0\uac8c \uc624\uac8c \ub418\ub294\ub370...", "original_language": "en", "poster_path": "/7XFfURIFCJxN1mfBg0SAjk5yGzg.jpg", "backdrop_path": "/pPj1yM2PXiC56GkUYmoT3qR9zka.jpg", "genres": [12, 28, 878]}}

data = []
with open('movies.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    cnt = -1
    for movie in reader:
        if len(movie) < 24:
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
                "budget": int(movie[2]),
                "genre": genres,
                "overview": movie[9],  
                "popularity": float(movie[10]), 
                "poster_path": f'https://image.tmdb.org/t/p/w500/{movie[11]}.jpg',
                "production_companies": productions, 
                "production_countries": countries,
                "release_date": movie[14],
                "revenue": movie[15],
                "runtime": movie[16], 
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