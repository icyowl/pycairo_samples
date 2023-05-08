import pickle
import matplotlib.pyplot as plt
from matplotlib import patches
from mycolorsys import lch_to_rgb

if __name__ == "__main__":

    with open("lch_list.pkl", "rb") as f: lch_list = pickle.load(f)

    fig, ax = plt.subplots(figsize=(4,4))

    ax.set_title("Hue circle - lch")
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.axis("off")

    for i, (hue, (lmin, lmax), (cmin, cmax)) in enumerate(lch_list):
        r, g, b = [x/255. for x in lch_to_rgb((lmax, cmax, hue))]
        if 0. <= r <=1. and 0. <= g <= 1. and 0. <= b <= 1.:
            w = patches.Wedge((0,0), 
                            0.9, 
                            width=0.3,
                            theta1=i, 
                            theta2=i+1, 
                            color=(r, g, b))
            ax.add_patch(w)
    
    plt.show()