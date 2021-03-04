#-*- coding: utf-8 -*-

# 조건문
# 조건에 따라 코드 실행여부를 결정하는 구문

age = int(input('나이가 어떻게 되세요? '))
with_parents = input('보호자와 같이 오셨나요? 네/아니오 ')
if (age >= 19) or (with_parents == '네'):
    print('15세 이상 관람가 입장가능~')
else:
    print('입장을 하실 수 없습니다.')
print()

if 22:  # else 조건이 실행되기 위해서는 조건에 0을 입력
    print('항상 실행!')
else:
    print('실행 될 일이 없음')
print()

# 비교 연산자
print(5 == 5)   # True
print(5 != 5)   # False
print(5 > 5)    # False
print(5 >= 5)   # True
print()

# 논리 연산자 (feat. 비교 연산자)
x = 5
print(2>x and x>1)  # False
print(2!=x and x>1)  # True
print(2>x or x>1)  # True
print(2==x or x<1)  # False
print(not(2==x))    # True