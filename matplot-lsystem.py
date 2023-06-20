import math
import matplotlib.pyplot as plt 
import string

# fig = plt.figure(figsize=(4, 12))
# ax = fig.add_subplot(3, 1, 1)
# ax2 = fig.add_subplot(3, 1, 2)
# ax3 = fig.add_subplot(3, 1, 3)


fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim([0, 512])
ax.set_ylim([0, 512])
ax.axis("off")

theta, x, y = 90, 256, 0
stack = []

def forward(length):
    global theta, x, y
    rad = math.radians(theta)
    dx = math.cos(rad) * length
    dy = math.sin(rad) * length
    ax.arrow(x, y, dx, dy)
    x += dx
    y += dy

def left(length, angle):
    global theta
    theta += angle
    forward(length)

def right(length, angle):
    global theta
    theta -= angle
    forward(length)

def append():
    global theta, x, y
    stack.append((theta, (x, y)))

def pop():
    global theta, x, y
    theta, (x, y) = stack.pop()

def draw(s, length, angle):
    for c in s:
        if c in string.ascii_letters:
            forward(length)
        elif c == '-':
            left(length, angle)
        elif c == '+':
            right(length, angle)
        elif c == "[":
            append()
        elif c == "]":
            pop()

def show(axiom, length, angle, iterations, rule):
    plt.text(0, 150, f"axiom: {axiom}")
    plt.text(0, 120, f"length: {length}")
    plt.text(0, 90, f"θ: {angle}")
    plt.text(0, 60, f"n: {iterations}")
    for i, k in enumerate(rule.keys()):
        txt = k + " → " + rule.get(k)
        plt.text(0, 30 - i*30, txt)
    plt.show()

def lSysGenerate(s, d, order):
    for i in range(order):
        s = ''.join([d.get(c) or c for c in s])

    return s

if __name__ == "__main__":

    axiom = "X"
    length = 5
    angle = 25.7
    iterations = 5
    rule = {
        # "X": "F[+X]F[-X]+X",
        # "F": "FF",
        "X": "F[+X]-X",
        "F": "FF"
    }
    s = lSysGenerate(axiom, rule, iterations)
    draw(s, length, angle)
    show(axiom, length, angle, iterations, rule)




