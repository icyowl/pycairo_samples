from mycolorsys import *
import tkinter as tk



hc = "#ff0000"
hc = "#ADC3FF"
r, g, b = hex_to_rgb(hc)

hsv = rgb_to_hsv(r, g, b)
hsl = rgb_to_hsl(r, g, b)
print(hsv, hsl)

l, c, h = rgb_to_lch(r, g, b)


root = tk.Tk()
tk.Canvas(root, width=200, height=200, bg=lch_to_hex(l, c, h+60)).pack(padx=10, pady=10)
root.mainloop()