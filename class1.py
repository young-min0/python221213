# class1.py
#클래스 정의
class Person:
    # 초기화 매서드
    def __init__(self):
        self.name = "default name"
    # 인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

# 인스턴스 생성
p1 = Person()
# 메서드 호출
p1.print()


        
