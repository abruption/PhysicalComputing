# Q1) 안주 추천 프로그램 v0.4 (2점)

import random
alcohol_foods = {'맥주':'치킨', '와인':'치즈','고량주':'짬뽕','소주':'골뱅이소면'}

while True:
    alcohol = input('주문하실 술(맥주/와인/소주/고량주/아무거나/결제)은? ') 
    if alcohol == '결제':
        print('감사합니다. 다음 또 방문 부탁드려요~')
        break
    if alcohol in alcohol_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
    elif alcohol == '아무거나':
        any = random.choice(list(alcohol_foods))
        print('{0}를 추천합니다. 안주는 {1}~~'.format(any, alcohol_foods[any]))
    else:
        print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요!'.format(alcohol))
    