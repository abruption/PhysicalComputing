# Q1) Dictionary (2점)
# 김인하는 ITAEWON CLASS 등장인물이 아닙니다. 다시 입력해주세요.

import random
iclass = {
    '박새로이':('박서준','단밤'),
    '조이서':('김다미','단밤'),
    '장대희':('유재명','장가'),
    '오수아':('권나라','장가')}
print("----- ITAEWON CLASS -----")
name = input('iclass 등장인물 : ')

if name in iclass.keys():
    print(iclass[name][1] + ' ' + iclass[name][0])
elif name == '랜덤으로':
    name = random.choice(list(iclass))
    print(iclass[name][1] + ' ' + iclass[name][0])
else:
    print(name + '은 ITAEWON CLASS 등장인물이 아닙니다. 다시 입력해주세요.')