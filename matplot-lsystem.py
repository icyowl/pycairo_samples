import matplotlib.pyplot as plt 


def pltview(something=None):
    ...


if __name__ == "__main__":

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlim([0, 512])
    ax.set_ylim([0, 512])
    ax.axis("off")

    ax.arrow(256, 256, 0, 100)
    ax.arrow(256, 356, 50, 50)
    plt.show()