import cairo
from collections import deque
import math
from PIL import Image, ImageTk
import string
import tkinter as tk

def lSysGenerate(s, order):
    for i in range(order):
        s = lSysCompute(s)
    return s

def lSysCompute(s):
    d = {
        # "F": "F+F-F-F+F",
        # "F": "F[+F]F[-F]F",
        # "F": "FF-[-F+F+F]+[+F-F-F]",
        "X": "F[+X]F[-X]+X",
        "F": "FF"
    }
    return ''.join([d.get(c) or c for c in s])


WIDTH, HEIGHT = 512, 512 

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

dgr, x, y = 90, 420, 256
dgr, x, y = 90., 256., 480.
# stack = deque()
stack = []

def start():
    global x, y
    ctx.move_to(x, y)

def forward(length):
    global dgr, x, y
    rad = math.radians(dgr)
    x += math.cos(rad) * length
    y -= math.sin(rad) * length
    ctx.line_to(x, y)
    ctx.stroke()
    ctx.move_to(x, y)

def left(length, angle):
    global dgr, x, y
    dgr = dgr + angle
    rad = math.radians(dgr)
    x += math.cos(rad) * length
    y -= math.sin(rad) * length
    ctx.line_to(x, y)
    ctx.stroke()
    ctx.move_to(x, y)

def right(length, angle):
    global dgr, x, y
    dgr = dgr - angle
    rad = math.radians(dgr)
    x += math.cos(rad) * length
    y -= math.sin(rad) * length
    ctx.line_to(x, y)
    ctx.stroke()
    ctx.move_to(x, y)

def append():
    global dgr, x, y
    stack.append((dgr, (x, y)))

def pop():
    global dgr, x, y
    dgr, (x, y) = stack.pop()
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

# axiom = "-F"
# length = 2
# angle = 90
# iterations = 4

axiom = "X"
length = 6
angle = 20
iterations = 4

s = lSysGenerate(axiom, iterations)
# print(s[:5])
draw(s, length, angle)


root = tk.Tk()
root.title("L-system")
label = tk.Label(root)
label.pack()

img = Image.frombuffer("RGBA", 
                    (surface.get_width(), surface.get_height()),
                    surface.get_data(),
                    "raw", "RGBA", 0, 1)
imgTk = ImageTk.PhotoImage(img)
label.configure(image=imgTk)

root.mainloop()