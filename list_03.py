#-*- coding: utf-8 -*-

# List 03
# 리스트 복사
my_utube = ['악뮤', '볼사', '코노', '언더독', '홍수웅', '빅뱅']
ur_utube = my_utube[0:5]

print(ur_utube)
del my_utube[-1]
my_utube.append('태양')
print(my_utube)
print()


a = [2, 3, 1, 5]
#b = a   # 공유
#b = a[0:]   # Slicing 0은 시작 index, : 뒤에 빈칸은 끝까지라는 의미
#b = a.copy()
b = list(a)
print(b)
b[-2] = 4
print(b)
print(a)
print(id(a), id(b))
print()

ur_friends = ['릴러밀즈', '슈퍼비']
#friends = my_utube[2:5]
#friends = my_utube[-4:-1]
#friends = my_utube[2:-1]
#friends = my_utube[-4:5]
friends = my_utube[2:len(my_utube)-1]
print(friends)

friends.extend(ur_friends)
print(friends)