from tkinter import *
root=Tk()


Button1=Button(None,text="Click me!",fg="Blue",bg="Red")
Button1.pack()
Button2=Button(None,text="Yes",fg="Green")
Button2.pack(fill=X)
Button3=Button(None,text="Yes",fg="Green",bg="Yellow")
Button3.pack(side=RIGHT,fill=Y)
Button4=Button(None,text="Yes",fg="Green",bg="Yellow")
Button4.pack(side=LEFT)

root.mainloop()
