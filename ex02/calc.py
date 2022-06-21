import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        eq = entry.get()
        res = eval(eq)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)
    else:
        entry.insert(tk.END, num)

if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry("300x500")
    root.title("計算機")

    r, c = 0, 0
    for i, num in enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+", "="]):
        button = tk.Button(
            root, 
            text=f"{num}", 
            height=2, 
            width=4,
            font=("Times New Roman", 30)
            )
        button.bind("<1>", button_click)
        button.grid(row=r+1, column=c)
        c+=1
        if (i+1)%3==0:
            r+=1
            c=0

    entry = tk.Entry(
            root, 
            justify="right",   
            width=10, 
            font=("Times New Roman", 40)
            )
    entry.grid(columnspan=3, column=0, row=0)

    root.mainloop()