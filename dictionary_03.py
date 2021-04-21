# Dictionary (cont.)

# 안주 추천 프로그램 v0.3
import random
alcohol_foods = {'맥주':'치킨', '와인':'치즈','고량주':'짬뽕','소주':'골뱅이소면'}
print(list(alcohol_foods)) # Dictionary를 List로 바꾸게 되면 Key 값만 들어오게 됨.

while True:
    alcohol = input('주문하실 술(맥주/와인/고량주/소주/아무거나/결제)은? ')
    if alcohol == '결제':
        break
    if alcohol in alcohol_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
    elif alcohol == '아무거나':
        print(random.choice(list(alcohol_foods)))
    else:
        print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요!'.format(alcohol))

# copy()
#copy_alcohol = alcohol_foods
copy_alcohol = alcohol_foods.copy()
copy_alcohol['소주'] = '두부김치'
print(alcohol_foods)
print(copy_alcohol)


# tuple : List와의 공통점은 순서를 가지고, 차이점은 immutable(불변)을 가진다. (일명 상수의 리스트)
# tuple의 원소를 정의한 후에는 추가, 삭제 수정 불가
empty = ()
numbers = (1, -9, 7)
print(type(empty))
print(numbers[1])
numbers[0] = 5

subjects = ('python', 'c++', 'english', 'math')
for subject in subjects:
    print(subject)
kim, han, tom, lee = subjects
print(kim, tom, han)

a = input()
b = input()q
# t = b
# b = a
# a = t
a, b = (b, a)   # Packing과 Unpacking을 동시에 수행
print(a, b)