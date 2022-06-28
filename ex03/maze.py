import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

def key_down(event):
    global key
    key = event.keysym

def key_up(event):
    global key
    key = ""

def enemy_move():#enemyの行動パターン定義
    global ecx, ecy, emx, emy
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    tmp = [ 
        maze[emy][emx-1], 
        maze[emy-1][emx], 
        maze[emy][emx+1], 
        maze[emy+1][emx]
        ]#左上右下
    for n, i in enumerate(tmp):
        if i == 0:
            emx += dx[n]
            emy += dy[n]
            break

def main_proc():
    global cx, cy, mx, my, is_goal, is_defeated, is_move
    if key == "Up" and maze[my-1][mx] == 0:
        my += -1
        is_move = True
    elif key == "Down" and maze[my+1][mx] == 0:
        my += 1
        is_move = True
    elif key == "Left" and maze[my][mx-1] == 0:
        mx += -1
        is_move = True
    elif key == "Right" and maze[my][mx+1] == 0:
        mx += 1
        is_move = True
    cx, cy = mx*100+50, my*100+50
    canvas.coords("koukaton", cx, cy)

    if is_move:
        enemy_move()
    ecx, ecy = emx*100+50, emy*100+50
    canvas.coords("enemy", ecx, ecy)

    is_move = False
    
    #接触時の処理
    if mx == gmx and my == gmy:
        is_goal = True
        canvas.create_text(750, 450, text="Clear", font=("Times New Roman", 200))
    if mx == emx and my == emy:
        is_defeated = True
        canvas.create_text(750, 450, text="failed...", font=("Times New Roman", 200))

    if not is_goal or not is_defeated:
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

    is_goal = False
    is_defeated = False
    is_move = False #自機が動いたかどうか

    maze = maze_maker.make_maze(15, 9)#[y軸][x軸]のリスト
    maze_maker.show_maze(canvas, maze)#canvasにmazeを描画する

    koukaton = tk.PhotoImage(file="fig/0.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=koukaton, tag="koukaton")
    canvas.pack()

    goal = tk.PhotoImage(file="fig/9.png")
    gmx, gmy = 13, 7
    gcx, gcy = gmx*100+50, gmy*100+50
    canvas.create_image(gcx, gcy, image=goal, tag="goal")
    canvas.pack()

    enemy = tk.PhotoImage(file="fig/5.png")
    emx, emy = 13, 1
    ecx, ecy = emx*100+50, emy*100+50
    canvas.create_image(ecx, ecy, image=enemy, tag="enemy")
    canvas.pack()

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()

    root.mainloop()