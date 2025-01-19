from tkinter import *
root=Tk()
radiovar=IntVar()
Label(root,text="Gender",).grid(row=0,column=0)
Radiobutton(root,text="male",variable=radiovar,value=1).grid(row=1,column=0)
Radiobutton(root,text="female",variable=radiovar,value=2).grid(row=2,column=0)
Radiobutton(root,text="others",variable=radiovar,value=3).grid(row=3,column=0)
root.mainloop()