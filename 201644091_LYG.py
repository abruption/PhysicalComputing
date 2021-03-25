num1 = int(input("첫 번째 정수 입력 : "))
num2 = int(input("두 번째 정수 입력 : "))

for i in range(1, 51):
    if (i % num1 == 0) and (i % num2 == 0):
        print("{0} {1} 공배수 {2}".format(num1, num2, i))
    elif i % num1 == 0:
        print("{0}의 배수".format(num1))
    elif i % num2 == 0:
        print("{0}의 배수".format(num2))
    else:
        print(i)