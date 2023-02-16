from tkinter import *
from datetime import datetime

win = Tk()
win.geometry("600x100")
win.title("What time?")
win.option_add("*Font", "궁서 20")

def what_time():
    dnow = datetime.now()
    btn.config(text=dnow)

btn = Button(win)
btn.config(text="현재 시각")
btn.config(width=30)
btn.config(command=what_time)

btn.pack()

win.mainloop()