# demo61    Entry like Editor

import tkinter
import tkinter.font
from tkinter.font import Font

def func1(ev):
    label.config(text=entry.get())
    print(ev)

top = tkinter.Tk()
font1 = Font(family='Carlito', size=32)
font2 = Font(family='Microsoft YaHei', size=28)
label = tkinter.Label(top, text="display result", font=font1)
entry = tkinter.Entry(top, font=font1)
button = tkinter.Button(top, font=font1, text='submit')
entry.bind('<Return>', func1)
button.bind('<Button-1>', func1)
label.pack()
entry.pack()
button.pack()
top.mainloop()