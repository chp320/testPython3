import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 페이지에서 html 을 가져옴
response = requests.get("https://news.naver.com")

# BeautifulSoup 객체 생성
soup = BeautifulSoup(response.text, 'html.parser')

# 뉴스 헤드라인 검색
headlines = soup.select("div.cjs_channel_card div.cjs_journal_wrap._item_contents div.cjs_news_tw div.cjs_t")

# 각 헤드라인 텍스트 출력
for headline in headlines:
    print(headline.text.strip())