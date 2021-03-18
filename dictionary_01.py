# Dictionary

# List와 비슷하나 순서를 따지지 않는다.
# 키와 값이 pair가 원소가 된다.

fruits = {'apple':'사과', 'watermelon':'수박'} 
print(fruits['watermelon'])
print(fruits)

fruits['banana'] ='바나나'  # 삽입
print(fruits)

fruits['kiwi'] = '키위'    # 삽입
print(fruits)

fruits['kiwi'] ='키위'     # 수정
print(fruits)

empty = {}
print(type(fruits), type(empty))

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
fruits.update(others)   
print(fruits)

# del → 삭제
# del fruits → 딕셔너리를 삭제
del fruits['apple'] # 원소 1개 삭제
print(fruits)

# clear → 원소 전부 삭제
fruits.clear()
print(fruits)