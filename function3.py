# function3.py
#가변형식인 경우
wordlist = ["J", "A", "M"]

#함수 정의
def change(x):
    # 복사본을 생성
    x1 = x[:]
    x1[0] = "H"
    print("내부:", x1)

#호출
change(wordlist)
print(wordlist)

print("---global keyword---")
g = 1
def testScope(a):
    global g
    g = 2
    return g+a

# 호출
print(testScope(1), "전역변수 g:", g)
print(testScope(g), g)

#교집합 문자를 리턴
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print( intersect("HAM","SPAM"))


#함수의 기본인자값
def times(a=10,b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드인자(parameter 명시)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

# 호출
print( connectURI("credu.com","80"))
print( connectURI(port="8080", server="credu.com"))
