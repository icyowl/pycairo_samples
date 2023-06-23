import matplotlib.pyplot as plt
import numpy as np
import random
import string

def lSystem(s, rule, iterations):
    for _ in range(iterations):
        s = ''.join([rule.get(c) or c for c in s])

    return s

def axis_equal_3d(ax):
    a = np.array([getattr(ax, f"get_{dim}lim")() for dim in "xyz"])
    mid_x, mid_y, mid_z = np.mean(a, axis=1)
    rng = max(abs(a[:,1] - a[:,0])) * 0.3
    ax.set_xlim(mid_x - rng, mid_x + rng)
    ax.set_ylim(mid_y - rng, mid_y + rng)
    ax.set_zlim(mid_z - rng, mid_z + rng)

def rotate_x(vec, angle, w):
    rad = np.radians(angle)
    mtr = [
        [1, 0, 0],
        [0, np.cos(rad), -np.sin(rad)],
        [0, np.sin(rad), np.cos(rad)]
        ]
    return np.dot(mtr, vec), w / 1.5

def rotate_y(vec, angle, w):
    rad = np.radians(angle)
    mtr = [
        [np.cos(rad), 0, -np.sin(rad)],
        [0, 1, 0],
        [np.sin(rad), 0, np.cos(rad)]
        ]
    return np.dot(mtr, vec), w / 1.5

def plot3d(s, length, angle, alpha=1, colors={}):
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    ax.axis("off")
    color = "k"
    w = 5
    pos = np.zeros(3, dtype=np.float64)
    direction = np.array([0, 0, 1.])
    stack = []
    for i, c in enumerate(s):
        if i == 1:
            direction = direction * 3
        if i == 2:
            direction = direction / 3
        theta = angle + (random.random()-0.5) * 12
        if c in string.ascii_uppercase:
            new_pos = pos + direction
            ax.plot([pos[0], new_pos[0]], [pos[1], new_pos[1]], [pos[2], new_pos[2]], linewidth=w, c=color)
            pos = new_pos
        elif c == "+":
            direction, w = rotate_x(direction, theta, w)
        elif c == "-":
            direction, w = rotate_x(direction, -theta, w)
        elif c == "&":
            direction, w = rotate_y(direction, theta, w)
        elif c == "^":
            direction, w = rotate_y(direction, -theta, w)
        elif c == '*':
            direction = direction * alpha
        elif c == '/':
            direction = direction / alpha
        elif c == "[":
            stack.append((pos, w, direction))
        elif c == "]":
            pos, w, direction = stack.pop()
        elif c in colors:
            color = colors[c]
    
    return ax

# fig = plt.figure(figsize=(4,4))
# ax = fig.add_subplot(111, projection='3d')

# ax.set_xlabel("X")
# ax.set_ylabel("Y")
# ax.set_zlabel("Z")

# X = np.random.rand(100)*10+5
# Y = np.random.rand(100)*5+2.5
# Z = np.random.rand(100)*50+25

# ax.scatter(X,Y,Z)

axiom = "B"
length = 10
angle = 25.7
iterations = 5
rule = {
    # "X": "F[+X]F[-X]+X",
    # "F": "FF"
    "B": "gF/[+B][-B][&B]^B*",
    "g": "k"
}
s = lSystem(axiom, rule, iterations)
ax = plot3d(s, length, angle, alpha=1.2, colors={"g": (0,0,0,0.3), "k": (0,0,0,0.9)})

axis_equal_3d(ax)
plt.show()