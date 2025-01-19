from tkinter import *
root=Tk()
Label(root,text="hobbies").grid(row=0,sticky=W)

c1=IntVar()
Checkbutton(root,text="reading",variable=c1).grid(row=1,sticky=W)

c2=IntVar()
Checkbutton(root,text="writing",variable=c2).grid(row=2,sticky=W)

c3=IntVar()
Checkbutton(root,text="singing",variable=c3).grid(row=3,sticky=W)

c4=IntVar()
Checkbutton(root,text="dancing",variable=c4).grid(row=4,sticky=W)

def close():
    root.destroy()
    
Button(root,text="close",command=root.destroy).grid(row=6)

root.mainloop()
