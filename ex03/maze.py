import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key == "Up" and maze[my-1][mx] == 0:
        my += -1
    elif key == "Down" and maze[my+1][mx] == 0:
        my += 1
    elif key == "Left" and maze[my][mx-1] == 0:
        mx += -1
    elif key == "Right" and maze[my][mx+1] == 0:
        mx += 1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("koukaton", cx, cy)
    root.after(100, main_proc)

#mainloop
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

    maze = maze_maker.make_maze(15, 9)#[y軸][x軸]のリスト
    maze_maker.show_maze(canvas, maze)#canvasにmazeを描画する

    koukaton = tk.PhotoImage(file="fig/0.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=koukaton, tag="koukaton")
    canvas.pack()

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()