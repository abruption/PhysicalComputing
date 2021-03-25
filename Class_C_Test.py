subject = input("수강 과목을 /로 구분하여 입력하세요 (총 3과목) : " ) 
subjects = subject.split("/")
print(subjects)

delsub = input("삭제과목을 입력하세요 : ")
subjects.remove(delsub)
print("삭제된 과목은 " + delsub + "입니다.")
print(subjects)
