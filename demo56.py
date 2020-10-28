#demo56

import tkinter
import tkinter.font
from tkinter.font import Font


def func1(ev):
    label1.config(text='cursor in label2')


def func2(ev):
    label1.config(text='cursor leave label2')


top = tkinter.Tk()
font1 = Font(family='Carlito', size=32)
font2 = Font(family='Microsoft YaHei', size=28)
label1 = tkinter.Label(top, text='display status', font=font1)
label2 = tkinter.Label(top, text="region", font=font1, bg='#000', fg='#FFF', padx='20', pady='20')
label2.bind('<Leave>', func2)
label2.bind('<Enter>', func1)
label1.pack()
label2.pack()
top.mainloop()