# 몽고 db에 music 데이터 제
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

#print(musics)

rank = 1
for music in musics:
    a_tag = music.select_one('td.info > a')
    title = music.select_one('td.info > a.title.ellipsis').text.strip()
    singer = music.select_one('td.info > a.artist.ellipsis').text
    if a_tag is not None:
        doc = {
            'rank' : rank,
            'title' : title,
            'singer' : singer
        }
        db.musics.insert_one(doc)
        rank += 1
