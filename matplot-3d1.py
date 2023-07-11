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

# def lSystem(s, rule, iterations):
#     for _ in range(iterations):
#         s = ''.join([rule.get(c) or c for c in s])
#     return s

def axis_equal_3d(ax):
    a = np.array([getattr(ax, f"get_{dim}lim")() for dim in "xyz"])
    rng = max(abs(a[:,1] - a[:,0])) * 0.3
    mid_x, mid_y, mid_z = np.mean(a, axis=1)
    ax.set_xlim(mid_x - rng, mid_x + rng)
    ax.set_ylim(mid_y - rng, mid_y + rng)
    ax.set_zlim(mid_z - rng, mid_z + rng)

def rotate_x(vec, angle):
    rad = np.radians(angle)
    mat = [[1, 0, 0], [0, np.cos(rad), -np.sin(rad)], [0, np.sin(rad), np.cos(rad)]]
    return np.dot(mat, vec)

def rotate_y(vec, angle):
    rad = np.radians(angle)
    mat = [[np.cos(rad), 0, -np.sin(rad)], [0, 1, 0], [np.sin(rad), 0, np.cos(rad)]]
    return np.dot(mat, vec)

def plot3d(s, angle, alpha=1, colors={}):
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    ax.axis("off")
    color = "k"
    width = 4
    pos = np.zeros(3, dtype=np.float64)
    vec = np.array([0, 0, 1.])
    stack = []
    t = 1
    for i, c in enumerate(s):
        theta = angle + (np.random.rand() - 0.5) * 12
        if i == 1:
            vec = rotate_x(vec, (np.random.rand() - 0.5) * 2)
            vec = vec * 15
        if i == 2:
            vec = vec / 15
        if i < len(s)-1:
            if c in "+-&^" and s[i+1] == "k":
                theta = 27 + (np.random.rand() - 0.5) * 6
                t = 2 + (np.random.rand() - 0.5) * 2
                vec = vec * t
            elif c == "k":
                vec = vec / t
        if c in string.ascii_uppercase:
            new_pos = pos + vec
            ax.plot([pos[0], new_pos[0]], [pos[1], new_pos[1]], [pos[2], new_pos[2]], linewidth=width, c=color)
            pos = new_pos
        elif c == "+":
            vec = rotate_x(vec, theta)
        elif c == "-":
            vec = rotate_x(vec, -theta)
        elif c == "&":
            vec = rotate_y(vec, theta)
        elif c == "^":
            vec = rotate_y(vec, -theta)
        elif c == "/":
            vec = vec * alpha
        elif c == "*":
            vec = vec / alpha
        elif c == "[":
            stack.append((pos, vec, width))
        elif c == "]":
            pos, vec, width = stack.pop()
        elif c in colors:
            r, g, b = 69/255, 70/255, 72/255
            if c == "g":
                a = np.random.randint(0, 9) * 0.1
                color = r, g, b, a 
            else:
                a = np.random.randint(7, 9) * 0.1
                color = r, g, b, a 
                # color = colors[c]
        if c in "+-&^":
            width = width / 1.6

    ax.view_init(elev=20, azim=10)

    return fig, ax

if __name__ == "__main__":
    

    axiom = "X"
    angle = 27.5
    n = 5
    rule = {
        "P1": "gF/[+X][-X][^X]&X*",
        "P2": "gF/[+X][-X][&X]*",
        "P3": "gF/[+X][-X][^X]*",
        "g": "k"
    }
    s = lSystem(axiom, rule, n)
    r, g, b = 69/255, 70/255, 72/255
    fig, ax = plot3d(s, angle, alpha=1.4, colors={"g": (r,g,b,0.6), "k": (r,g,b,0.9)})

    axis_equal_3d(ax)

    plt.savefig("tree_.svg", transparent=True)

    root = tk.Tk()
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().pack()
    plt.close()
    root.mainloop()
