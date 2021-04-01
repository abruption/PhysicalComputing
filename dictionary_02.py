# Dictorionary (cont.)

# keys() → Key 값만 출력
fruits = {
    'apple':'사과', 
    'watermelon':'수박',
    'strawberry':'딸기',
    'kiwi':'키위',
    'banana':'버내너'} 

for k, v in fruits.items():
    print(k, '\t', v)   # 키값 + Tab + Value 출력

print(fruits.keys())

# values() → Value 값만 출력
print(fruits.values())

# items() → Key와 Value 세트로 출력
print(fruits.items())


# 안주 추천 프로그램 v0.1
alcohol_foods = {'맥주':'치킨', '와인':'치즈','고량주':'짬뽕','소주':'골뱅이소면'}
alcohol = input('주문하실 술(맥주/와인/고량주/소주)은? ')

if alcohol in alcohol_foods.keys():
    print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))


# 안주 추천 프로그램 v0.2
alcohol_foods = {'맥주':'치킨', '와인':'치즈','고량주':'짬뽕','소주':'골뱅이소면'}

while True:
    alcohol = input('주문하실 술(맥주/와인/고량주/소주)은? ')
    if alcohol == '결제':
        break

    if alcohol in alcohol_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
    else:
        print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요!'.format(alcohol))