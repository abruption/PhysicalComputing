# -*- coding: utf-8 -*-

# List 02
# List 원소 삭제 (계속)
subjects= ['english', 'python', 'java']
print(subjects)
#print(subjects.remove('python'))
print(subjects.pop(1))   # pop 함수는 삭제하려는 원소 값을 리턴 후 삭제
print(subjects)
print('')

# List의 위치 출력
print(subjects.index('java'))
print('')

# List의 원소의 값 세기
subjects.append('java')
subjects.append('java')
print(subjects.count('english'))
print(subjects)
print('')

# in 키워드
print('java' in subjects)
print('')

# List 원소의 개수 리턴
subjects.insert(0, 'python')
print(len(subjects))

# 리스트를 문자열로 바꿔주는 함수 join()
subjects_string = '/'.join(subjects)
print(subjects_string)
print('')

# 문자열을 리스트로 바꿔주는 함수 split()
subjects_lists = subjects_string.split('/')
print(subjects_lists)
print('')

# 리스트 원소 정렬
#subjects.sort()     # 오픔차순 정렬 (사전순)
subjects.sort(reverse=True) # 내림차순 정렬 (사전순)
print(subjects)

list_a = [2, 3.1, 3, 1, 'python']
list_copy = sorted(list_a)
print(list_a)
print(list_copy)