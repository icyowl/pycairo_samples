import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import string
import tkinter as tk

def lSystem(s, rule, n):
    f = lambda: np.random.choice(["P1", "P2", "P3"])
    for _ in range(n):
        s = ''.join([rule.get(f()) if c == "X" else rule.get(c) or c for c in s])
    return s

def axis_equal_3d(ax):
    a = np.array([getattr(ax, f"get_{dim}lim")() for dim in "xyz"])
    rng = max(abs(a[:,1] - a[:,0])) * 0.3
    mid_x, mid_y, mid_z = np.mean(a, axis=1)
    ax.set_xlim(mid_x - rng, mid_x + rng)
    ax.set_ylim(mid_y - rng, mid_y + rng)
    ax.set_zlim(mid_z - rng, mid_z + rng)

def rotate_x(vec, angle, width):
	rad = np.radians(angle)
	mat = [[1, 0, 0], [0, np.cos(rad), -np.sin(rad)], [0, np.sin(rad), np.cos(rad)]]
	return np.dot(mat, vec), width / 1.6

def rotate_y(vec, angle, width):
	rad = np.radians(angle)
	mat = [[np.cos(rad), 0, -np.sin(rad)], [0, 1, 0], [np.sin(rad), 0, np.cos(rad)]]
	return np.dot(mat, vec), width / 1.6

def plot3d(s, angle, alpha=1, colors={}):
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    ax.axis("off")
    color = "k"
    width = 4
    pos = np.zeros(3, dtype=np.float64)
    vec = np.array([0, 0, 1.])
    stack = []
    for i, c in enumerate(s):
        theta = angle + (np.random.rand() - 0.5) * 12
        if i == 1:
            vec = vec * 8
        if i == 2:
            vec = vec / 8
        if s[i-1] == "g":
            tip = 1. + np.random.rand()
            vec = vec * tip 
        if s[i-2] == "g":
            vec = vec / tip
        if c in string.ascii_uppercase:
            new_pos = pos + vec
            ax.plot([pos[0], new_pos[0]], [pos[1], new_pos[1]], [pos[2], new_pos[2]], linewidth=width, c=color)
            pos = new_pos
        elif c == "+":
            vec, width = rotate_x(vec, theta, width)
        elif c == "-":
            vec, width = rotate_x(vec, -theta, width)
        elif c == "&":
            vec, width = rotate_y(vec, theta, width)
        elif c == "^":
            vec, width = rotate_y(vec, -theta, width)
        elif c == "/":
            vec = vec * alpha
        elif c == "*":
            vec = vec / alpha
        elif c == "[":
            stack.append((pos, vec, width))
        elif c == "]":
            pos, vec, width = stack.pop()
        elif c in colors:
            color = colors[c]

    return fig, ax

if __name__ == "__main__":
    

    axiom = "X"
    angle = 20
    n = 5
    rule = {
        "P1": "gF/[+X][-X][&X]^X",
        "P2": "gF/[+X][&X]^X*",
        "P3": "gF/[&X][^X]+X",
        "g": "k"
    }
    s = lSystem(axiom, rule, n)
    # print(s)
    fig, ax = plot3d(s, angle, alpha=1.2, colors={"g": (0,0,0,0.3), "k": (0,0,0,0.6)})
    axis_equal_3d(ax)

    plt.savefig("tree.svg")

    root = tk.Tk()
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().pack()
    plt.close()
    root.mainloop()
    

    