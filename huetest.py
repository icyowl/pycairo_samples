import colorsys
import matplotlib.pyplot as plt
from matplotlib import patches

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
    # hex_l = [format(x, 'x') for x in rgb]

    return R, G, B

def hex_to_rgb(code):
    c = code.strip("#")
    R, G, B = [int(x, 16) for x in (c[:2], c[2:4], c[4:])]
    return R, G, B

def rgb_to_hex(R, G, B):
    return "#%02x%02x%02x" % (R, G, B)


if __name__ == "__main__":

    print(rgb_to_hex(128, 128, 128))
    print(hex_to_rgb("#808080"))

    fig, ax = plt.subplots(figsize=(4,4))

    ax.set_title("Hue circle - hsl(dig, 100, 50)")
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.axis("off")

    for i in range(360):
        rgb = [x/255. for x in hsl_to_rgb(i, 100, 50)]
        w = patches.Wedge((0,0), 
                        0.9, 
                        width=0.3,
                        theta1=i, 
                        theta2=i+1, 
                        color=rgb)
        ax.add_patch(w)
    
    #plt.show()
    plt.savefig("huecircle.png")