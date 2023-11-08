import tkinter as tk
from tkinter import *
from data import *

def add():
    line= id.get()+ '-' + name.get() + '-' + date.get()
    save(line)
    show()
def show():
    sv=read()
    listbox.delete(0,END)
    for i in sv:
        listbox.insert(END,i)

def sort():
    sv= read()
    for i in range(len(sv)):
        for j in range(len(sv)):
            x, y = sv[i], sv[j]
            if x[2] > y[2]:
                sv[i], sv[j] = y,x
    listbox.delete(0 ,END)
    for i in sv:
        listbox.insert(END,i)

root= Tk()
# var
id = StringVar
name= StringVar
date = StringVar

root.title('Quan ly hang hoa')
root.minsize(height=500, width=500)
Label(root, text='Ung dung quan ly hang hoa', fg='red',font=('cambria', 16),width=25).grid(row=0)
listbox = Listbox(root, width=90, height=20)
listbox.grid(row=1,columnspan=2)
show()
Label(root,text='Ma san pham: ').grid(row=2,column=0)
Entry(root,width=40, textvariable=id).grid(row=2, column=1)
Label(root,text='Ten san pham: ').grid(row=3,column=0)
Entry(root,width=40, textvariable=name).grid(row=3, column=1)
Label(root,text='Ngay nhap hang: ').grid(row=5,column=0)
Entry(root,width=40, textvariable=date).grid(row=5, column=1)
button = Frame(root)
Button(button, text='Them').pack(side=LEFT)
Button(button, text='Xoa').pack(side=LEFT)
Button(button, text='Sua').pack(side=LEFT)
Button(button, text='Thoat', command=root.quit).pack(side=LEFT)
button.grid(row=6, column=1)


root.mainloop()
