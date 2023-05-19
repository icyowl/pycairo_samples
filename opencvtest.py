import colour
import cv2 
import numpy as np
from numpy.typing import ArrayLike
from mycolorsys import hex_to_rgb, rgb_to_hex

# print(cv2.__version__)
# img = cv2.imread("michiru.jpg")
# cv2.imshow("image", img)
# cv2.waitKey(0)

def sRGB_to_XYZ(rgb: ArrayLike) -> np.array:

    rgb = np.array([x/255. for x in rgb])
    GAMMA = 2.4 
    gcf = np.vectorize(lambda x: x / 12.92 if x<=0.040450 else ((x+0.055)/1.055) ** GAMMA, otypes=[float])
    linear_rgb = gcf(rgb)
    xyz_matrix = np.array([
            [0.4124, 0.2126, 0.0193],
            [0.3576, 0.7152, 0.1192],
            [0.1805, 0.0722, 0.9505]
        ])

    return np.dot(linear_rgb, xyz_matrix)

def XYZ_to_LAB(xyz: ArrayLike) -> np.array:
    x, y, z = xyz
    xn, yn, zn = 0.9505, 1.0, 1.089
    func = lambda x: x**(1/3) if x>0.008856 else (841/108)*x+(16/116)
    l = 116 * func(y/yn) - 16
    a = 500 * (func(x/xn) - func(y/yn))
    b = 200 * (func(y/yn) - func(z/zn))

    return np.array([l, a, b])

def LAB_to_LCH(lab: ArrayLike) -> np.array:
    l, a, b = lab
    c = np.sqrt(a**2 + b**2)
    func = lambda rad: rad * 180 / np.pi
    h = func(np.arctan2(b, a))

    return np.array([l, c, h])

def LCH_to_LAB(lch: ArrayLike) -> np.array:
    l, c, h = lch
    rad = h * np.pi / 180
    a = c*np.cos(rad)
    b = c*np.sin(rad)

    return np.array([l, a, b])

def LAB_to_XYZ(lab: ArrayLike):
    l, a, b = lab 
    xn, yn, zn = 0.9505, 1.0, 1.089
    f = lambda x: x**3 if x>0.206893 else (x-(16/116))*(108/841)
    x = f((a/500)+((l+16)/116)) * xn
    y = f((l+16)/116) * yn 
    z = f(((l+16)/116)-(b/200)) * zn

    return np.array([x, y, z])

def XYZ_to_sRGB(xyz: ArrayLike):
    rgb_matrix = np.array([
            [3.2406, -0.9689, 0.0557],
            [-1.5372, 1.8758, -0.2040],
            [-0.4986, 0.0415, 1.0570]
        ])
    linear_rgb = np.dot(xyz, rgb_matrix)

    GAMMA = 2.4 
    gcf = np.vectorize(lambda x: 1.055 * x**(1.0/GAMMA) - 0.055 if x>0.003130 else 12.92 * x, otypes=[float])
    rgb = gcf(linear_rgb)
    
    return np.around(rgb * 255).astype(int)

def foo(r, g, b):
    GAMMA = 2.4
    # r, g, b = colors[key][1:3], colors[key][3:5], colors[key][5:]
    # srgb = np.array([[[int(r, 16), int(g, 16), int(b, 16)]]]).astype(np.uint8)
    # r, g, b = hex_to_rgb(color)
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

    # print(xyz_f, lab_f)

    return xyz_f


def hex_to_lch(color):
    rgb = hex_to_rgb(color)
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

if __name__ == "__main__":

    darksaimon = "#E9967A"
    rgb = hex_to_rgb(darksaimon)
    print(rgb)
    xyz = sRGB_to_XYZ(rgb)
    lab = XYZ_to_LAB(xyz)
    lch = LAB_to_LCH(lab)
    print(lab, lch)
    res = LCH_to_LAB(lch)
    print(res)


    # lch = hex_to_lch(red)
    # res = lch_to_hex(lch)
    # print(lch, res)