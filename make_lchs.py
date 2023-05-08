from mycolorsys import *
import tkinter as tk
import itertools
from numba import jit
import numpy as np
import pickle
import time

from sklearn.utils.extmath import cartesian

# @jit
# def rgb_to_hsl(rgb):
#     r, g, b = [x/255. for x in rgb]
#     # -> 
#     maxc = max(r, g, b)
#     minc = min(r, g, b)
#     sumc = (maxc+minc)
#     rangec = (maxc-minc)
#     l = sumc/2.0
#     if minc == maxc:
#         return 0.0, l, 0.0
#     if l <= 0.5:
#         s = rangec / sumc
#     else:
#         s = rangec / (2.0-sumc)
#     rc = (maxc-r) / rangec
#     gc = (maxc-g) / rangec
#     bc = (maxc-b) / rangec
#     if r == maxc:
#         h = bc-gc
#     elif g == maxc:
#         h = 2.0+rc-bc
#     else:
#         h = 4.0+gc-rc
#     h = (h/6.0) % 1.0
#     # <- 
#     h, s, l = h*360, s*100, l*100

#     return h, s, l

# hc = "#ff0000"
# hc = "#ADC3FF"
# r, g, b = hex_to_rgb(hc)

# hsv = rgb_to_hsv(r, g, b)
# hsl = rgb_to_hsl(r, g, b)
# print(hsv, hsl)

# l, c, h = rgb_to_lch(r, g, b)


# root = tk.Tk()
# tk.Canvas(root, width=200, height=200, bg=lch_to_hex(l, c, h+60)).pack(padx=10, pady=10)
# root.mainloop()

# sRGB = np.array(list(itertools.product(range(256), repeat=3)))

# print(list(itertools.product([1,2,3], repeat=3)))

start = time.time()

x = range(25)
arr = cartesian((x, x, x))


res = [rgb_to_lch(a) for a in arr]

with open('res.pickle', 'wb') as f:
    pickle.dump(res, f)

t = time.time() - start
print(round(t/60), "min", round(t%60, 5), "sec")
