import tkinter as tk
from tkinter import scrolledtext
from basic_chatGPT import chating

def show_text(event=None):
    text = entry.get()
    answer = chating(text)
    label.config(text=answer)

# tkinter 객체 생성
root = tk.Tk()
root.geometry("500x300") # 창 크기를 3배로 늘립니다.

# 입력 창 생성
entry_text = tk.StringVar()
entry_font = ("Helvetica", 14) # 글씨 크기를 조정합니다.
entry_width = 35 # 입력 창의 너비를 조정합니다.
entry = tk.Entry(root, textvariable=entry_text, font=entry_font, width=entry_width)
entry.pack()
entry.bind("<Return>", show_text) # <Return> 이벤트 처리를 추가합니다.

# 결과 창 생성
label_font = ("Helvetica", 14) # 폰트 크기를 2배로 키웁니다.
label_pady = 20 # 출력 문자와 위아래 간격을 조정합니다.
label_wraplength = 450 # 너비가 250 이하일 때 자동으로 개행합니다.
label_anchor = "nw" # 출력 문자를 좌측 상단에 정렬합니다.
label = tk.Label(root, text="", font=label_font, pady=label_pady, wraplength=label_wraplength, anchor=label_anchor)
label.pack()

# 버튼 생성
button = tk.Button(root, text="입력", command=show_text)
button.pack()

# tkinter mainloop 실행
root.mainloop()
