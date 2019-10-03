from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 몽고 DB에서 특정 데이터 보기
all_movies = list(db.movies.find())
#print(all_movies)

same_stars = list(db.users.find({'star':'9.60'}))
print(same_stars)

