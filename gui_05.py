# Graphic User Interface 05
import tkinter as tk

def add_input():
    f = int(en_first.get())
    s = int(en_second.get())
    lbl_result.configure(text=f+s)

def enter_pressed(e):
    add_input

w = tk.Tk()
w.title('Event Handling')

w.bind('<Return>', enter_pressed)

btn_add = tk.Button(w, text='더하기', command=add_input)
lbl_result = tk.Label(w, text='결과 출력')
en_first = tk.Entry(w)
en_second = tk.Entry(w)

# Grid 배치
lbl_result.grid(row=0, column=0, columnspan=2)
en_first.grid(row=1, column=0)
en_second.grid(row=1, column=1)
btn_add.grid(row=2, column=0, columnspan=2)

w.mainloop()

# # PhotoViewer v0.3
# # 키보드 PgUP 버튼, PgDn 버튼 클릭 시 이벤트 처리
# from tkinter import *

# # 기능 구현
# def click_next():
#     global idx      # 전역변수 지정
#     idx += 1        # 다음 이미지의 index 증가
#     if idx > 2:
#         idx = 0
#     p = PhotoImage(file=photos[idx])
#     lbl_photo.configure(image=p)    # 준비
#     lbl_photo.image = p             # 붙이기
#     lbl_page_no.configure(text='{0} / {1}'.format(idx+1, len(photos)))    # str 생략 가능


# def click_prev():
#     global idx      # 전역변수 지정
#     idx -= 1        # 다음 이미지의 index 감소
#     if idx < 0:
#         idx = 2
#     p = PhotoImage(file=photos[idx])
#     lbl_photo.configure(image=p)    # 준비
#     lbl_photo.image = p             # 붙이기
#     lbl_page_no.configure(text='{0} / {1}'.format(idx+1, len(photos)))    # str 생략 가능


# def pg_up(ev):
#     click_prev()

# def pg_dn(ev):
#     click_next()

# # 전역변수 선언
# photos = ['michael.PNG', 'franklin.PNG', 'trevor.PNG']
# idx = 0

# # 메인 부분
# w = Tk()
# w.geometry('400x530')
# w.title('PhtoViewer v0.2')

# # 위젯.bind('이벤트', 이벤트리스너(=처리함수의 이름))
# w.bind('<Prior>', pg_up)    # 키보드 Page Up 버튼과 바인딩
# w.bind('<Next>', pg_dn)     # 키보드 Page Down 버튼과 바인딩

# p = PhotoImage(file='michael.PNG')
# lbl_photo = Label(w, image=p)
# btn_next = Button(w, text='다음====>', command=click_next)
# btn_prev = Button(w, text='<====이전', command=click_prev)
# lbl_page_no = Label(w, text=str(idx+1)+' / '+str(len(photos)))

# lbl_photo.pack()
# btn_next.pack(fill='x')
# btn_prev.pack(fill='x')
# lbl_page_no.pack()

# w.mainloop()




# # PhotoViewer v0.2
# from tkinter import *

# # 기능 구현
# def click_next():
#     global idx      # 전역변수 지정
#     idx += 1        # 다음 이미지의 index 증가
#     if idx > 2:
#         idx = 0
#     p = PhotoImage(file=photos[idx])
#     lbl_photo.configure(image=p)    # 준비
#     lbl_photo.image = p             # 붙이기
#     # lbl_page_no.configure(text=str(idx+1)+' / '+str(len(photos)))
#     lbl_page_no.configure(text='{0} / {1}'.format(idx+1, len(photos)))    # str 생략 가능


# def click_prev():
#     global idx      # 전역변수 지정
#     idx -= 1        # 다음 이미지의 index 감소
#     if idx < 0:
#         idx = 2
#     p = PhotoImage(file=photos[idx])
#     lbl_photo.configure(image=p)    # 준비
#     lbl_photo.image = p             # 붙이기
#     lbl_page_no.configure(text='{0} / {1}'.format(idx+1, len(photos)))    # str 생략 가능

# # 전역변수 선언
# photos = ['michael.PNG', 'franklin.PNG', 'trevor.PNG']
# idx = 0

# # 메인 부분
# w = Tk()
# w.geometry('400x530')
# w.title('PhtoViewer v0.2')

# p = PhotoImage(file='michael.PNG')
# lbl_photo = Label(w, image=p)
# btn_next = Button(w, text='다음====>', command=click_next)
# btn_prev = Button(w, text='<====이전', command=click_prev)
# lbl_page_no = Label(w, text=str(idx+1)+' / '+str(len(photos)))

# lbl_photo.pack()
# btn_next.pack(fill='x')
# btn_prev.pack(fill='x')
# lbl_page_no.pack()

# w.mainloop()