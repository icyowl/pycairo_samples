import math
import matplotlib.pyplot as plt 
import random
import string

def lSystem(s, rule, iterations):
    f = lambda: random.choice(["P1", "P2", "P3"])
    for _ in range(iterations):
        s = ''.join([rule.get(f()) if c == "X" else c for c in s])
    return s

# def lSystem(s, rule, iterations):
#     for _ in range(iterations):
#         s = ''.join([rule.get(c) or c for c in s])
#     return s

def plot(s, angle):
    fig, ax = plt.subplots(figsize=(4,4))
    ax.set_aspect("equal")
    ax.axis("off")
    color = "k"
    theta = 90
    x, y = 0, 0
    stack = []
    for i, c in enumerate(s):
        if c in string.ascii_uppercase:
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

    axiom = "X"
    angle = 25
    iterations = 6
    rule = {
        # "F": "F[+F]F[-F]F",
        "P1": "F[+X][-X]X",
        "P2": "F[+X]-X",
        "P3": "F[+X]-X"
    }
    s = lSystem(axiom, rule, iterations)
    plot(s, angle)