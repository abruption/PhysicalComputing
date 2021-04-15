# file io (cont.)

# 안주 추천 프로그램 v0.4
import random
alcohol_foods = {}

with open('alcohols.txt', 'r') as fp1:
    with open('foods.txt', 'r') as fp2:
        alcohols = fp1.readlines()  # 리스트 변수 alcohols
        foods = fp2.readlines()     # 리스트 변수 foods
        for k in range(len(alcohols)):
            for j in range(len(foods)):
                alcohol_foods[alcohols[k].strip('\n')] = foods[k][0:-1]     # strip 함수와 Slicing 기법 사용

while True:
    alcohol = input('주문하실 술(맥주/와인/고량주/소주/아무거나/결제)은? ')
    if alcohol == '결제':
        break
    if alcohol in alcohol_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
    elif alcohol == '아무거나':
        any = random.choice(list(alcohol_foods))
        print('{0}을 추천합니다. 안주는 {1}입니다.'.format(any, alcohol_foods[any]))
    else:
        print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요!'.format(alcohol))