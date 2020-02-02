import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

music = soup.select('#body-content > div.newest-list > div > table.list-wrap > tbody > tr.list')

# print(music)

rank = 1
for musicList in music:

    title = musicList.select_one('td.info > a.title').text.strip()
    artist = musicList.select_one('td.info > a.artist').text.strip()

    if title is not None and artist is not None:

        doc = {
            'rank' : rank,
            'title' : title,
            'artist' : artist
        }

        db.musicList.insert_one(doc);

        rank += 1