# demo55  tkinter

# import tkinter
# import tkinter.font
# from tkinter.font import Font
#
#
# def callback1():
#     print("hello world!")
#
#
# top = tkinter.Tk()
# for font in tkinter.font.families():    # show all font type
#     print(font)
#
# font1 = Font(family='Carlito', size=32)
# font2 = Font(family='Microsoft YaHei', size=28)
# label1 = tkinter.Label(top, text='Hello Tkinter inside Python3', font=font1, bg='#C0FFEE', fg='#FF0000')
# label2 = tkinter.Label(top, text='也可以使用中文', font=font2, bg='#FFC0EE', fg='#00FF00')
# button1 = tkinter.Button(top, text='click1', font=font1, command=callback1)
# button1.pack()   # display 有順序，越前面月上面
# label1.pack()
# label2.pack()
# top.mainloop()
#------------------------------------------------------
# demo55''
import tkinter
import tkinter.font
from tkinter.font import Font

counter = 0    # must used golbal

listCounter = [0]    # Not needed to use  golbal because list is immutable


def callback1():
    # print("hello world!")
    global counter    #must used golbal
    label1.config(text='button clicked %d times' % counter)
    counter += 1


def callback2():
    label2.config(text="button clicked %d times" % listCounter[0])
    listCounter[0] += 1


top = tkinter.Tk()
# for font in tkinter.font.families():
#     print(font)
font1 = Font(family='Carlito', size=32)
font2 = Font(family='Microsoft YaHei', size=28)
label1 = tkinter.Label(top, text='Hello Tkinter inside Python3', font=font1, bg='#C0FFEE', fg='#FF0000')
label2 = tkinter.Label(top, text='也可以使用中文', font=font2, bg='#FFC0EE', fg='#00FF00')
button1 = tkinter.Button(top, text='click1', font=font1, command=callback1)
button2 = tkinter.Button(top, text='click2', font=font1, command=callback2)
button1.pack()
button2.pack()
label1.pack()
label2.pack()
top.mainloop()