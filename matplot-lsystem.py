from collections import deque
import math
import matplotlib.pyplot as plt 
import string

def lSystem(s, rule, n):
    for _ in range(n):
        s = ''.join([rule.get(c) or c for c in s])

    return s

def plot(s, angle):
    facecolor = '#dee2e6'  # gray-300
    color = '#6610f2'  # indigo
    fig = plt.figure(figsize=(4,3), facecolor=facecolor)
    ax = fig.add_subplot(facecolor=facecolor)
    ax.set_aspect("equal")
    ax.axis("off")
    theta = 0
    x, y = 5, 15
    stack = deque()
    for i, c in enumerate(s):
        if c in string.ascii_letters:
            rad = math.radians(theta)
            dx = math.cos(rad)
            dy = math.sin(rad)
            ax.plot((x, (x+dx)), (y, (y+dy)), c=color)
            x += dx 
            y += dy
        elif c == "+":
            theta += angle
        elif c == "-":
            theta -= angle
        elif c == "[":
            stack.append((theta, x, y))
        elif c == "]":
            theta, x, y = stack.pop()

    # plt.show()
    plt.savefig('dragon.png')

if __name__ == "__main__":

    # axiom = "F--F--F"
    # # axiom = "F-F-F-F"
    # angle = 60
    # n = 4
    # rule = {
    #     "F": "F+F--F+F",
    #     # "F": "FF-F-F-F-FF"
    # }
    # s = lSystem(axiom, rule, n)
    # plot(s, angle)

    axiom = 'A'
    angle = 90
    n = 14
    rule = {
        'A': 'A+B+',
        'B': '-A-B'
    }
    s = lSystem(axiom, rule, n)
    plot(s, angle)




