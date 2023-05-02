import cairo
import math
import os

def cmykToRgb(c, m, y, k):
    c = c/100
    m = m/100
    y = y/100
    k = k/100
    r = round(255 - ((min(1, c * (1 - k) + k)) * 255))
    g = round(255 - ((min(1, m * (1 - k) + k)) * 255))
    b = round(255 - ((min(1, y * (1 - k) + k)) * 255))

    return r, g, b

def rgbToCmyk(r, g, b):
    if (r, g, b) == (0, 0, 0):
        # black
        return 0, 0, 0, 100

    c = 1 - r/255
    m = 1 - g/255
    y = 1 - b/255

    min_cmy = min(c, m, y)
    c = 100 * (c - min_cmy) / (1 - min_cmy)
    m = 100 * (m - min_cmy) / (1 - min_cmy)
    y = 100 * (y - min_cmy) / (1 - min_cmy)
    k = 100 * min_cmy 

    return c, m, y, k

WIDTH, HEIGHT = 720, 256

def michiru_colors(filename):
    
    if os.name == "posix":
        fontface = "YuGothic"
    if os.name == "nt":
        fontface = "Yu Gothic"

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