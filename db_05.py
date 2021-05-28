# Database Part 5

# 안주 추천 프로그램 v1.2
# Database II
import tkinter as tk
import random as rd
import sqlite3

### Backend ###
def menu_choice():
    """ Menu 선택 기능 """
    alcohol = en_menu.get()
    if alcohol == '결제':
        exit()

    elif alcohol == '아무거나':
        conn = sqlite3.connect('test.db')
        cur = conn.cursor()

        cur.execute('select alcohols from pub')
        records = cur.fetchall()
        conn.commit()
        # conn.close()

        any = rd.choice(records[0])

        # conn = sqlite3.connect('test.db')
        # cur = conn.cursor()

        cur.execute('select foods from pub where alcohols=?', (any,))
        records = cur.fetchall()
        conn.commit()
        conn.close()
        lbl_display.configure(text='{0}에 어울리는 안주는 {1}입니다.'.format(any, records[0][0]))

    else:
        try:
            conn = sqlite3.connect('test.db')
            cur = conn.cursor()

            cur.execute('select foods from pub where alcohols=?', (alcohol,))
            records = cur.fetchall()

            conn.commit()
            conn.close()
            lbl_display.configure(text='{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, records[0][0]))
        except IndexError:
            lbl_display.configure(text='{0}는 판매하지 않습니다. 메뉴에서 골라주세요~'.format(alcohol))


def connect_db():
    """ Database 접속 기능 및 화면 Display 기능 """
    menu = ''

    conn = sqlite3.connect('test.db')
    cur = conn.cursor()

    cur.execute('select alcohols from pub')
    records = cur.fetchall()
    for k in range(len(records)):       # 출력 결과 : 주문하실 술(맥주/소주/고량주/위스키/아무거나/결제)은?
        menu += str(records[k][0]) + '/'

    conn.commit()
    conn.close()

    lbl_display.configure(text='주문하실 술(' + menu + '아무거나/결제)은?')

def enter_pressed(e):
    """ 키보드 엔터키 이벤트 리스너 """
    menu_choice()



#### FrontEnd ####
if __name__ == "__main__":
    w = tk.Tk()
    w.title('안주 추천 프로그램 v1.0')

    # 엔터키 이벤트 바인딩
    w.bind('<Return>', enter_pressed)

    # 위젯 생성
    lbl_display = tk.Label(w, text='Display', font='Arial 20')
    en_menu = tk.Entry(w)
    btn_menu = tk.Button(w, text='실행', command=menu_choice)

    # 위젯 배치 (Grid 레이아웃)
    lbl_display.grid(row=0, column=0, columnspan=2)
    en_menu.grid(row=1, column=0, sticky='nswe')
    btn_menu.grid(row=1, column=1, sticky='nswe')

    connect_db()

    w.mainloop()