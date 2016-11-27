from tkinter import *

root=Tk()

def printName():
    print("Hello there")

button1=Button(root,text="Click Me",command=printName)

button1.pack()

root.mainloop()
