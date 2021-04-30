# -*- coding: utf-8 -*- 

# 자료형 (cont.)
# 문자열 함수
words = 'Life is too short,\nYou need\t Python'

temp = words.title()    # 각 단어의 첫 글자를 대문자로
print(temp)

_temp = words.lower()   # 모두 소문자로
print(_temp)

__temp = words.upper()  # 모두 대문자로
print(__temp)
print('')

# strip() 
trim1 = 'Python'
trim2 = '   Python  '
trim3 = '&&&Python&&&'
trim4 = '&&&pyt&on&&'
print(trim1)                # Python
print(trim2.strip())        # Python → 공백이 들어간 모든 문자를 제거함
print(trim3.strip('&'))     # Python → &이 들어간 모든 문자를 제거함.
print(trim3.rstrip('&'))    # &&&Python → rstrip은 우측에 있는 것만 제거해줌.
print(trim3.lstrip('&'))    # Python&&& → lstrip은 좌측에 있는 것만 제거해줌.
print(trim4.strip())        # &&&pyt&on&& → 문자 중간에 있는 특수문자는 제거하지 못함.
print('')

# str()
print('1' + "hi")           # 1hi
print(str(1) + "hi")        # 1hi

# int()
a = '1'
b = 2
print(int(a) + b)           

# input()
#name = input('이름을 입력하세요 : ')
#print('안녕 ' + name)
#print('안녕', name)

celsius = input('섭씨 온도 : ')
fahrenheit = (int(celsius) * 9/5) + 32
print(fahrenheit)
