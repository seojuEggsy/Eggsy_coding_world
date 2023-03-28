import tkinter as tk

def show_text(event=None):
    text = entry.get()
    label.config(text=text)

def start_drag(event):
    global x, y
    x = event.x
    y = event.y

def drag(event):
    x_new = event.x
    y_new = event.y
    delta_x = x_new - x
    delta_y = y_new - y
    label.place(x=label.winfo_x() + delta_x, y=label.winfo_y() + delta_y)
    x = x_new
    y = y_new

# tkinter 객체 생성
root = tk.Tk()
root.geometry("300x300") # 창 크기를 3배로 늘립니다.

# 입력 창 생성
entry_text = tk.StringVar()
entry_font = ("Helvetica", 14) # 글씨 크기를 조정합니다.
entry_width = 20 # 입력 창의 너비를 조정합니다.
entry = tk.Entry(root, textvariable=entry_text, font=entry_font, width=entry_width)
entry.pack()
entry.bind("<Return>", show_text) # <Return> 이벤트 처리를 추가합니다.

# 결과 창 생성
label_font = ("Helvetica", 20) # 폰트 크기를 2배로 키웁니다.
label_pady = 20 # 출력 문자와 위아래 간격을 조정합니다.
label_wraplength = 250 # 너비가 250 이하일 때 자동으로 개행합니다.
label_anchor = "nw" # 출력 문자를 좌측 상단에 정렬합니다.
label_text = tk.StringVar()
label = tk.Label(root, textvariable=label_text, font=label_font, pady=label_pady, wraplength=label_wraplength, anchor=label_anchor, bd=1, relief="solid")
label_text.set("결과 창")
label.pack()

# 마우스 드래그 이벤트 처리
label.bind("<Button-1>", start_drag)
label.bind("<B1-Motion>", drag)

# 버튼 생성
button = tk.Button(root, text="입력", command=show_text)
button.pack()

# tkinter mainloop 실행
root.mainloop()
