import matplotlib.pyplot as plt
from matplotlib import patches

def main(colors):

    n = len(colors)
    fig = plt.figure(figsize=(2*n, 2.5))
    for i, c in enumerate(colors):
        ax = fig.add_subplot(1, n, i+1)
        ax.set_title(c)
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.axis("off")
        p = patches.Circle(xy=(0, 0), radius=0.8, fc=c)
        ax.add_patch(p)
        ax.text(-0.7, -1.2, c, size=12)

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":

    c = ["#345623", "#765832", "#46521f", "#ff00aa"]
    main(c)