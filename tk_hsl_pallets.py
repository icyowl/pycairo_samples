import tkinter as tk
from mycolorsys import *

root = tk.Tk()

hue = 200
root.title(f"HSL Table hue={hue}")

frame = tk.Frame(root)
tk.Label(frame, text="Sat =", width=5).pack(side=tk.LEFT)
for i in range(11):
    canvas = tk.Canvas(frame, width=50, height=20)
    canvas.create_text(28, 14, text=f"{i*10}%")
    canvas.pack(padx=3, pady=3, side=tk.LEFT)

frame.pack()

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