from tkinter import *
root=Tk()

topFrame=Frame(root)
topFrame.pack()
botFrame=Frame(root)
botFrame.pack(side=BOTTOM)
##
##theLabel=Label(root,text="This is  our Tkinter window")
##theLabel.pack()

Button1=Button(topFrame,text="Click me!",fg="Blue",bg="Red")
Button1.pack(side=LEFT)
Button2=Button(topFrame,text="Yes",fg="Green",bg="Yellow")
Button2.pack(side=LEFT)
Button3=Button(botFrame,text="Yes",fg="Green",bg="Yellow")
Button3.pack(side=LEFT)
Button4=Button(botFrame,text="Yes",fg="Green",bg="Yellow")
Button4.pack(side=LEFT)

root.mainloop()
