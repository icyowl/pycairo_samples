import math
import matplotlib.pyplot as plt 
import string

# fig, ax = plt.subplots(figsize=(4, 4))
# ax.set_xlim([0, 512])
# ax.set_ylim([0, 512])
# ax.axis("off")


class Lsys0:
    def __init__(self, ax):
        self.ax = ax
        self.theta = 90
        self.x = 256
        self.y = 0
        self.stack = []

    def forward(self, length):
        rad = math.radians(self.theta)
        dx = math.cos(rad) * length
        dy = math.sin(rad) * length
        self.ax.arrow(self.x, self.y, dx, dy)
        self.x += dx
        self.y += dy

    def left(self, length, angle):
        self.theta += angle
        self.forward(length)

    def right(self, length, angle):
        self.theta -= angle
        self.forward(length)

    def append(self):
        self.stack.append((self.theta, (self.x, self.y)))

    def pop(self):
        self.theta, (self.x, self.y) = self.stack.pop()

    def draw(self, s, length, angle):
        for c in s:
            if c in string.ascii_letters:
                self.forward(length)
            elif c == '-':
                self.left(length, angle)
            elif c == '+':
                self.right(length, angle)
            elif c == "[":
                self.append()
            elif c == "]":
                self.pop()

    def show(self, axiom, length, angle, iterations, rule):
        self.ax.text(0, 150, f"axiom: {axiom}")
        self.ax.text(0, 120, f"length: {length}")
        self.ax.text(0, 90, f"θ: {angle}")
        self.ax.text(0, 60, f"n: {iterations}")
        for i, k in enumerate(rule.keys()):
            txt = k + " → " + rule.get(k)
            self.ax.text(0, 30 - i*30, txt)

class Lsys1:
    def __init__(self, ax):
        self.ax = ax
        self.theta = 90
        self.x = 256
        self.y = 0
        self.stack = []

    def forward(self, length, color):
        rad = math.radians(self.theta)
        # if color == "green":
        #     dx = math.cos(rad) * length * 2
        #     dy = math.sin(rad) * length * 2
        # else:
        dx = math.cos(rad) * length
        dy = math.sin(rad) * length
        if color == "purple":
            dx = dx/3
            dy = dy/3
        if color != "red":
            self.ax.arrow(self.x, self.y, dx, dy, edgecolor=color)
        self.x += dx
        self.y += dy

    def left(self, length, angle, color):
        self.theta += angle
        self.forward(length, color)

    def right(self, length, angle, color):
        self.theta -= angle
        self.forward(length, color)

    def append(self):
        self.stack.append((self.theta, (self.x, self.y)))

    def pop(self):
        self.theta, (self.x, self.y) = self.stack.pop()

    def draw(self, s, length, angle):
        for i, c in enumerate(s):
            color = None
            if i < len(s) - 2:
                if s[i+1] == "]" or s[i+2] == "]":
                    color = "red"
            # if i < len(s) - 4:
            #     if s[i+4] == "]":
            #         color = "green"
            if 510 < i and i < 526:
                color = "purple"
            if c in string.ascii_letters:
                self.forward(length, color)
            elif c == '-':
                self.left(length, angle, color)
            elif c == '+':
                self.right(length, angle, color)
            elif c == "[":
                self.append()
            elif c == "]":
                self.pop()

    def show(self, axiom, length, angle, iterations, rule):
        self.ax.text(0, 150, f"axiom: {axiom}")
        self.ax.text(0, 120, f"length: {length}")
        self.ax.text(0, 90, f"θ: {angle}")
        self.ax.text(0, 60, f"n: {iterations}")
        for i, k in enumerate(rule.keys()):
            txt = k + " → " + rule.get(k)
            self.ax.text(0, 30 - i*30, txt)

def lSysGenerate(s, d, order):
    for i in range(order):
        s = ''.join([d.get(c) or c for c in s])

    return s

if __name__ == "__main__":

    # fig, ax = plt.subplots()
    # ax.set_xlim((0,512))
    # ax.set_ylim((0,512))
    # ax.axis("off")

    # https://www.frontiersin.org/articles/10.3389/fpls.2012.00076/full#B13

    fig, axs = plt.subplots(1,2,figsize=(8,4))
    for ax in axs:
        ax.set_xlim((0,512))
        ax.set_ylim((0,512))
        ax.axis("off")

    axiom = "X"
    length = 7
    angle = 25.7
    iterations = 5
    rule = {
        "X": "F[+X]F[-X]+X",
        "F": "FF",
    }
    s = lSysGenerate(axiom, rule, iterations)
    lsys0 = Lsys0(axs[0])
    lsys0.draw(s, length, angle)
    lsys0.show(axiom, length, angle, iterations, rule)

    axiom = "X"
    length = 7
    angle = 25.7
    iterations = 5
    rule = {
        "X": "F[+X]F[-X]+X",
        "F": "FF",
    }
    s = lSysGenerate(axiom, rule, iterations)
    # print(s)
    lsys1 = Lsys1(axs[1])
    lsys1.draw(s, length, angle)
    lsys1.show(axiom, length, angle, iterations, rule)

    plt.show()

    # s = "FFFFFFFFFFFFFFFF[+FFFFFFFF[+FFFF[+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFF[-FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFFFFFF[-FFFF[+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFF[-FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FFFF[+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]FFFF[-FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]+FF[+F[+X]F[-X]+X]FF[-F[+X]F[-X]+X]+F[+X]F[-X]+X]"
    # print(len(s)) # 263