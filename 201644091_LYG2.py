price = 0
kids = 0
mids = 0
adults = 0
humans = int(input('몇 분이 오셨죠? '))
ages = [int(input('나이는? ')) for i in range(humans)]

for age in ages:
    if age < 8:
        price += 5000
        kids += 1
    elif 8<= age < 19:
        price += 9000
        mids += 1
    elif age >= 19:
        price += 11000
        adults +=1

print('=' * 50)
print('총 인원 : {0}명 (어린이 : {1}, 청소년 : {2}, 성인 : {3})'.format(humans, kids, mids, adults))
print('총 금액 : {0}원'.format(price))