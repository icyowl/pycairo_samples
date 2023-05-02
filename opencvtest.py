import colour
import cv2 
import numpy as np
from mycolorsys import hex_to_rgb, rgb_to_hex

# print(cv2.__version__)
# img = cv2.imread("michiru.jpg")
# cv2.imshow("image", img)
# cv2.waitKey(0)

def foo(color):
    GAMMA = 2.4
    # r, g, b = colors[key][1:3], colors[key][3:5], colors[key][5:]
    # srgb = np.array([[[int(r, 16), int(g, 16), int(b, 16)]]]).astype(np.uint8)
    r, g, b = hex_to_rgb(color)
    srgb = np.array([[[r, g, b]]]).astype(np.uint8)
    # sRGB値(0~255)からリニアRGB値(0.0~1.0)に変換
    r, g, b = srgb[0,0,0] / 255.0, srgb[0,0,1] / 255.0, srgb[0,0,2] / 255.0
    r = r / 12.92 if r<=0.040450 else ((r + 0.055) / 1.055) ** GAMMA
    g = g / 12.92 if g<=0.040450 else ((g + 0.055) / 1.055) ** GAMMA
    b = b / 12.92 if b<=0.040450 else ((b + 0.055) / 1.055) ** GAMMA
    lrgb = np.array([[[r, g, b]]]).astype(np.float32)

    # 色空間の変換
    # リニアRGBからXYZ
    xyz = cv2.cvtColor((lrgb*255).astype(np.uint8), cv2.COLOR_RGB2XYZ)
    xyz_f = cv2.cvtColor(lrgb, cv2.COLOR_RGB2XYZ)
    # リニアRGBからL*a*b*
    lab = cv2.cvtColor((lrgb*255).astype(np.uint8), cv2.COLOR_RGB2Lab)
    lab_f = cv2.cvtColor(lrgb, cv2.COLOR_RGB2Lab)

    print(xyz_f, lab_f)

red = "#ff0000"

foo(red)


def hex_to_lch(color):
    rgb = hex_to_rgb(red)
    xyz = colour.sRGB_to_XYZ(np.array(rgb)/255.)
    lab = colour.XYZ_to_Lab(xyz)
    lch = colour.Lab_to_LCHab(lab)
    
    return lch 

def lch_to_hex(lch):
    lab = colour.LCHab_to_Lab(lch)
    xyz = colour.Lab_to_XYZ(lab)
    srgb = colour.XYZ_to_sRGB(xyz)
    r, g, b = np.around(srgb*255).astype(int)
    hexcode = rgb_to_hex(r, g, b)
    
    return hexcode

lch = hex_to_lch(red)
res = lch_to_hex(lch)
print(lch, res)