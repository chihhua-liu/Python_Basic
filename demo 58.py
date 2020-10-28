# demo58   Message

import tkinter
import tkinter.font
from tkinter.font import Font


def func1(ev):
    message.config(text='move to [%d,%d]' % (ev.x, ev.y))


top = tkinter.Tk()
font1 = Font(family='Carlito', size=32)
font2 = Font(family='Microsoft YaHei', size=28)
message = tkinter.Message(top, text="display here", font=font1, bg='#C0FFEE')
message.pack()
message.bind('<Motion>', func1)   # 傳even
top.minsize(600, 400)    # limit windows size : Fixed size
top.maxsize(600, 400)
top.mainloop()