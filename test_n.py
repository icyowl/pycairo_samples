import colour
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
import pandas as pd
import pickle
import tkinter as tk

def lch_to_rgb(lch):
    lab = colour.LCHab_to_Lab(lch)
    xyz = colour.Lab_to_XYZ(lab)
    srgb = colour.XYZ_to_sRGB(xyz)
    
    return srgb # np.around(srgb*255).astype(int)

def rgb_to_hex(R, G, B):
    return "#%02x%02x%02x" % (R, G, B)

if __name__ == "__main__":

    p = "lch_df.pkl"
    with open(p, "rb") as f: df = pickle.load(f)

    f = np.vectorize(lambda x: 0. <= x <= 1.)

    root = tk.Tk()

    hue = 350.
    # L 0 - 100, c 0 - 134
    root.title(f"Lch hue={round(hue, 1)}")

    canvas = tk.Canvas(root, width=800, height=100)

    for i in range(14):
        L = 80.0
        lch = [L, i*10.0, hue]
        rgb = lch_to_rgb(lch)
        rgb = np.round(rgb, 3)
        if f(rgb).sum() == 3:
            pos = 50+i*50, 50, 80+i*50, 80
            r, g, b = [int(x*255) for x in rgb]
            color = rgb_to_hex(r, g, b)
            canvas.create_oval(*pos, fill=color, outline=color)
    
    canvas.pack()

    # frame = tk.Frame(root)
    # tk.Label(frame, text="L* =", width=5).pack(side=tk.LEFT)
    # for i in range(11):
    #     canvas = tk.Canvas(frame, width=50, height=20)
    #     canvas.create_text(28, 14, text=f"{i*10}%")
    #     canvas.pack(padx=3, pady=3, side=tk.LEFT)

    # frame.pack()

    # for i in range(11):
    #     val = i*10
    #     frame = tk.Frame(root)
    #     text = "c* =" + str(round(val)).rjust(3, " ") 
    #     label = tk.Label(frame, text=text)
    #     label.pack(side=tk.LEFT)

    #     n = 1
    #     for j in range(11*n):
    #         L = j*(10/n)
    #         r, g, b = lch_to_rgb((L, c, h))
    #         if 0<=r<=255 and 0<=g<=255 and 0<=b<=255:
    #             color = rgb_to_hex(r, g, b)
    #         else:
    #             color = "#ffffff"
    #             print(r, g, b)
    #         canvas = tk.Canvas(frame, width=50, height=50, bg=color)
    #         canvas.pack(padx=3, pady=3, side=tk.LEFT)
        
    #     frame.pack()

    root.mainloop()