from tkinter import *

root=Tk()

label1=Label(root,text="Name")

label1.grid(row=0,column=0)

entrySpace=Entry(root)

entrySpace.grid(row=0,column=1)

cbutton=Checkbutton(root,text="Remember name")
cbutton.grid(columnspan=2)

root.mainloop()
