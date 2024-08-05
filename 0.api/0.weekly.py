import os
import json
import csv
import requests
from dotenv import load_dotenv

load_dotenv()    # 현재 내가 실행하고 있는 폴더 위치에 있는 env 파일을 읽어내고 환경변수에 불러옴.
KOBIS_API_KEY = os.getenv('KOBIS_API_KEY')
print(KOBIS_API_KEY)


URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
WEEKLY_URL = f'{URL}?key={KOBIS_API_KEY}&targetDt=20240701'
# {URL}?Key=Value&Key=Value...
# print(WEEKLY_URL)

res = requests.get(WEEKLY_URL)
data = res.json()    # json 구조 -> 딕셔너리형으로 변환

movie_list = data['boxOfficeResult']['weeklyBoxOfficeList']


# 1. Dict 추출
movie_dict = {}
for movie in movie_list:

    # movieCd를 key로 설정
    movie_dict[movie['movieCd']] = {
        '영화명': movie['movieNm'],
        '누적관객수':movie['audiAcc'],
    }

print(movie_dict)

# 저장 1. json 형태, ./output/weekly.json
output_dir = './output'
output_file = os.path.join(output_dir,'weekly.json')

if not os.path.exists(output_dir):    # output_dir에 output이라는 파일이 없으면
    os.makedirs(output_dir)

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(movie_dict, f, ensure_ascii=False)    # dict 형태의 데이터를 json으로 변환

    # *여러 주의 데이터를 저장할 수 있는 방법에 대해 고민

# 저장 2. csv 형태, ./output/weekly.csv
output_file = os.path.join(output_dir,'weekly.csv')
with open(output_file, 'w', encoding='utf-8', newline='') as f:    # newline='' -> 개행 취소
    csv = csv.writer(f)
    csv_writer.writerow(['대표코드','영화명','누적관객수'])

    for movie in movie_list:
        csv_writer.writerow(movie['movieCd'],movie['MovieNm'],movie['audiAcc'])






