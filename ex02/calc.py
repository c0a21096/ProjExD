import tkinter as tk


def main():
    root = tk.Tk()
    root.title("計算機")
    root.geometry("300x500")


    button = tk.Button(
            root, 
            text=0, 
            font=("Times New Roman", 30),
            height=2, 
            width=4,
            )
    button.grid(row=0, column=0)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()