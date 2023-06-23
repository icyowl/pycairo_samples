import math
import matplotlib.pyplot as plt 
import string
import random

def lSystem(s, rule, iterations):
    for _ in range(iterations):
        s = ''.join([rule.get(c) or c for c in s])

    return s

def plot(s, length, angle, alpha=1, colors={}):
    fig, ax = plt.subplots(figsize=(4,4))
    ax.set_aspect("equal")
    ax.axis("off")
    color = "k"
    theta = 90 + (random.random() - 0.5) * 5
    w = 5
    x, y = 0, 0
    stack = []
    for i, c in enumerate(s):
        if i == 0:
            length *= 2
        if i == 1:
            length /= 2
        if s[i-1] == "g":
            length *= 2
        if s[i-2] == "g":
            length /= 2
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


    plt.show()

if __name__ == "__main__":

    axiom = "X"
    length = 10
    angle = 20
    iterations = 8
    rule = {
        # "X": "F[+X]F[-X]+X",
        # "F": "FF"
        "X": "F/[+gX]-gX*",
        "g": "k"
    }
    s = lSystem(axiom, rule, iterations)
    plot(s, length, angle, alpha=1.2, colors={"g": (0,0,0,0.6), "k": (0,0,0,0.9)})