# Database Exercise (Login)

# UI
# 1) 위젯 생성, 2) 위젯 레이아웃 배치


# Database
# 1) 데이터베이스 생성, 2) 테이블 생성 (ex. member), 3) DML INSERT

# Backend

import tkinter
import sqlite3
from tkinter import messagebox

def login():
    i = en_id.get()
    p = en_pw.get()
    checked = 0

    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('select * from member')
    rows = cur.fetchall()

    while(True):
        for k in range(len(rows)):
            if (rows[k][0] == i) and (rows[k][1] == p):
                checked = k
                break
        if checked != 0:
            messagebox.showinfo('로그인 성공', rows[checked][0] + '님 로그인 성공~~~')
            break
        else:
            messagebox.showerror('로그인 실패', '아이디 또는 비밀번호를 확인하세요.')
            break
    # 기존의 코드는 rows의 첫번째 순서로만 비교했기때문에 그 이후의 ID/PW는 모두 로그인 실패 처리가 발생한다.
    # 이 문제를 개선하기 위해 무한반복 While문 안에 for문을 넣어 rows의 길이만큼 반복문을 돌리고,
    # 입력한 ID/PW의 값이 rows에 존재할 경우 해당 번지를 checked 변수에 넣고 for문을 빠져나온다.

    # checked 변수의 값이 0이 아니라면 해당 값으로 DB에서 입력한 ID/PW 값이 존재한다는 의미이므로
    # messagebox에 해당 번지를 넣어 아이디를 출력하여 로그인 성공을 띄워준다.

    # 만약 checked 변수의 값이 0이라면 DB에 입력한 ID/PW이 존재하지 않으므로 로그인 실패 창을 띄운다.

    conn.commit()
    conn.close()

w = tkinter.Tk()
w.title('로그인 실습 v0.5')

lbl_id = tkinter.Label(w, text='아이디 : ')
lbl_pw = tkinter.Label(w, text='패스워드 : ')
en_id = tkinter.Entry(w)
en_pw = tkinter.Entry(w, show='*')      # 로그인 화면에서 비밀번호가 보이는 것을 방지하기 위해 *로 표시
btn_login = tkinter.Button(w, text='Login', command=login)

lbl_id.grid(row=0, column=0)
en_id.grid(row=0, column=1)
lbl_pw.grid(row=1, column=0)
en_pw.grid(row=1, column=1)
btn_login.grid(row=2, column=0, columnspan=2, sticky='nswe')

w.mainloop()