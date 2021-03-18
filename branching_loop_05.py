# While

r = list(range(1, 6))
print(r)

for k in range(1, 6, 1):
    print(k, end=' ')

k = 1
while k <= 5:
    print(k, end=' ')
    k += 1


# FizzBuzz Test
n = 1
while n < 101:
    output = n
    if(n % 3 == 0) and (n % 5 == 0):
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
    n += 1

for n in range(1, 101):
    if(n % 3 == 0) and (n % 5 == 0):
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

while True:
    answer = input('런던, 파리, 서울 중 영국의 수도는? ')
    if answer == '런던':
        print('정답입니다. Outstanding!') 
        break   # 반복을 종료하는 키워드
    elif answer == '파리':
        print('파리는 프랑스의 수도입니다.')
    elif answer == '서울':
        print('서울은 대한민국의 수도입니다.')
    else:
        print('보기에서 골라주세요.')


count = 0
while count < 6:
    count += 1
    if count == 3:
        continue    # 반복의 처음으로 돌아가는 키워드
    print(count)