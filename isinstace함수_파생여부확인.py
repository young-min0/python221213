class Person:
    pass
class Bird:
    pass
class Student(Person):
    pass

p, s = Person(), Student()
print("p is instance of Person: ", isinstance(p, Student))
print("s is instance of Person: ", isinstance(s, Student))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))