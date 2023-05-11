import colorsys
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=540, height=64)
canvas.pack()
x = 0
for i in range(360):
    rgb = colorsys.hsv_to_rgb(i/360, 1.0, 0.5)
    rgb = tuple(int(x*255) for x in rgb)
    hrgb = "#%02x%02x%02x" % rgb
    canvas.create_line(x, 0, x, 64, width=1.5, fill=hrgb)
    x += 1.5


root.mainloop()