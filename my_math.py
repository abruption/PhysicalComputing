def power(base, expo):
    """
    거듭제곱 함수
    :param base: 밑
    :param expo: 지수
    "return: 계산 결과 값
    """
    result = 1
    for k in range(expo):
        result *= base
    return result

def square(n):
    """
    제곱 함수
    :param n: 정수 1개
    :return: 제곱한 결과 값
    """
    return n * n

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

def factorial_loop(n):
    """ Factorial by 반복문 """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fizz_buzz(n1, n2):
    for i in range(n1, n2+1):
        print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

def isPrime(n):
    is_prime = True
    cnt = 2
    if n == 1:
        is_prime = False
    else:
        while cnt < n:
            if n % cnt == 0:
                is_prime == False
                break
            cnt += 1
            
    return is_prime
