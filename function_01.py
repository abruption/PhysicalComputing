# 함수 (Function) : 한 가지 작업을 수행하도록 디자인된 코드블럭 or 코드의 집합

def test(name):
    print('Hi ' + name)
    return '이름을 출력함'

test('파이썬')  # Function Call
print(test('C++'))

def minus(a, b):
    """ 
    두 수의 차를 구하는 함수 
    매개변수는 a와 b로 받음
    """
    return a - b

print(minus(5,3, 99))
help(minus)
print(minus.__doc__)


# 가변 매개변수
def print_even(times, *values):
    for value in values:
        print(times * value)

print_even(2, -9, 11, 7)


# 기본 매개변수
def print_default(value, times=3):
    print(times * value)

print_default(12, 5)