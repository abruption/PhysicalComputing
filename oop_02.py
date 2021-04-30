# OOP Part 2

# Inheritance (상속)

class Animal:
    count = 0   # class 변수
    def __init__(self, name):
        self.name = name
        Animal.count += 1
    # 인스턴스 메서드    
    def move(self):
        print('이동합니다.')
    def speak(self):
        pass
    # 클래스 메서드 선언을 위해 데커레이터
    @classmethod
    def animals(cls):
        print('집에서 키우는 동물은 총 {0}마리 입니다!'.format(Animal.count))

class Kitten(Animal):
    # 인스턴스 메서드
    def speak(self):    # Override
        print('냐옹~~')

class Puppy(Animal): 
    # 인스턴스 메서드   
    def speak(self):    # Override
        print('멍멍~~')

d1 = Puppy('쫑')
k1 = Kitten('나비')
Animal.animals()
d2 = Puppy('해피')
Animal.animals()

d1.speak()

print(k1.name + '가', end=' ')
k1.move()
k1.speak()




# Class & Object
# 메서드(함수), 속성(멤버변수)

# class Puppy:
#     # 특수 메서드, 생성자 함수
#     def __init__(self, name, age):
#         """ 강아지의 이름과 나이 속성을 초기화 """
#         self.name = name
#         self.age = age

#     def wait(self):
#         """ 강아지 대기 시키기 """
#         print(self.name + "이 기다립니다.")

#     def sit(self):
#         """ 강아지 앉게 하기 """
#         print('{0}이(가) 앉습니다.'.format(self.name))

#     # get, set 메서드
#     def set_age(self, n):
#         """ 나이 지정 """
#         self.age = n
    
#     def get_age(self):
#         """ 나이 리턴 """
#         return self.age

# p1 = Puppy('zzong', 2)
# p2 = Puppy('happy', 1)

# p2.sit()
# p1.wait()

# # 속성 값을 직접 바꾸기
# # p1.age = 3
# # p2.age = 2

# # 메서드를 통해 값 바꾸기
# p1.set_age(3)
# p2.set_age(2)

# # 메서드를 통해 값 가져오기
# print('{0}의 나이는 {1}살입니다.'.format(p1.name, p1.get_age()))
# print('{0}의 나이는 {1}살입니다.'.format(p2.name, p2.age))