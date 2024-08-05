import requests
from pprint import pprint
from bs4 import BeautifulSoup

URL = 'https://dhlottery.co.kr/common.do?method=main'

res = requests.get(URL)
# print(res.text)

# parser : html 코드를 파이썬이 읽기 쉬운 데이터 형태로 변환
soup = BeautifulSoup(res.text, 'html.parser')
# balls = soup.select('span.ball_645')
# for ball in balls:
#     print(ball.text)

# print(soup.select('span.bonus + span'))    # '+' : 형제 요소를 반환
# print(soup.select('a#numView > span'))       # '>' : 자식 요소를 반환

print(soup.select('a[href*="/gameResult"]'))
