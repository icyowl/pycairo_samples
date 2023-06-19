import cairo
from collections import deque
import math
from PIL import Image, ImageTk
import string
import tkinter as tk

class Draw512:
    def __init__(self, initial_angle, initial_x, initial_y):
        self.angle, self.x, self.y = initial_angle, initial_x, initial_y
        self.stack = []

        w, h = 512, 512 
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
        self.ctx = cairo.Context(self.surface)
        self.ctx.move_to(self.x, self.y)

    def forward(self, length):
        rad = math.radians(self.angle)
        self.x += math.cos(rad) * length
        self.y -= math.sin(rad) * length
        self.ctx.line_to(self.x, self.y)
        self.ctx.stroke()
        self.ctx.move_to(self.x, self.y)

    def left(self, length, angle):
        self.angle += angle
        self.forward(length)

    def right(self, length, angle):
        self.angle -= angle
        self.forward(length)

    def append(self):
        self.stack.append((self.angle, (self.x, self.y)))

    def pop(self):
        self.angle, (self.x, self.y) = self.stack.pop()
        self.ctx.move_to(self.x, self.y)

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
        
        return self.surface

def view(surface):
    root = tk.Tk()
    root.title("L-system")
    cimg = Image.frombuffer("RGBA", 
                        (surface.get_width(), surface.get_height()),
                        surface.get_data(),
                        "raw", "RGBA", 0, 1)
    image = ImageTk.PhotoImage(cimg)
    tk.Label(image=image).pack()

    root.mainloop()

def lSysGenerate(s, d, order):
    for i in range(order):
        s = ''.join([d.get(c) or c for c in s])

    return s

if __name__ == "__main__":

    # axiom = "-F"
    # length = 2
    # angle = 90
    # iterations = 4

    axiom = "X"
    length = 6
    angle = 24.7
    iterations = 5
    rule = {
        "X": "F[+X]F[-X]+X",
        "F": "FF"
    }

    s = lSysGenerate(axiom, rule, iterations)
    draw = Draw512(initial_angle=90, initial_x=256, initial_y=480)
    surface = draw.draw(s, length, angle)
    view(surface)
