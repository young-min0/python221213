# web1.py
from bs4 import BeautifulSoup

# 페이지 로딩: 메서드 체인 (연속으로 함수, 메서드 호출)
page = open(r"c:\work\test01.html", "rt", encoding="utf-8").read()
# 검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
# 전체 페이지 보기
# print(soup.prettify())

# <p> 태그 전부 검색
# print(soup.find_all("p"))

# 첫 번째 <p> 태그
# print(soup.find("p"))

# 검색의 조건: <p class='outer-text'>"
# 파이썬의 키워드 class 제공(이름 충돌): class_ 
# print(soup.find_all("p", class_='outer-text'))

# 컨텐츠만 가져오기
for item in soup.find_all("p"):
    print(item.text.strip().replace("\n",""))
