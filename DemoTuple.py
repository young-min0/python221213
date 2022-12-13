# DemoTuple.py
tp = (1,2,3)
print( len(tp) )
print( type(tp) )
print( tp[0] )

# 함수를 정의
def calc(a,b):
    return a+b, a*b

# 호출
result = calc(3,4)
print( result[0] )
print( result[1] )

print( "id: %s, name: %s" % ("kim", "김유신") )

args = (5,6)
print( calc(*args) )

print("--형식변환--")
a = (10,20,30)
b = list(a)
b.append(40)
print( b )

print("---dict---")
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print( type(device) )
print( device )
#디버깅할 때 중단점(Break Point)
for item in device.items():
    print(item)

for k,v in device.items():
    print(k, v)

#검색
print( device["아이폰"] )
#입력
device["맥북"]= 15
#수정
device["아이폰"] = 6
#삭제
del device["윈도우"]
print( device )
