import cairo
from collections import deque
import math
from PIL import Image, ImageTk
import string
import tkinter as tk


WIDTH, HEIGHT = 512, 512 

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

theta, x, y = 90, 256, 480
stack = []

def start():
    ctx.move_to(x, y)

def forward(length):
    global theta, x, y
    rad = math.radians(theta)
    x += math.cos(rad) * length
    y -= math.sin(rad) * length
    ctx.line_to(x, y)
    ctx.stroke()
    ctx.move_to(x, y)

def left(length, angle):
    global theta
    theta += angle
    forward(length)

def right(length, angle):
    global theta
    theta -= angle
    forward(length)

def append():
    stack.append((theta, (x, y)))

def pop():
    global theta, x, y
    theta, (x, y) = stack.pop()
    ctx.move_to(x, y)

def draw(s, length, angle):
    start()
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
    
    return surface

def tkview(surface):
    root = tk.Tk()
    root.title("L-system")
    w, h = surface.get_width(), surface.get_height()
    img = Image.frombuffer("RGBA", (w, h), surface.get_data(), "raw", "RGBA", 0, 1)
    image = ImageTk.PhotoImage(img)
    tk.Label(root, image=image).pack()
    root.mainloop()

def lSysGenerate(s, d, order):
    for i in range(order):
        s = ''.join([d.get(c) or c for c in s])

    return s

if __name__ == "__main__":

    axiom = "X"
    length = 6
    angle = 25
    iterations = 5
    rule = {
        "X": "F[+X]F[-X]+X",
        "F": "FF",
    }
    s = lSysGenerate(axiom, rule, iterations)
    surface = draw(s, length, angle)
    tkview(surface)

