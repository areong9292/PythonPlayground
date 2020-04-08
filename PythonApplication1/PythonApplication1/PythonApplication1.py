import requests
from bs4 import BeautifulSoup

import re

url = 'https://finance.naver.com/sise/'
resp = requests.get(url)



# beautifulsoup 모듈로 html 파일 가져온다
soup = BeautifulSoup(resp.text, "html.parser")

# 현재 코스피 수치
now_kospi = soup.find(class_ = 'num', id = 'KOSPI_now')
print("현재 코스피 - ", now_kospi.get_text())

print()

# 코스피 변화
change_kospi = soup.find(class_ = 'num_s', id = 'KOSPI_change')
print("코스닥 변화량", change_kospi.get_text())


# 현재 코스닥 수치
now_kosdaq = soup.find(class_ = 'num', id = 'KOSDAQ_now')
print("현재 코스닥 - ", now_kosdaq.get_text())

print()

# 코스닥 변화
change_kosdaq = soup.find(class_ = 'num_s', id = 'KOSDAQ_change')
print("코스닥 변화량", change_kosdaq.get_text())


# 현재 코스피 200 수치
now_kospi200 = soup.find(class_ = 'num', id = 'KPI200_now')
print("현재 코스피 200 - ", now_kospi200.get_text())

print()

# 코스닥 변화
change_kospi200 = soup.find(class_ = 'num_s', id = 'KPI200_change')
print("코스피 200 변화량", change_kospi200.get_text())