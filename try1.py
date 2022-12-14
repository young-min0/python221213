# try1.py
#함수 정의
def divide(a,b):
    return a/b

# 에러처리
try:
    # 함수 호출
    result = divide(5,1)
except ZeroDivisionError:
    print("0으로 나누면 안 됩니다.")
except TypeError:
    print("숫자만 입력할 수 있습니다.")
else:
    print("결과:", result)
finally:
    print("한 번 더 체크(이중체크)")


print("전체 코드 실행 종료")
