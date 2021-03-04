# -*- coding: utf-8 -*-

# List
# List는 특정 순서가 있는 항목의 모음
# 대괄호([])와 쉼표(,) 기호를 사용합니다.

# List 생성
empty_lists = list()
subjects = ['english', 'python', 'java']
print(type(empty_lists))
print(type(subjects))
print(empty_lists)
print(subjects)
# print(type(5))
# print(type(5.7))
# print(type('python'))
print('')

# List Indexing
print(subjects[1])
print(subjects[-2])
print('') 

# List Add, Insert
subjects.append('C++')
subjects.insert(2, 'math')
print(subjects)
print(subjects[1])
print(subjects[-2])
print('')

# List Item Edit
subjects[3] = 'assembly'
print(subjects)
print('')

# List Item Remove
#del subjects[-1]
#del subjects[4]
#subjects.pop()  # 맨 뒤의 원소 삭제
#subjects.append('math')
#print(subjects)
subjects.remove('math') # 중복 원소일 때 맨 앞의 원소만 삭제
print(subjects)