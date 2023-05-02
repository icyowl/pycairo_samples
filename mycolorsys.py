import colorsys
import colour
import numpy as np

def rgb_to_hsl(R:int, G:int, B:int) -> tuple:
    rgb = (R, G, B)
    h, l, _ = colorsys.rgb_to_hls(*rgb)

    H = h * 360
    maxc, minc = max(rgb), min(rgb)
    S = 100*(maxc-minc)/(255-abs(maxc+minc-255))
    L = 100*l/255

    return H, S, L

def hsl_to_rgb(H:float, S:float, L:float) -> tuple:
    h = H / 360
    maxc = 2.55 * (L + L * (S/100)) if L < 50 else 2.55 * (L + (100-L) * (S/100))
    minc = 2.55 * (L - L * (S/100)) if L < 50 else 2.55 * (L - (100-L) * (S/100))
    l = L * 2.55
    s = (maxc-minc)/(1 - abs(maxc + minc - 1))

    R, G, B = [int(x) for x in colorsys.hls_to_rgb(h, l, s)]

    return R, G, B

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

def hex_to_lch(code):
    rgb = hex_to_rgb(code)
    xyz = colour.sRGB_to_XYZ(np.array(rgb)/255.)
    lab = colour.XYZ_to_Lab(xyz)
    lch = colour.Lab_to_LCHab(lab)

    return lch

def lch_to_hex(lch):
    lab = colour.LCHab_to_Lab(lch)
    xyz = colour.Lab_to_XYZ(lab)
    srgb = colour.XYZ_to_sRGB(xyz)
    r, g, b = np.around(srgb*255).astype(int)
    code = rgb_to_hex(r, g, b)

    return code

