# web2.py
# 서버와 통신
import urllib.request
# 웹크롤링
from bs4 import BeautifulSoup

# 네이버에 요구
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
# 검색이 용이한 객체
soup = BeautifulSoup(data, "html.parser")

cartoons = soup.find_all("td", class_="title")
print("길이:{0}".format(len(cartoons)))
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title.strip())
print(link.strip())
# <td class="title">
# 	<a href="/webtoon/detail?titleId=20853&no=50&weekday=fri" >마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>

for tag in cartoons:
    title = tag.text.strip()
    print(title)
 