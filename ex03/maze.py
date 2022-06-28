import tkinter as tk
import tkinter.messagebox as tkm

def key_down(event):
    global key
    key = event.keysym

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")
    canvas = tk.Canvas(
        root, 
        width = 1500, 
        height = 900, 
        bg = "black"
        )
    canvas.pack()

    koukaton = tk.PhotoImage(file="fig/0.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=koukaton, tag="koukaton")
    
    key = ""
    root.bind("<KeyPress>", key_down)

    root.mainloop()
    