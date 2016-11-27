from tkinter import *

root=Tk()
label1=Label(None,text="Enter your expression here:")
label1.pack()
def evaluate(event):
    data=e.get()
    ans.configure(text="Answer:\t"+str(eval(data)))

e=Entry(root)

e.bind("<Return>",evaluate)
e.pack()
ans= Label(root)
ans.pack()

root.mainloop()
