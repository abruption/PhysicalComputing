# 안주 추천 프로그램 v0.5
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
    alcohol = input('주문하실 술(' + '/'.join([alcohol.rstrip('\n') for alcohol in alcohols]) + '/아무거나/결제)은? ')
    if alcohol == '결제':
        break
    if alcohol in alcohol_foods.keys():
        print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
    elif alcohol == '아무거나':
        any = random.choice(list(alcohol_foods))
        print('{0}을 추천합니다. 안주는 {1}입니다.'.format(any, alcohol_foods[any]))
    else:
        print('{0}는 판매하지 않습니다. 메뉴에서 골라주세요!'.format(alcohol))




# exception handling (cont.)

def midterm():
    score = int(input('1에서 10 사이의 정수 입력 : '))
    if (score <= 0) or (score > 10):
        raise Exception('입력하신 {0}은 중간고사 점수 입력 범위를 벗어났습니다.'.format(score))
    else:
        print('{0}점 입니다.'.format(score))


try:
    midterm()
except Exception as e:
    print('예외 발생 : {0}'.format(e))


try:
    print(5/2)
    b = int(input('첫 번째 수를 입력해주세요 : '))
    a = [1, 2, 3]
    print(a[1])
    raise Exception('내가 만든 예외')
except ZeroDivisionError as e:
    print('분모에 0이 올 수 없습니다. : {0}'.format(e))
except IndexError as e:
    print('인덱스 범위를 벗어났습니다. : {0}'.format(e))
except Exception as e:  # 맨 마지막에 작성
    print('무언가 에러가 발생했습니다. : {0}'.format(e))