# 0.weekly.py에서 수집한 영화의 배우 목록 추출
from dotenv import load_dotenv
import os, csv, json, requests

load_dotenv()
KOBIS_API_KEY = os.getenv('KOBIS_API_KEY')

URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
SEARCH_MOVIE_URL = f'{URL}?key={KOBIS_API_KEY}&movieCd='

input_dir = './output'
input_file = os.path.join(input_dir, 'weekly.json')

with open(input_file, 'r', encoding='utf-8') as f:
    movie_dict = json.load(f)    # load : json->dict / dump : dict->json
    # print(movie_dict)

    for movie_cd in movie_dict.keys():
        SM_URL = SEARCH_MOVIE_URL + movie_cd

        res = requests.get(SM_URL)
        data = res.json()
        
        actors = data['movieInfoResult']['movieInfo']['actors']
        /print(actors)

        actor_str = ', '.join([actor['peopleNm'] for actor in actors])
        print(actor_str)
