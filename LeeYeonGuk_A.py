import random

def plus(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def gob(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 // n2

question = 0
answer = 0

print('사칙연산 암산게임 시작 (A-이연국)')
while True:
    mode = input('원하는 사칙연산을 선택하세요 (+ : 1, - : 2, * : 3, / : 4, 랜덤 : 5) : ')
    if mode == '1':
        question += 1
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        print('{0} + {1} = ?'.format(a, b))
        result = input()
        if int(result) == plus(a, b):
            answer += 1
            print('결과 : 정답입니다.\n계속 하시겠습니까? YES = 1, NO = 2')
            cont = input()
            if cont == '1':
                continue
            elif cont == '2':
                break
            else:
                con = input('1 또는 2의 수를 입력하세요.\n')
                if cont == '1':
                    continue
                elif cont == '2':
                    break
        else:
            print('결과 : 오답입니다.')
            cont = input('계속 하시겠습니까? YES = 1, NO = 2')
            if cont == '1':
                continue
            elif cont == '2':
                break
            else:
                con = input('1 또는 2의 수를 입력하세요.\n')
                if cont == '1':
                    continue
                elif cont == '2':
                    break

    elif mode == '2':
        question += 1
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        print('{0} - {1} = ?'.format(a, b))
        result = input()
        if int(result) == minus(a, b):
            answer += 1
            print('결과 : 정답입니다.\n계속 하시겠습니까? YES = 1, NO = 2')
            cont = input()
            if cont == '1':
                continue
            elif cont == '2':
                break
            else:
                con = input('1 또는 2의 수를 입력하세요.\n')
                if cont == '1':
                    continue
                elif cont == '2':
                    break
        else:
            print('결과 : 오답입니다.')
            cont = input('계속 하시겠습니까? YES = 1, NO = 2')
            if cont == '1':
                continue
            elif cont == '2':
                break
            else:
                con = input('1 또는 2의 수를 입력하세요.\n')
                if cont == '1':
                    continue
                elif cont == '2':
                    break

    elif mode == '3':
        question += 1
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        print('{0} * {1} = ?'.format(a, b))
        result = input()
        if int(result) == gob(a, b):
            answer += 1
            print('결과 : 정답입니다.\n계속 하시겠습니까? YES = 1, NO = 2')
            cont = input()
            if cont == '1':
                continue
            elif cont == '2':
                break
            else:
                con = input('1 또는 2의 수를 입력하세요.\n')
                if cont == '1':
                    continue
                elif cont == '2':
                    break
        else:
            print('결과 : 오답입니다.')
            cont = input('계속 하시겠습니까? YES = 1, NO = 2')
            if cont == '1':
                continue
            elif cont == '2':
                break
            else:
                con = input('1 또는 2의 수를 입력하세요.\n')
                if cont == '1':
                    continue
                elif cont == '2':
                    break

    elif mode == '4':
        question += 1
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        print('{0} / {1} = ?'.format(a, b))
        result = input()
        if int(result) < 0:
            reinput = input('정수만 입력하세요.\n')
            if int(reinput) == div(a,b):
                answer += 1
                print('결과 : 정답입니다.\n계속 하시겠습니까? YES = 1, NO = 2')
                cont = input()
                if cont == '1':
                    continue        
                elif cont == '2':
                    break
                else:
                    con = input('1 또는 2의 수를 입력하세요.\n')
                    if cont == '1':
                        continue
                    elif cont == '2':
                        break

        elif int(result) == div(a, b):
            answer += 1
            print('결과 : 정답입니다.\n계속 하시겠습니까? YES = 1, NO = 2')
            cont = input()
            if cont == '1':
                continue
            elif cont == '2':
                break
            else:
                con = input('1 또는 2의 수를 입력하세요.\n')
                if cont == '1':
                    continue
                elif cont == '2':
                    break
        else:
            print('결과 : 오답입니다.')
            cont = input('계속 하시겠습니까? YES = 1, NO = 2')
            if cont == '1':
                continue
            elif cont == '2':
                break
            else:
                con = input('1 또는 2의 수를 입력하세요.\n')
                if cont == '1':
                    continue
                elif cont == '2':
                    break

    elif mode == '5':
        question += 1
        temp = random.randint(1, 4)
        if temp == 1:
            a = random.randint(1, 99)
            b = random.randint(1, 99)
            print('{0} + {1} = ?'.format(a, b))
            result = input()
            if int(result) == plus(a, b):
                answer += 1
                print('결과 : 정답입니다.\n계속 하시겠습니까? YES = 1, NO = 2')
                cont = input()
                if cont == '1':
                    continue
                elif cont == '2':
                    break
                else:
                    con = input('1 또는 2의 수를 입력하세요.\n')
                    if cont == '1':
                        continue
                    elif cont == '2':
                        break

            else:
                print('결과 : 오답입니다.')
                cont = input('계속 하시겠습니까? YES = 1, NO = 2')
                if cont == '1':
                    continue
                elif cont == '2':
                    break
                else:
                    con = input('1 또는 2의 수를 입력하세요.\n')
                    if cont == '1':
                        continue
                    elif cont == '2':
                        break
            
        elif temp == 2:
            a = random.randint(1, 99)
            b = random.randint(1, 99)
            print('{0} - {1} = ?'.format(a, b))
            result = input()
            if int(result) == minus(a, b):
                answer += 1
                print('결과 : 정답입니다.\n계속 하시겠습니까? YES = 1, NO = 2')
                cont = input()
                if cont == '1':
                    continue
                elif cont == '2':
                    break
                else:
                    con = input('1 또는 2의 수를 입력하세요.\n')
                    if cont == '1':
                        continue
                    elif cont == '2':
                        break
            else:
                print('결과 : 오답입니다.')
                cont = input('계속 하시겠습니까? YES = 1, NO = 2')
                if cont == '1':
                    continue
                elif cont == '2':
                    break
                else:
                    con = input('1 또는 2의 수를 입력하세요.\n')
                    if cont == '1':
                        continue
                    elif cont == '2':
                        break

        elif temp == 3:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            print('{0} * {1} = ?'.format(a, b))
            result = input()
            if int(result) == gob(a, b):
                answer += 1
                print('결과 : 정답입니다.\n계속 하시겠습니까? YES = 1, NO = 2')
                cont = input()
                if cont == '1':
                    continue
                elif cont == '2':
                    break
                else:
                    con = input('1 또는 2의 수를 입력하세요.\n')
                    if cont == '1':
                        continue
                    elif cont == '2':
                        break
            else:
                print('결과 : 오답입니다.')
                cont = input('계속 하시겠습니까? YES = 1, NO = 2')
                if cont == '1':
                    continue
                else:
                    break

        elif temp == 4:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            print('{0} / {1} = ?'.format(a, b))
            result = input()
            if int(result) < 0:
                reinput = input('정수만 입력하세요.')
                if int(reinput) == div(a,b):
                    answer += 1
                    print('결과 : 정답입니다.\n계속 하시겠습니까? YES = 1, NO = 2')
                    cont = input()
                    if cont == '1':
                        continue        
                    elif cont == '2':
                        break
                    else:
                        con = input('1 또는 2의 수를 입력하세요.\n')
                        if cont == '1':
                            continue
                        elif cont == '2':
                            break

            elif int(result) == div(a, b):
                answer += 1
                print('결과 : 정답입니다.\n계속 하시겠습니까? YES = 1, NO = 2')
                cont = input()
                if cont == '1':
                    continue
                elif cont == '2':
                    break
                else:
                    con = input('1 또는 2의 수를 입력하세요.\n')
                    if cont == '1':
                        continue
                    elif cont == '2':
                        break
            else:
                print('결과 : 오답입니다.')
                cont = input('계속 하시겠습니까? YES = 1, NO = 2')
                if cont == '1':
                    continue
                else:
                    break
    else:
        print('올바른 값을 입력하세요.')


per = ((answer / question) * 100)
percent = round(per, 2)
with open('LeeYeonGuk_A.txt', 'a') as fp:
    print('총 문제 수 : {0}회, 정답수 : {1}회, 정답률 : {2}%'.format(question, answer, percent))
    fp.write('총 문제 수 : {0}회, 정답수 : {1}회, 정답률 : {2}%\n'.format(question, answer, percent))