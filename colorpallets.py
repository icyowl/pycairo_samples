from mycolorsys import *
import matplotlib.pyplot as plt
from matplotlib import patches

def get_tonename(color):
    hue, sat, lit = hex_to_hsl(color)
    if sat >= 90. and 62.5 > lit and lit >= 37.5:
        return "vivid"
    if sat >= 90. and (62.5 <= lit or lit < 37.5):
        return "vivid?"

    if 90 > sat and sat >= 70. and 87.5 > lit and lit >= 62.5:
        return "bright"
    if 90 > sat and sat >= 70. and 62.5 > lit and lit >= 37.5:
        return "strong"
    if 90 > sat and sat >= 70. and 37.5 > lit and lit >= 12.5:
        return "deep"
    
    if 70 > sat and sat >= 40. and 98 > lit and lit >= 74.:
        return "light"
    if 70 > sat and sat >= 40. and 74 > lit and lit >= 50.:
        return "soft"
    if 70 > sat and sat >= 40. and 50 > lit and lit >= 26.:
        return "dull"
    if 70 > sat and sat >= 40. and 26 > lit and lit >= 2.:
        return "dark"
    
    if 40. > sat and 98 > lit and lit >= 74.:
        return "pale"
    if 40. > sat and 74 > lit and lit >= 50.:
        return "ltgrey"
    if 40. > sat and 50 > lit and lit >= 26.:
        return "greish"
    if 40. > sat and 26 > lit and lit >= 2.:
        return "dkgrey"

    return "none"

def main(colors_d):

    n = len(colors_d)
    fig = plt.figure(figsize=(2*n, 2))
    for i, k in enumerate(colors_d):
        c = colors_d[k]
        ax = fig.add_subplot(1, n, i+1)
        ax.set_title(k)
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.text(-0.52, 0, c, size=12)
        ax.axis("off")
        p = patches.Circle(xy=(0, 0), radius=0.8, fc=c)
        ax.add_patch(p)
        s = [str(round(e, 1)) for e in hex_to_hsl(c)]
        dsc = "hsl:" + " ".join(s) + " (" + get_tonename(c) + ")"
        ax.text(-1, -1, dsc, size=9)

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":

    colors = ["#daeef3", "#169bbd", "#2a99b6", "#33bbdf", "#f1fbfe"]
    d = {
        "primary": "#daeef3", 
        "secondary": "#169bbd",
        "link": "#2a99b6",
        "hover": "#33bbdf",
        "background": "#f1fbfe"
    }
    d = {
        "primary": "#7fb1b2", 
        "secondary": "#1b2c3f",
        "link": "#213040",
        "hover": "#283d55",
        "background": "#fbfdfd"
    }
    d = {
        "primary": "#B0BEC5", 
        "secondary": "#373d59",
        "link": "#413f5c",
        "hover": "#504c77",
        "background": "#fbfcfd"
    }
    main(d)


