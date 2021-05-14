# Database Part 2

# 1. 커넥션 열기
# 2. 커서 열기
# 3. 2에서 연 커서를 사용해서 데이터 삽입/조회/수정/삭제
# 4. 커서 닫기
# 5. 커넥션 닫기

import sqlite3

# DB 접속 후 커넥션 열기
conn = sqlite3.connect('test.db')   

# conn으로부터 커서 열기
cur = conn.cursor()                 

# DML 삽입
cur.execute("insert into students (name, subjects, city) values ('메르시', 'Python', '부산')")

# 레코드 삽입 후 커밋
conn.commit()

# 커넥션 닫기
conn.close()
