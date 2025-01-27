from tkinter import *
root=Tk()
root.geometry("400x500")
root.title("Form Designing")

l1=Label(text="user name")
l1.grid(row=0,column=0)

e1=Entry()
e1.grid(row=0,column=1,pady=10)

l2=Label(text="password")
l2.grid(row=1)

e2=Entry(root,show="*")
e2.grid(row=1,column=1,pady=10)

def closewindow():
    root.destroy()

def submit():
    root.destroy()

b1=Button(text="Submit",command=submit)
b1.grid(row=2)

b2=Button(text="closeform",command=closewindow)
b2.grid(row=2,column=1)

mainloop()