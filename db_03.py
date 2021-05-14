# Database Part 3
import sqlite3

# DB 접속 후 커넥션 열기
conn = sqlite3.connect('test.db')

# conn으로부터 커서 열기
cur = conn.cursor()

# 명령프롬프트에서 sqlite3 실행 후 확인
# 외부 플러그인을 ide에 설치 후 확인
# 파이썬 코드 내에서 DML 조작어로 확인
cur.execute("SELECT * FROM students where subjects='Python'")

# fetchall() → 리턴은 리스트
records = cur.fetchall()
print(records)
for record in records:
    print(record)

# 레코드 삽입 후 커밋
conn.commit()

# 커넥션 닫기
conn.close()




# import sqlite3
#
# # DB 접속 후 커넥션 열기
# conn = sqlite3.connect('test.db')
#
# # conn으로부터 커서 열기
# cur = conn.cursor()
#
# # DML 삽입
# # cur.execute("insert into students (name, subjects, city) values ('메르시', 'Python', '부산')")
#
# # 다중 레코드 삽입 (excutemany)
# data = (
#     ('맥크리', 'Python', '인천'),
#     ('한조', 'C++', '서울'),
#     ('로드호그', '영어', '인천')
# )
# cur.executemany("insert into students (name, subjects, city) values (?, ?, ?)", data)

#
# # 레코드 삽입 후 커밋
# conn.commit()
#
# # 커넥션 닫기
# conn.close()
