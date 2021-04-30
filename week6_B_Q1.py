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
    # 키 값(name)에 맞는 Value를 출력한다. (회사명 + 본명)
    print(iclass[name][1] + ' ' + iclass[name][0])
elif name == '랜덤으로':
    # iclass를 리스트로 변환하여 키 값을 name에 저장하고 이 값을 통해 Value를 출력한다. (회사명 + 본명)
    name = random.choice(list(iclass))
    print(iclass[name][1] + ' ' + iclass[name][0])
else:
    # 딕셔너리에 Key 값이 존재하지 않을 경우 else 구문을 출력한다.
    print(name + '은 ITAEWON CLASS 등장인물이 아닙니다. 다시 입력해주세요.')