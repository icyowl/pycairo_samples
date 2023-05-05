import tkinter as tk
from mycolorsys import *

root = tk.Tk()

hc = "#ADC3FF"
hc = "#AF0000"
r, g, b = hex_to_rgb(hc)
print(r, g, b)
l, c, h = rgb_to_lch((r, g, b))

hue = h
root.title(f"Lch Table hue={round(hue, 1)}")

frame = tk.Frame(root)
tk.Label(frame, text="L* =", width=5).pack(side=tk.LEFT)
for i in range(11):
    canvas = tk.Canvas(frame, width=50, height=20)
    canvas.create_text(28, 14, text=f"{i*10}%")
    canvas.pack(padx=3, pady=3, side=tk.LEFT)

frame.pack()

for i in range(11):
    val = i*10
    frame = tk.Frame(root)
    text = "c* =" + str(round(val)).rjust(3, " ") 
    label = tk.Label(frame, text=text)
    label.pack(side=tk.LEFT)

    n = 1
    for j in range(11*n):
        L = j*(10/n)
        r, g, b = lch_to_rgb((L, c, h))
        if 0<=r<=255 and 0<=g<=255 and 0<=b<=255:
            color = rgb_to_hex(r, g, b)
        else:
            color = "#ffffff"
            print(r, g, b)
        canvas = tk.Canvas(frame, width=50, height=50, bg=color)
        canvas.pack(padx=3, pady=3, side=tk.LEFT)
    
    frame.pack()

root.mainloop()