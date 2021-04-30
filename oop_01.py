# OOP Part 1
# Class & Object

# 메서드(함수), 속성(멤버변수)

class Puppy:
    # 특수 메서드, 생성자 함수
    def __init__(self, name, age):
        """ 강아지의 이름과 나이 속성을 초기화 """
        self.name = name
        self.age = age

    def wait(self):
        """ 강아지 대기 시키기 """
        print(self.name + "이 기다립니다.")

    def sit(self):
        """ 강아지 앉게 하기 """
        print('{0}이(가) 앉습니다.'.format(self.name))

p1 = Puppy('zzong', 2)
p2 = Puppy('happy', 1)

print('{0}의 나이는 {1}살입니다.'.format(p2.name, p2.age))
print('{0}의 나이는 {1}살입니다.'.format(p1.name, p1.age))

p2.sit()
p1.wait()

# 속성 값을 직접 바꾸기
p1.age = 3
p2.age = 2

print('{0}의 나이는 {1}살입니다.'.format(p2.name, p2.age))
print('{0}의 나이는 {1}살입니다.'.format(p1.name, p1.age))