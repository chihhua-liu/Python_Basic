#demo59' Rediobutton

import tkinter
import tkinter.font
from tkinter.font import Font


def func1():
    label.config(text='Android')


def func2():
    label.config(text='iOS')


def funcx():
    if selector.get() == 1:
        label.config(text='Android')
    else:
        label.config(text='iOS')


top = tkinter.Tk()
selector = tkinter.IntVar()
selector.set(2)
font1 = Font(family='Carlito', size=32)
font2 = Font(family='Microsoft YaHei', size=28)
# change func1, func2 to funcX
rb1 = tkinter.Radiobutton(top, anchor='w', text='Google', font=font1, variable=selector, value=1, command=funcx,
                          padx=20)
rb2 = tkinter.Radiobutton(top, anchor='w', text='Apple', font=font1, variable=selector, value=2, command=funcx,
                          padx=20)
label = tkinter.Label(top, anchor='w', text="result", font=font2, padx=20, bg='#C0FFEE')
label.pack(fill='both')
rb1.pack(fill='both')
rb2.pack(fill='both')
top.minsize(400, 300)
top.maxsize(400, 300)
top.mainloop()