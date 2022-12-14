# class1.py
#클래스 정의
class Person:
    # 클래스 멤버 변수(일종의 공통 데이터로 사용)
    num_person = 0
    # 초기화 매서드
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    # 인스턴스 메서드
    def print(self):
        print("My name is {0}".format(self.name))

# 인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person()
print("인스턴스 개수:{0}".format(Person.num_person))
        
