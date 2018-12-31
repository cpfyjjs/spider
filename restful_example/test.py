import json

with open('D:\spider\dygang\movie.txt',mode='r') as f:
    for r in f.readlines():
        try :
            if len(r) >200:
                continue
            movies = json.loads(r,encoding='utf-8')
            name = movies.get('name')
            age = movies.get('age')
            location = movies.get('location')
            director = movies.get('director')
            print(name,age,location,director)
        except:
            pass