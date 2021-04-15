# Q1) 단, 소수를 리스트에 담아 출력하되 filter 함수를 사용한다. (5점)

from my_math import power, fibo_recursion, square, factorial_loop, fizz_buzz, isPrime
raw_data =[[2,16], [3,10], [6,11], [5,15]]

for i in raw_data:
    print('{0}의 {1} 거듭제곱은 {2}입니다.'.format(i[0], i[1], power(int(i[0]), int(i[1]))))
    print('{0}의 피보나치 수는 {1}입니다.'.format(i[0], fibo_recursion(int(i[0]))))
    print('{0}의 제곱은 {1}입니다.'.format(i[1], square(int(i[1]))))
    print('{0}의 팩토리얼 값은 {1}입니다.'.format(i[1], factorial_loop(int(i[1]))))
    fizz_buzz(i[0], i[1])
    result = list(filter(isPrime, i))
    print(result)