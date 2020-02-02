from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movieStar = db.movie.find_one({'title':'사운드 오브 뮤직'})['star']
sameStar = list(db.movie.find({'star': movieStar}))

for movie in sameStar:
    print (movie['title'])

search_query = {'star': movieStar}
update_query = {'$set' : {'star':0}}

db.movie.update_many(search_query, update_query)

