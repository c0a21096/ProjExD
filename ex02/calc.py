import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num =btn["text"]
    tkm.showinfo("info", f"{num}が押されました")

def main():
    root = tk.Tk()
    #root.geometry("300x500")
    root.title("計算機")

    r, c = 0, 0
    for i in range(9, -1, -1):
        button = tk.Button(
            root, 
            text=f"{i}", 
            height=2, 
            width=4,
            font=("Times New Roman", 30)
            )
        button.bind("<1>", button_click)
        button.grid(row=r+1, column=c)
        c+=1
        if (i-1)%3==0:
            r+=1
            c=0

    entry = tk.Entry(
            justify="right",   
            width=10, 
            font=("Times New Roman", 40)
            )
    entry.grid(columnspan=3, column=0, row=0)

    root.mainloop()

if __name__ == "__main__":
    main()