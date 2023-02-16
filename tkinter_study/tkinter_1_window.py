from tkinter import *
# import tkinter

win = Tk() # 창 생성

win.geometry("1000x500")
win.title("temp")
win.option_add("*Font","맑은고딕 25")

btn = Button(win, text='버튼', command=win.destroy)
btn.pack()

win.mainloop() # 창 실행


# from tkinter import *
# from tkinter import ttk
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()
