import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기 copy Selector
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


# movies (tr들) 의 반복문을 돌리기
for music in musics:
    # movie 안에 a 가 있으면,
    title = music.select_one('td.info > a.title.ellipsis')
    if title is not None:
        # a의 text를 찍어본다.
        print(title.text.strip())
