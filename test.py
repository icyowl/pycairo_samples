import colorsys
from mycolorsys import rgb_to_hsl
import tkinter as tk

def hex_to_rgb(HC):
    R, G, B = [int(x, 16) for x in (HC[1:3], HC[3:5], HC[5:])]
    return R, G, B

def rgb_to_hex(R, G, B):
    HC = "#%02x%02x%02x" % (R, G, B)
    return HC

def rgb_to_hsv(r, g, b):
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    return h*360, s*100, 100*v/255.

# print(colorsys.hsv_to_rgb(1,1,1))

# root = tk.Tk()
# root.title("color test")

hc = "#ff0000"
hc = "#ADC3FF"
r, g, b = hex_to_rgb(hc)
r, g, b = [x/255. for x in (r,g,b)]
h, s, v = colorsys.rgb_to_hls(r, g, b)
h, s, v = h*360, s*100, v*100
print(h,s, v)

hc = "#ADC3FF"
r, g, b = hex_to_rgb(hc)

hsv = rgb_to_hsv(r, g, b)
hsl = rgb_to_hsl(r, g, b)
print(hsv, hsl)

# tk.Canvas(root, width=300, height=300, bg="red").pack(padx=10, pady=10)
# root.mainloop()