# Graphic User Interface 04

# PhotoViewer v0.1
from tkinter import *

# 기능 구현
def click_next():
    global idx      # 전역변수 지정
    idx += 1        # 다음 이미지의 index 증가
    if idx > 2:
        idx = 0
    p = PhotoImage(file=photos[idx])
    lbl_photo.configure(image=p)    # 준비
    lbl_photo.image = p             # 붙이기


def click_prev():
    global idx      # 전역변수 지정
    idx -= 1        # 다음 이미지의 index 감소
    if idx < 0:
        idx = 2
    p = PhotoImage(file=photos[idx])
    lbl_photo.configure(image=p)    # 준비
    lbl_photo.image = p             # 붙이기

# 전역변수 선언
photos = ['michael.PNG', 'franklin.PNG', 'trevor.PNG']
idx = 0

# 메인 부분
w = Tk()
w.geometry('400x510')
w.title('PhtoViewer v0.1')

p = PhotoImage(file='michael.PNG')
lbl_photo = Label(w, image=p)
btn_next = Button(w, text='다음====>', command=click_next)
btn_prev = Button(w, text='<====이전', command=click_prev)

lbl_photo.pack()
btn_next.pack(fill='x')
btn_prev.pack(fill='x')

w.mainloop()



# import tkinter as tk

# def popup():    
#     if seleted.get() == 0:
#         lbl_display.configure(text='리트리버')
#     elif seleted.get() == 1:
#         lbl_display.configure(text='허스키')
#     else:
#         lbl_display.configure(text='웰시코기')

# win = tk.Tk()
# win.title("라디오 버튼 실습")
# win.geometry('300x150')

# seleted = tk.IntVar()
# lbl_display = tk.Label(win, text='선택할 견종은?')
# rb_1 = tk.Radiobutton(win, text='리트리버', variable=seleted, value=0, command=popup)
# rb_2 = tk.Radiobutton(win, text='허스키', variable=seleted, value=1, command=popup)
# rb_3 = tk.Radiobutton(win, text='웰시코기', variable=seleted, value=2, command=popup)

# lbl_display.pack()
# rb_1.pack()
# rb_2.pack()
# rb_3.pack()

# win.mainloop()