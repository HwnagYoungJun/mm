import requests
import csv

def om(name):
    my_key = '&apikey=1b2630f'
    url = 'http://www.omdbapi.com/?t=' + name + my_key
    temp_res = requests.get(url).json()
    return temp_res.get("Poster")

with open('movies.csv', 'r', encoding='utf-8') as f:
    w = open('output.csv', 'w', encoding='utf-8', newline='')
    writer = csv.writer(w)
    reader = csv.reader(f)
    cnt = False
    for movie_name in reader:
        if not cnt:
            writer.writerow(['poster_url'])
            cnt = True
        else:
            writer.writerow([om(movie_name[8])])