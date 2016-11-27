from tkinter import *

root=Tk()

def leftClick(event):
    print("Left")
    
def rightClick(event):
    print("Left")

def scroll(event):
    print("Scroll")

def leftKey(event):
    print("Left key pressed")

def rightKey(event):
    print("Right key pressed")

root.geometry("500x500")

root.bind("<Button-1>",leftClick)
root.bind("<Button-2>",rightClick)
root.bind("<Button-3>",scroll)
root.bind("<Left>",leftKey)
root.bind("<Right>",rightKey)



root.mainloop()
