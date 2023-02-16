from tkinter import *
import time


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("830x610")
window.configure(bg = "#ededed")
canvas = Canvas(
    window,
    bg = "#ededed",
    height = 700,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    420, 467.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")

canvas.create_text(
    400, 50,
    text = "PRODUCT",
    fill = "#5b5b5b",
    font = ("Inder-Regular", int(50.0)))

window.resizable(True, True)

Buttons = ["Button 1","Button 2","Button 3","Button 4"]

j = 150
i = 0
while True: 

    window.update()
    b0 = Button(
        text = Buttons[i],
        font = ("Inder-Regular", int(20.0)),
        bg = "#D9D9D9",
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")
    b0.place(
        x = 70, y = j,
        width = 691,
        height = 50)
    # j=j+55
    i=i+1
    time.sleep(2)
