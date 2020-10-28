# demo60   tkinter :  Scale

import tkinter
import tkinter.font
from tkinter.font import Font



displayMessage = "Value=%d"
def func1(scale):
    label1.config(text=displayMessage%int(scale))

top = tkinter.Tk()
value = tkinter.IntVar()  #default
value.set(0)

font1 = Font(family='Carlito', size=32)
font2 = Font(family='Microsoft YaHei', size=28)

label1 = tkinter.Label(top, text=displayMessage % 0, font=font1)
scale1 = tkinter.Scale(top, label="Volume", font=font2, orient="h", from_=0, to=100,     # value from 0 to 100,orient="h" or"v"
                       showvalue=False, variable=value, command=func1)    # showvalue =Ture or False
label1.pack()
#scale1.pack()
scale1.pack(fill='both')  # check length
top.maxsize(600, 200)
top.minsize(600, 200)
top.mainloop()