from tkinter import *
import requests
from bs4 import BeautifulSoup

'''로또 번호를 가져오는 함수'''
def lotto_p(n):
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    txt = soup.find("div", attrs = {"class", "win_result"}).get_text()
    num_list = txt.split("\n")[7:13]
    bonus = txt.split('\n')[-4]

    print("당첨번호")
    print(num_list)
    print("보너스번호")
    print(bonus)

'''입력창의 값을 받아오는 함수'''
def ent_p():
    lotto_p(ent.get())


win = Tk()
win.geometry("600x200")
win.option_add("*Font", "궁서 20")

ent = Entry(win)
ent.pack()
    

btn = Button(win)
btn.config(text = "로또 당첨 번호 확인")
btn.config(command = ent_p)
btn.pack()


win.mainloop()