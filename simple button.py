from tkinter import *
from tkinter import messagebox

top=Tk()
top.geometry("500x500")
def fun():
    msg=messagebox.showerror("title","u r chutiya")
   

B=Button(top,state='active',height=10,width=10,activebackground='red',bg='green',command=fun).invoke()
B.place(x=100,y=100)
top.mainloop()
