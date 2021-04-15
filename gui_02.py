# Graphic User Interface 02

from tkinter import *
from PIL import Image, ImageTk

window = Tk()  # 윈도우 객체 생성
window.title('레이블 실습 : 이미지')    # 제목 표시줄

# .png / .gif 지원
# .jpg / .bmp 등등 PIL (Photo Image Library) 별도 설치 후 사용

# 이미지 준비
p1 = PhotoImage(file='dog.png')
p2 = PhotoImage(file='dog.png')
p3 = PhotoImage(file='dog.png')

# 이미지 레이블 생성 및 바인딩
lbl_display1 = Label(window, image=p1)
lbl_display2 = Label(window, image=p2)
# btn_display3 = Button(window, text='클릭')
btn_display3 = Button(window, image=p3)

# 윈도우에 레이블 부착
lbl_display1.pack()
lbl_display2.pack()
btn_display3.pack()
# btn_display3.pack(fill='x')

window.mainloop()
