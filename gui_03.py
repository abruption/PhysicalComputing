# Graphic User Interface 03

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def popup():    
    if checked.get() == 0:
        #messagebox.showinfo('팝업', '체크버튼 OFF')
        lbl_display.configure(text='체크버튼 OFF')
    else:
        #messagebox.showinfo('팝업', '체크버튼 ON')
        lbl_display.configure(text='체크버튼 ON')
        
    #messagebox.showinfo('클릭', '버튼이 눌렸습니다.')
    #messagebox.showerror('클릭', '버튼이 눌렸습니다.')
    #messagebox.showwarning('클릭', '버튼이 눌렸습니다.')
    #print('버튼이 눌렸습니다.')        # Console 출력

win = tk.Tk()
win.title("팝업 실습")
win.geometry('200x100')


# btn_click = tk.Button(win, text='클릭 시 팝업', command=popup)
# btn_exit = tk.Button(win, text='종료', command=quit)

# btn_click.pack(fill='x')
# btn_exit.pack(fill='x')
# btn_exit.place(x=200, y=150)
# .grid 격자 형태 배치

checked = tk.IntVar()
cb_1 = tk.Checkbutton(win, text='체크', variable=checked, command=popup)
lbl_display = tk.Label(win, text='')
cb_1.pack()
lbl_display.pack()


win.mainloop()