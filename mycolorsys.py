import colorsys
import colour
import numpy as np
from numpy.typing import ArrayLike

def _rgb_to_hsl(R:int, G:int, B:int) -> tuple:
    rgb = (R, G, B)
    h, l, _ = colorsys.rgb_to_hls(*rgb)

    H = h * 360
    maxc, minc = max(rgb), min(rgb)
    S = 100*(maxc-minc)/(255-abs(maxc+minc-255))
    L = 100*l/255

    return H, S, L

def _hsl_to_rgb(H:float, S:float, L:float) -> tuple:
    h = H / 360
    maxc = 2.55 * (L + L * (S/100)) if L < 50 else 2.55 * (L + (100-L) * (S/100))
    minc = 2.55 * (L - L * (S/100)) if L < 50 else 2.55 * (L - (100-L) * (S/100))
    l = L * 2.55
    s = (maxc-minc)/(1 - abs(maxc + minc - 1))

    R, G, B = [int(x) for x in colorsys.hls_to_rgb(h, l, s)]

    return R, G, B

def rgb_to_hsl(rgb: ArrayLike):
    r, g, b = [x/255. for x in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h, s, l = h*360, s*100, l*100

    return np.array([h, s, l])

def hsl_to_rgb(h, s, l):
    h, l, s = h/360, l/100, s/100
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    r, g, b = [int(round(x*255)) for x in (r, g, b)]

    return r, g, b

def rgb_to_hsv(r, g, b):
    r, g, b = [x/255. for x in (r, g, b)]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h, s, v = h*360, s*100, v*100

    return h, s, v

def hsv_to_rgb(h, s, v):
    h, s, v = h/360, s/100, v/100
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    r, g, b = [int(round(x*255)) for x in (r, g, b)]

    return r, g, b


def hex_to_rgb(code):
    c = code.strip("#")
    R, G, B = [int(x, 16) for x in (c[:2], c[2:4], c[4:])]
    return R, G, B

def rgb_to_hex(R, G, B):
    return "#%02x%02x%02x" % (R, G, B)

def hex_to_hsl(code):
    r, g, b = hex_to_rgb(code)
    
    return rgb_to_hsl(r, g, b)

def hsl_to_hex(H, S, L):
    rgb = hsl_to_rgb(H, S, L)

    return rgb_to_hex(*rgb)

def rgb_to_lch(rgb):
    rgb = [x/255. for x in rgb]
    xyz = colour.sRGB_to_XYZ(rgb)
    lab = colour.XYZ_to_Lab(xyz)
    lch = colour.Lab_to_LCHab(lab)

    l, c, h = [round(x, 3) for x in lch.tolist()]

    return l, c, h

def lch_to_rgb(lch):
    lab = colour.LCHab_to_Lab(lch)
    xyz = colour.Lab_to_XYZ(lab)
    srgb = colour.XYZ_to_sRGB(xyz)
    
    return np.around(srgb*255).astype(int)

def lch_to_hex(L, C, H):
    R, G, B = lch_to_rgb(L, C, H)

    return rgb_to_hex(R, G, B)


