import matplotlib.pyplot as plt
import numpy as np
import string

def lSystem(s, rule, iterations):
    for _ in range(iterations):
        s = ''.join([rule.get(c) or c for c in s])
    return s

def axis_equal_3d(ax):
    a = np.array([getattr(ax, f"get_{dim}lim")() for dim in "xyz"])
    rng = max(abs(a[:,1] - a[:,0])) * 0.3
    mid_x, mid_y, mid_z = np.mean(a, axis=1)
    ax.set_xlim(mid_x - rng, mid_x + rng)
    ax.set_ylim(mid_y - rng, mid_y + rng)
    ax.set_zlim(mid_z - rng, mid_z + rng)

def rotate_x(vec, angle):
	rad = np.radians(angle)
	mtr = [[1, 0, 0], [0, np.cos(rad), -np.sin(rad)], [0, np.sin(rad), np.cos(rad)]]
	return np.dot(mtr, vec)

def rotate_y(vec, angle):
	rad = np.radians(angle)
	mtr = [[np.cos(rad), 0, -np.sin(rad)], [0, 1, 0], [np.sin(rad), 0, np.cos(rad)]]
	return np.dot(mtr, vec)

def plot3d(s, angle, alpha=1, colors={}):
    fig = plt.figure(figsize=(4,4))
    ax = fig.add_subplot(111, projection='3d')
    ax.axis("off")
    color = "k"
    pos = np.zeros(3, dtype=np.float64)
    direction = np.array([0, 0, 1.])
    stack = []
    for i, c in enumerate(s):
        if i == 1:
            direction = direction * 5
        if i == 2:
            direction = direction / 5
        if c in string.ascii_uppercase:
            new_pos = pos + direction
            ax.plot([pos[0], new_pos[0]], [pos[1], new_pos[1]], [pos[2], new_pos[2]], c=color)
            pos = new_pos
        elif c == "+":
            direction = rotate_x(direction, angle)
        elif c == "-":
            direction = rotate_x(direction, -angle)
        elif c == "&":
            direction = rotate_y(direction, angle)
        elif c == "^":
            direction = rotate_y(direction, -angle)
        elif c == "/":
            direction = direction * alpha
        elif c == "*":
            direction = direction / alpha
        elif c == "[":
            stack.append((pos, direction))
        elif c == "]":
            pos, direction = stack.pop()
        elif c in colors:
            color = colors[c]

    return ax

if __name__ == "__main__":
    
    axiom = "X"
    length = 10
    angle = 20
    iterations = 5
    rule = {
        "X": "gF/[+X][-X][&X]^X*",
        "g": "k"
    }
    s = lSystem(axiom, rule, iterations)
    ax = plot3d(s, angle, alpha=1.2, colors={"g": (0,0,0,0.3), "k": (0,0,0,0.6)})
    axis_equal_3d(ax)

    plt.show()

    # ax.set_xlabel("X")
    # ax.set_ylabel("Y")
    # ax.set_zlabel("Z")
    # X = np.random.rand(100)*10+5
    # Y = np.random.rand(100)*5+2.5
    # Z = np.random.rand(100)*50+25

    # ax.scatter(X,Y,Z)