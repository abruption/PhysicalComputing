# 함수 (Function cont.)

# factorial
# 5! = 5 x 4 x 3 x 2 x 1

def factorial_recursion(n):
    """
    Factorial by 재귀함수 
    f(n) = n * f(n-1)
    f(3) = 3 * f(2)
         = 3 * 2 * f(1)
         = 3 * 2 * 1 * f(0)
         = 3 * 2 * 1 * 1
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursion(n-1)
print(factorial_recursion(4))
print(factorial_recursion(6))




def factorial_loop(n):
    """ Factorial by 반복문 """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial_loop(4))
print(factorial_loop(6))


# Fibonacci : 성능 상의 문제가 있음 (해결 방법 중 하나가 메모화)
def fibo_recursion(n):
    """
    f(n) = f(n-1) + f(n-2)
    f(1) =1
    f(2) = 2
    """
    if (n == 1) or (n == 2):
        return 1
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)

for k in range(1, 8):
    print('Fibonacci {0} : {1}'.format(k, fibo_recursion(k)))


# 함수의 매개변수로 함수 전달하기
def print_hi(hi):
    for k in range(5):
        hi()

def hi():
    print('Hello~')

# hi()
print_hi(hi)


# map(함수, 순환가능한 자료구조)
# List, Dictionary, 문자열, 범위 range
def square(n):
    return n * n

def odd(n):
    return n % 2 == 1

result = []
for k in range(1, 6):
    result.append(square(k))
print(result)
# print(list(map(square, [1,2,3,4,5])))

# filter(함수, 순환가능한 자료구조)
print(list(filter(odd, [1,2,3,4,5])))

# 람다함수, 제너레이터