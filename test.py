import itertools
import pickle 
import numpy as np
import matplotlib.pyplot as plt
import colour
import time
import tkinter as tk

def lch_to_rgb(lch):
    lab = colour.LCHab_to_Lab(lch)
    xyz = colour.Lab_to_XYZ(lab)
    srgb = colour.XYZ_to_sRGB(xyz)
    
    return srgb # np.around(srgb*255).astype(int)

def rgb_to_lch(srgb):
    xyz = colour.sRGB_to_XYZ(srgb)
    lab = colour.XYZ_to_Lab(xyz)
    lch = colour.Lab_to_LCHab(lab)

    return lch

def make_lchs():
    x = [i/255. for i in range(256)]
    rgbs = list(itertools.product(x, repeat=3))
    
    print("start")
    start = time.time()

    ls = [rgb_to_lch(rgb) for rgb in rgbs]
    arr = np.array(ls)

    with open('lch_arr.pkl', 'wb') as f:
        pickle.dump(arr, f)    

    t = time.time() - start
    print("end", round(t/60), "min", t%60, "sec")


if __name__ == "__main__":
    
    ...
    # make_lchs()

    # p = "lch_df.pkl"
    # with open(p, "rb") as f:
    #     df = pickle.load(f)

    # L = arr[:, 0]
    # chroma = arr[:, 1]
    # hue = arr[:, 2]

    # print(max(L), min(L))
    # print(max(chroma), min(chroma))
    # print(max(hue), min(hue))

    # plt.plot(df["hue"], df["c*"])
    # plt.show()

    # h = np.unique(hue)
    # idx, = np.where((29.9999 < h) & (h < 30.0001))
    # print([h[i] for i in idx])

    # for i, lch, in enumerate(arr):
    #     # if i > 10: break 
    #     rgb = lch_to_rgb(lch)
    #     print(rgb)


# hlc_list = []
# for dig in range(360):
#     # if i: break
#     h = dig + 0.0
#     idx, = np.where(arr[:,2] == h)
#     c = [arr[i][1] for i in idx]
#     minc, maxc = min(c), max(c)
#     # _minc = [arr[i][1] for i in idx if arr[i][0] == minl]
#     # _maxc = [arr[i][1] for i in idx if arr[i][0] == maxl]
#     print(h, minc, maxc)
#     val = h, (minc, maxc)
#     # print(val)
#     hlc_list.append(val)

# with open('lch_list.pkl', 'wb') as f:
#     pickle.dump(hlc_list, f)

