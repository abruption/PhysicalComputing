# -*- coding: utf-8 -*- 


# 자료형 (Data types)
# 문자열 (String)
print("Hello World!")
print("Hello "+"파이썬")
#print("Hello "-"파이썬")   # TypeError
#print("Hello "*"파이썬")   # TypeError
print("Hello "*5)


# 숫자형 (정수, 실수)
# 정수애 대한 연산
print(1+2)
print(1-2)
print(1*2)
print(1/2)
print(11//2)    # 몫
print(11%2)     # 나머지
print(2**8)     # 거듭제곱
print(pow(2,8)) # 거듭제곱 함수 사용

# 문자열에 대한 연산
print('1'+'2')

# 문자열과 숫자의 연산
#print(1+'2')    # TypeError 발생

# 실수에 대한 연산
# 실수는 부동소수점 방식을 쓰기때문에 오차가 발생할 수 있다.
print(1.2+1.4)
print(5.1-2.9)
print(1.5*2.0)
print(10.0/2.5)