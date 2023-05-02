from mycolorsys import *
import matplotlib.pyplot as plt
from matplotlib import patches

tones = "vivid", "bright", "strong", "deep", "light", "soft", "dull", "dark"

def is_tone(color):
    hue, sat, lit = hex_to_hsl(color)
    if sat >= 90. and 62.5 > lit and lit >= 37.5:
        return "vivid"
    
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
    
    return "no tone"
    
def main(color):
    
    
    hue, _, _ = hex_to_hsl(color)
    colors = (
        color,
        hsl_to_hex(hue, 90, 50),
        hsl_to_hex(hue, 80, 80),
        hsl_to_hex(hue, 80, 50),
        hsl_to_hex(hue, 80, 30)
    )
    n = len(colors)
    fig = plt.figure(figsize=(2*n, 2.3))
    for i, c in enumerate(colors):
        ax = fig.add_subplot(1, n, i+1)
        ax.set_title(c)
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.axis("off")
        p = patches.Circle(xy=(0, 0), radius=0.8, fc=c)
        ax.add_patch(p)
        s = [str(round(e, 2)) for e in hex_to_hsl(c)]
        hsl = "hsl: " + " ".join(s)
        t = is_tone(c)
        ax.text(-1, -1, t, size=10)

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":

    c = ["#345623", "#765832", "#46521f", "#ff00aa"]
    main("#ff6347")