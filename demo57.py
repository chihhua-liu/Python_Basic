#demo57   even used "ev"

import tkinter
import tkinter.font
from tkinter.font import Font


def func1(ev):
    label1.config(text=f'左鍵單擊 at,[{ev.x},{ev.y}]')


def func2(ev):
    label1.config(text=f'右鍵雙擊at,[{ev.x},{ev.y}]')


def func3(ev):
    label1.config(text=f'滾輪下壓後移動at,[{ev.x},{ev.y}]')


top = tkinter.Tk()
font1 = Font(family='Carlito', size=32)
font2 = Font(family='Microsoft YaHei', size=28)
label1 = tkinter.Label(top, text="show status", font=font1)
button1 = tkinter.Button(top, text="click", font=font1)
button1.bind('<Button-1>', func1)  # can sent "ev"
button1.bind('<Double-3>', func2)
button1.bind('<B2-Motion>', func3)
label1.pack()
button1.pack()
top.minsize(600, 250)
top.maxsize(600, 250)
top.mainloop()