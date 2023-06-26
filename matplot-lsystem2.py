import matplotlib.pyplot as plt 
import numpy as np
import string

def lsystem(s, rule, n):
    for _ in range(n):
        s = ''.join([rule.get(c) or c for c in s])

    return s

def rotate(vec, angle):
    rad = np.radians(angle)
    mat = [[np.cos(rad), -np.sin(rad)], [np.sin(rad), np.cos(rad)]]
    return np.dot(mat, vec)

def plot(s, angle):
    fig = plt.figure(figsize=(4,4), facecolor="white")
    ax = fig.add_subplot()
    ax.set_aspect("equal")
    ax.axis("off")
    pos = np.zeros(2, dtype=np.float64)
    vec = np.array([1., 0])
    stack = []
    for c in s:
        if c in string.ascii_letters:
            new_pos = pos + vec
            ax.plot((pos[0], new_pos[0]), (pos[1], new_pos[1]), color="black")
            pos = new_pos
        elif c == "+":
            vec = rotate(vec, angle)
        elif c == "-":
            vec = rotate(vec, -angle)
        elif c == "[":
            stack.append((pos, vec))
        elif c == "]":
            pos, vec = stack.pop()

    plt.show()

if __name__ == "__main__":

    axiom = "F"
    axiom = "F--F--F"
    angle = 60
    n = 4
    rule = {
        "F": "F+F--F+F",
    }
    s = lsystem(axiom, rule, n)
    plot(s, angle)
