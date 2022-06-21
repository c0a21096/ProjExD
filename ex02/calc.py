"""
追加機能:四則演算キー、初期化キー、キーボードの色変え機能
"""

import tkinter as tk
import tkinter.messagebox as tkm

THEME_LIST = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']
BG = "white"

def cfg_window(event): #cfg画面
    cfg = tk.Toplevel()
    #cfg.geometry("200x200")
    exp = tk.Label(cfg, text="テーマを選択")
    exp.grid(row=0, column=0)
    for i, theme in enumerate(THEME_LIST):
        button = tk.Button(
            cfg, 
            text=theme, 
            height=1, 
            width=10,
            font=("Times New Roman", 20)
            )
        button.bind("<1>", cfg_btn_click)
        button.grid(row=i+1, column=0)

def cfg_btn_click(event): #cfgボタンイベント
    global BG
    btn = event.widget
    color = btn["text"]
    BG = color
    init_keys()

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        eq = entry.get()
        res = eval(eq)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    elif num == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, num)

def init_keys():
    r, c = 0, 0 #行r、列c
    for i, num in enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+", "-", "*", "/", "=", "C"]):
        button = tk.Button(
            root, 
            text=f"{num}", 
            height=2, 
            width=4,
            font=("Times New Roman", 30),
            bg = BG
            )
        button.bind("<1>", button_click)
        button.grid(row=r+1, column=c)
        c+=1
        if (i+1)%4==0:
            r+=1
            c=0
    cfgbutton = tk.Button(
            root, 
            text="Config", 
            height=1, 
            width=50,
            font=("Times New Roman", 10)
            )
    cfgbutton.bind("<1>", cfg_window)
    cfgbutton.grid(row=r+1, column=c, columnspan=4)

if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("300x500")
    root.title("計算機")

    entry = tk.Entry(
            root, 
            justify="right",   
            width=10, 
            font=("Times New Roman", 40)
            )
    entry.grid(columnspan=4, column=0, row=0)
    init_keys()

    root.mainloop()