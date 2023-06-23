import matplotlib.pyplot as plt
import numpy as np
import string

def axis_equal_3d(ax):
    a = np.array([getattr(ax, f"get_{dim}lim")() for dim in "xyz"])
    rng = max(abs(a[:,1] - a[:,0])) * 0.5
    mid_x, mid_y, mid_z = np.mean(a, axis=1)
    ax.set_xlim(mid_x - rng, mid_x + rng)
    ax.set_ylim(mid_y - rng, mid_y + rng)
    ax.set_zlim(mid_z - rng, mid_z + rng)

def plot(s, length, angle, alpha=1, colors={}):
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')

    color = "k"
    theta = 90
    w = 5
    x, y, z = 0, 0, 0
    stack = []
    for i, c in enumerate(s):
        # if c in string.ascii_letters:
        if c in string.ascii_uppercase:
            rad = math.radians(theta)
            dx = math.cos(rad) * length
            dy = math.sin(rad) * length
            ax.plot((x, (x+dx)), (y, (y+dy)), linewidth=w, c=color)
            x += dx 
            y += dy
        elif c == "-":
            theta += angle + (random.random() - 0.5) * 10
            w = w / 1.5
        elif c == "+":
            theta -= angle + (random.random() - 0.5) * 10
            w = w / 1.5
        elif c == "/":
            length /= alpha
        elif c == "*":
            length *= alpha
        elif c == "[":
            stack.append((theta, w, x, y))
        elif c == "]":
            theta, w, x, y = stack.pop()
        elif c in colors:
            color = colors[c]



ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# ax.plot(3,4,1, "o", color="magenta")
# ax.plot(3,4,5, "o", color="cyan")

X = np.random.rand(100)*10+5
Y = np.random.rand(100)*5+2.5
Z = np.random.rand(100)*50+25

ax.scatter(X,Y,Z)

axis_equal_3d(ax)

plt.show()