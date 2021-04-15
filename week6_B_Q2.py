# Q2) 두 수(범위)를 매개변수로 갖는 fizz_buzz 함수를 설계합니다.
# 두 수의 입력방식은 설명을 참고합니다.
# 단, print 함수는 최소화 합니다. (3점)

# Option 1
def fizz_buzz(n1, n2):
    for i in range(n1, n2+1):
        print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)

a, b = map(input, input().split())
fizz_buzz(a, b)



# Option 2
def FizzBuzz(n1, n2):
    output = []
    for n in range(n1, n2+1):
        if (n % 3 == 0) and (n % 5 == 0):
            output.append('FizzBuzz')
        elif n % 3 == 0:
            output.append('Fizz')
        elif n % 5 == 0:
            output.append('Buzz')
        else:
            output.append(str(n))
        return output

num = input()
nlist = num.split(' ')
n1 = int(nlist[0])
n2 = int(nlist[1])
if n1 > n2:
    n1, n2 = n2, n1
print('\n'.join(FizzBuzz(n1, n2)))



# Option 3
def Fizz_Buzz(n):
    if (n % 3 == 0) and (n % 5 == 0):
        return 'FizzBuzz'
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

start_end = input()
start, end = start_end.split(' ')
for i in range(int(start), int(end)+1):
    print(Fizz_Buzz(i))
