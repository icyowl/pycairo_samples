import tkinter as tk
from mycolorsys import *

root = tk.Tk()

hue = 200
root.title(f"HSV Table hue={hue}")

frame = tk.Frame(root)
tk.Label(frame, text="Sat =", width=5).pack(side=tk.LEFT)
for i in range(11):
    canvas = tk.Canvas(frame, width=50, height=20)
    canvas.create_text(28, 14, text=f"{i*10}%")
    canvas.pack(padx=3, pady=3, side=tk.LEFT)

frame.pack()

for i in range(11):
    val = i*10
    frame = tk.Frame(root)
    text = "V=" + str(val).rjust(3, " ") + "%"
    label = tk.Label(frame, text=text)
    label.pack(side=tk.LEFT)

    for j in range(11):
        sat = j*10
        r, g, b = hsv_to_rgb(hue, sat, val)
        # color = lch_to_hex(lit, sat, hue)
        canvas = tk.Canvas(frame, width=50, height=50, bg=rgb_to_hex(r, g, b))
        canvas.pack(padx=3, pady=3, side=tk.LEFT)
    
    frame.pack()

root.mainloop()