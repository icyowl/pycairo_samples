import cairo
import math
import os

def cmykToRgb(c, m, y, k):
    c=float(c)/100.0
    m=float(m)/100.0
    y=float(y)/100.0
    k=float(k)/100.0
    r = round(255.0 - ((min(1.0, c * (1.0 - k) + k)) * 255.0))
    g = round(255.0 - ((min(1.0, m * (1.0 - k) + k)) * 255.0))
    b = round(255.0 - ((min(1.0, y * (1.0 - k) + k)) * 255.0))
    # r = round(255.0 * (1-c) * (1-k))
    # g = round(255.0 * (1-m) * (1-k))
    # b = round(255.0 * (1-y) * (1-k))
    return (r,g,b)

WIDTH, HEIGHT = 720, 256

def michiru_colors(filename):
    
    if os.name == "posix":
        fontface = "YuGothic"

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    c = cairo.Context(surface)
    c.set_source_rgb(1, 1, 1)
    c.paint()

    colors = [
        ("中蘇芳",(0, 100, 75, 30)), 
        ("牡丹", (27, 90, 0, 0)),
        ("茜", (0, 90, 56, 25)),
        ("海松色", (26, 0, 70, 70))
    # kanran = 0, 0, 55, 70 # 橄欖色
    ]

    division = 4

    for i, (name, cmyk) in enumerate(colors):

        x = (i+1) * WIDTH/(division+1)
        c.arc(x, HEIGHT*2.2/5, HEIGHT*1/5, 0, 2*math.pi)
        rgb = cmykToRgb(*cmyk)
        rgb = [x/255.0 for x in rgb]
        c.set_source_rgb(*rgb)
        c.fill()

        c.select_font_face(fontface, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        c.set_font_size(20)
        xx = 20 * len(name)/2
        c.move_to(x-xx, HEIGHT * 4/5)
        c.set_source_rgb(0, 0, 0)
        c.show_text(name)

    surface.write_to_png(filename)

if __name__ == "__main__":

    f = "michiru.png"
    michiru_colors(f)