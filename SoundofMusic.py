from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


# for i in target_movie:
# if target_movie
#
# print (target_movie['star'])
#
# 1. 전체 영화검색
# 2. target_movie['star'] == 점수
# return 영화제목

target_movie = db.movies.find_one({'title':'사운드 오브 뮤직'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))

for movie in movies:
    print(movie['title'])

# for i in 전체 영화 길이
#     if target_movie['star'] == 영화.점수
#         return 영화 제목