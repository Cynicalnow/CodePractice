from tkinter import *
import tkinter.messagebox

root=Tk()

tkinter.messagebox.showinfo("Window Title","Do you like me?")

answer=tkinter.messagebox.askquestion("Qustion 1","Are you human?")
if answer=="yes":
    tkinter.messagebox.showinfo("Congrats","Nice to meet you!")
    
if answer=="no":
    tkinter.messagebox.showinfo("Alien","Go to hell")

root.mainloop()
