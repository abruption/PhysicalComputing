import tkinter
import sqlite3
from tkinter import messagebox

def insert():
    ids = en_id.get()
    name = en_userName.get()
    try:
        birth = int(en_birthYear.get())
        checked = 0

        conn = sqlite3.connect('inhaDB.db')
        cur = conn.cursor()
        cur.execute('select * from userTable')
        rows = cur.fetchall()
        while(True):
            for k in range(len(rows)):
                if rows[k][0] == ids:
                    checked = k
                    break
            if checked != 0:
                messagebox.showerror('실패', '데이터 입력 실패')
                break
            else:
                cur.execute('insert into userTable (id, userName, birthYear) values (?, ?, ?)', (ids, name, birth))
                messagebox.showinfo('성공', '데이터 입력 성공')
                break
        conn.commit()
        conn.close()

    except Exception:
        messagebox.showerror('실패', '데이터 입력 실패')



def search():
    id = ''
    name = ''
    birth = ''

    conn = sqlite3.connect('inhaDB.db')
    cur = conn.cursor()
    cur.execute('select * from userTable')
    rows = cur.fetchall()

    for k in range(len(rows)):
        id += rows[k][0] + '\n'
        name += rows[k][1] + '\n'
        temp = str(rows[k][2]) + '\n'
        birth += temp

    lbl_id.configure(text='환자 ID' + '\n' + '--------' + '\n' + id)
    lbl_name.configure(text='환자 이름' + '\n' + '--------' + '\n' + name)
    lbl_year.configure(text='출생연도' + '\n' + '--------' + '\n' + birth)

    conn.commit()
    conn.close()

def enter_pressed(e):
    insert()

w = tkinter.Tk()
w.title('기말고사A : 201644091 / 이연국')
w.bind('<Return>', enter_pressed)

en_id = tkinter.Entry(w)
en_userName = tkinter.Entry(w)
en_birthYear = tkinter.Entry(w)
btn_insert = tkinter.Button(w, text='입력', command=insert)
btn_search = tkinter.Button(w, text='조회', command=search)
lbl_id = tkinter.Label(w, text='환자 ID' + '\n' + '--------', font='Arial 20',  bg='green')
lbl_name = tkinter.Label(w, text='환자 이름' + '\n' + '--------', font='Arial 20', bg='gray')
lbl_year = tkinter.Label(w, text='출생연도' + '\n' + '--------', font='Arial 20', bg='red')


en_id.grid(row=0, column=0)
en_userName.grid(row=0, column=1)
en_birthYear.grid(row=0, column=2)
btn_insert.grid(row=0, column=3, sticky='w')
btn_search.grid(row=0, column=4, sticky='w')
lbl_id.grid(row=1, column=0, columnspan=2)
lbl_name.grid(row=1, column=2, columnspan=2)
lbl_year.grid(row=1, column=3, columnspan=2)
w.mainloop()