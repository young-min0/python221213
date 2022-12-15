# web1.py
from bs4 import BeautifulSoup

# 페이지 로딩
page = open(r"c:\work\test01.html", "rt", encoding="utf-8").open()
# 검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
# 전체 페이지 보기
print(soup.prettify())