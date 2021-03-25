school = input("재학중인 학교는? ")
temp = school.lower()
_temp = temp.title()
print(_temp+" 대학교에 다니시는군요!")
grade = input("몇 학년이세요? ")
if(int(grade)==1) or (int(grade)==2):
    print("저학년이네요.")
if (int(grade)==3):
    print(grade+"년째 재학중인 고학년이네요.")
if (int(grade)>3):
    print("학교를 오래다니고 계시네요. 졸업을 기원합니다.")

    
