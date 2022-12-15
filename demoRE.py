# demoRE.py
import re

#숫자가 있거나 없는 th문자열패턴
result = re.search("[0-9]*th", " 35th")
print(result)
print(result.group())

# result = re.match("[0-9]*th", " 35th")
# print(result)
# print(result.group())

result = re.search("apple", "this is apple")
print(result.group())

# result = re.match("apple", "this is apple")
# print(result.group())

# 컴파일 함수 사용
s = "Apple is big company and apple is very delicious"
# 대소문자를 구분하지 않도록
c = re.compile("apple", re.I)
print( c.findall(s))

print("---연도 찾기---")
result = re.search("\d{4}", " 올해는 2022년")
print(result.group())
result = re.search("\d{5}", " 우리 동네는 52300")
print(result.group())


