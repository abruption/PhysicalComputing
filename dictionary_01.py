# Dictionary

# List와 비슷하나 순서를 따지지 않는다.
# 키와 값이 pair가 원소가 된다.

fruits = {'apple':'사과', 'watermelon':'수박'} 
print(fruits['watermelon'])
print(fruits)

fruits['banana'] ='바나나'  # 삽입 : 중복되는 Key 값이 없을 경우 삽입된다.
print(fruits)

fruits['kiwi'] = '키위'    # 삽입 : 중복되는 Key 값이 없을 경우 삽입된다.
print(fruits)

fruits['kiwi'] ='키위'     # 수정 : 중복되는 Key 값이 있을 경우 수정된다.
print(fruits)

empty = {}
print(type(fruits), type(empty))    # 둘다 dict 타입이다.

# dict() → 딕셔너리 변환 함수
test = [['python', '3'], ['english', '2'], ['dance', '1']]
print(test[1])      # ['english', 2] 
print(test[1][0])   # english
print(test[1][1])   # 2
print(dict(test))   # Dictionary 형태로 출력

_test = ['ab', 'cd', 'ef']
print(_test[1])      # cd
print(_test[1][0])   # c
print(_test[1][1])   # d
print(dict(_test))   # Dictionary 형태로 출력


# update() → 결합
fruits = {'apple':'사과', 'watermelon':'수박'} 
fruits['banana'] ='바나나'  # 삽입
 
others = {'strawberry':'딸기', 'kiwi':'키위', 'banana':'버내너'}
fruits.update(others)   # fruits와 other가 결합한다. 단, 중복되는 Key 값이 있을경우 마지막 딕셔너리의 값으로 치환된다.
print(fruits)

# del → 삭제
# del fruits → 딕셔너리를 삭제
del fruits['apple'] # 원소 1개 삭제
print(fruits)

# clear → 원소 전부 삭제
fruits.clear()
print(fruits)