import tkinter as tk
from mycolorsys import *

root = tk.Tk()

hue = 200
root.title(f"HSL Table hue={hue}")

frame = tk.Frame(root)

scale_var = tk.IntVar()



def scale_pack(frame, var, callback):
    tk.Scale(frame, 
            variable = var, 
            command = callback,
            orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
            length = 256,           # 全体の長さ
            width = 20,             # 全体の太さ
            sliderlength = 10,      # スライダー（つまみ）の幅
            from_ = 0,            # 最小値（開始の値）
            to = 360,               # 最大値（終了の値）
            resolution=1,         # 変化の分解能(初期値:1)
            tickinterval=100         # 目盛りの分解能(初期値0で表示なし)
            ).pack(padx=8)

def callback():
    hue = scale_var + 0.0
    for i in range(11):
        lit = i*10
        frame = tk.Frame(root)
        text = "L=" + str(lit).rjust(3, " ") + "%"
        label = tk.Label(frame, text=text)
        label.pack(side=tk.LEFT)

        for j in range(11):
            sat = j*10
            color = hsl_to_hex(hue, sat, lit)
            # color = lch_to_hex(lit, sat, hue)
            canvas = tk.Canvas(frame, width=50, height=50, bg=color)
            canvas.pack(padx=3, pady=3, side=tk.LEFT)
        
        frame.pack()

scale_pack(frame, scale_var, callback)

tk.Label(frame, text="Sat =", width=5).pack(side=tk.LEFT)
for i in range(11):
    canvas = tk.Canvas(frame, width=50, height=20)
    canvas.create_text(28, 14, text=f"{i*10}%")
    canvas.pack(padx=3, pady=3, side=tk.LEFT)

frame.pack()

hue = 0.0
for i in range(11):
    lit = i*10
    frame = tk.Frame(root)
    text = "L=" + str(lit).rjust(3, " ") + "%"
    label = tk.Label(frame, text=text)
    label.pack(side=tk.LEFT)

    for j in range(11):
        sat = j*10
        color = hsl_to_hex(hue, sat, lit)
        # color = lch_to_hex(lit, sat, hue)
        canvas = tk.Canvas(frame, width=50, height=50, bg=color)
        canvas.pack(padx=3, pady=3, side=tk.LEFT)
    
    frame.pack()

root.mainloop()