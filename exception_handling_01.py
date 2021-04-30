# exception handling

# try:
    # 예외가 발생할 가능성이 있는 코드
# except:
    # 예외가 발생했을 때 실행할 코드
# else:
    # 예외가 발생하지 않았을 때 실행할 코드
# finally:
    # 무조건 실행할 코드 (예외 발생 여부 X)

try:
    c = list()
    c.append('사과')
    a = int(input('첫 번째 수 입력 : '))
    b = int(input('두 번째 수 입력 : '))
    print(a/b)
    print(c[0])
except ZeroDivisionError:
    print('분모에 0이 올 수 없습니다.')
except ValueError:
    print('입력된 수는 정수가 아닙니다!')
except IndexError:
    print('리스트의 범위를 벗어난 인덱스가 사용되었습니다.')
except:
    print('무언가 에러가 발생했습니다.')        # 나머지 모든 Exception이 여기서 처리됨.
else:
    print('정상적으로 처리되었습니다.')         # 예외 발생이 되지 않았을 경우 여기서 처리됨
finally:
    print('예외 발생 여부에 상관없이 항상 실행됩니다.') # 예외 발생 여부와 상관없이 항상 실행됨.



# a = input('첫 번째 수 입력 : ')
# b = input('두 번째 수 입력 : ')

# if a.isdigit() and b.isdigit(): # 마이너스 정수를 문자열로 인식하는 문제가 발생
#     print(int(a)+int(b))
# else:
#     print('입력된 수는 정수가 아닙니다.')