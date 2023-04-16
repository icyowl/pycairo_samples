import cairo
import math

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

WIDTH, HEIGHT = 256, 128

def michiru_colors(filename):

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    c = cairo.Context(surface)

    c.set_source_rgb(1, 1, 1)
    c.paint()

    nakasuo = 0, 100, 75, 30 # 中蘇芳
    botan = 27, 90, 0, 0 # 牡丹
    akane = 0, 90, 56, 25 # 茜
    kanran = 0, 0, 55, 70 # 橄欖色
    miruiro = 26, 0, 70, 70 # 海松色

    cmyk_colors = nakasuo, miruiro

    for i, cmyk in enumerate(cmyk_colors):
        c.arc((i+1) * WIDTH/(len(cmyk_colors)+1), HEIGHT/2, HEIGHT/5, 0, 2*math.pi)
        rgb = cmykToRgb(*cmyk)
        rgb = [x/255 for x in rgb]
        c.set_source_rgb(*rgb)
        c.fill()

    surface.write_to_png(filename)

if __name__ == "__main__":

    f = "michru.png"
    michiru_colors(f)