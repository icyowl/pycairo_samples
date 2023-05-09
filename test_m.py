import colour
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches
import pandas as pd
import pickle

def foo():
    p = "lch_arr.pkl"
    with open(p, "rb") as f:
        arr = pickle.load(f)
    # return arr

    # _arr = arr[:, [2, 0, 1]] # lch -> hlc
    df = pd.DataFrame(arr, columns=("L*", "c*", "hue"))
    df_s = df.sort_values(["hue", "L*"])

    q = "lch_df.pkl"
    with open(q, "wb") as f:
        pickle.dump(df_s, f)

def lch_to_rgb(lch):
    lab = colour.LCHab_to_Lab(lch)
    xyz = colour.Lab_to_XYZ(lab)
    srgb = colour.XYZ_to_sRGB(xyz)
    
    return srgb # np.around(srgb*255).astype(int)


if __name__ == "__main__":
    
    # foo()

    p = "lch_df.pkl"
    with open(p, "rb") as f: df = pickle.load(f)

    idx = (77. < df["L*"]) & (df["L*"] < 83.) & (34. < df["c*"]) & (df["c*"] < 38.)
    _df = df[idx]
    print(len(_df))

    f = np.vectorize(lambda x: 0. <= x <= 1.)
    n = len(_df)
    colors = []
    prev_hue = None
    for i, (idx, row) in enumerate(_df.iterrows()):
        if not prev_hue == int(row["hue"]):
            rgb = lch_to_rgb(row.values)
            rgb = np.round(rgb, 3)
            if f(rgb).sum() != 3:
                print(rgb)
            colors.append(rgb)
            prev_hue = int(row["hue"])
            # print(prev_hue)

    print(len(colors))

    fig, ax = plt.subplots(figsize=(4,4))

    ax.set_title("Hue circle - lch")
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.axis("off")

    for i, (r, g, b) in enumerate(colors):
        w = patches.Wedge((0,0), 
                        0.9, 
                        width=0.3,
                        theta1=i, 
                        theta2=i+1, 
                        color=(r, g, b))
        ax.add_patch(w)
    
    plt.show()