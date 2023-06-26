from collections import deque
import math
import matplotlib.pyplot as plt 
import string

def lSystem(s, rule, iterations):
    for _ in range(iterations):
        s = ''.join([rule.get(c) or c for c in s])

    return s

def plot(s, angle):
    fig, ax = plt.subplots(figsize=(4,4))
    ax.set_aspect("equal")
    ax.axis("off")
    color = "k"
    theta = 0
    x, y = 0, 0
    stack = deque()
    for i, c in enumerate(s):
        if c in string.ascii_letters:
            rad = math.radians(theta)
            dx = math.cos(rad)
            dy = math.sin(rad)
            ax.plot((x, (x+dx)), (y, (y+dy)), c=color)
            x += dx 
            y += dy
        elif c == "-":
            theta += angle
        elif c == "+":
            theta -= angle
        elif c == "[":
            stack.append((theta, x, y))
        elif c == "]":
            theta, x, y = stack.pop()

    plt.show()

if __name__ == "__main__":

    axiom = "F-F-F-F"
    angle = 90py
    iterations = 4
    rule = {
        # "F": "F+F-F-F+F",
        "F": "FF-F-F-F-FF"
    }
    s = lSystem(axiom, rule, iterations)
    plot(s, angle)




