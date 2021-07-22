# from bs4 import BeautifulSoup as bs
# from urllib.request import urlopen
# from urllib.parse import quote_plus
 
# baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# plusUrl = input('검색어 입력: ') 
# crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))
 
# url = baseUrl + quote_plus(plusUrl) # 한글 검색 자동 변환
# html = urlopen(url)
# soup = bs(html, "html.parser")
# img = soup.find_all(class_='_img')
 
# n = 1
# for i in img:
#     print(n)
#     imgUrl = i['data-source']
#     with urlopen(imgUrl) as f:
#         with open('../../static/img/img' + str(n)+'.jpg','wb') as h: # w - write b - binary
#             img = f.read()
#             h.write(img)
#     n += 1
#     if n > crawl_num:
#         break
    
    
# print('Image Crawling is done.')

import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time
 
driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")    # 이미지들을 가져올 url
time.sleep(5) # 5초 동안 페이지 로딩 기다리기
 
req = driver.page_source
 
soup = BeautifulSoup(req, 'html.parser')
 
thumbnails = soup.select("#imgList > div > a > img")
# 크롬에서 가져오고 싶은 이미지 오른쪽 클릭
# 검사 -> 개발자 도구에서의 선택된 부분을 오린쪽 클릭
# copy -> copy selector 를 하여 복사된 정보에서 중복을 삭제
 
i=1
for thumbnail in thumbnails:    # 해당 페이지의 이미지들의 태그들을 모두 가져옴
    src = thumbnail["src"]    # 가져온 태그 정보중에 src만 가져옴
    dload.save(src, f'imgs/{i}.jpg')    # 설정한 경로로 jpg파일로 다운로드
    i += 1
 
driver.quit() # 끝나면 닫아주기