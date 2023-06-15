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
    _x, _y = x, y
    x += math.cos(rad) * length
    y -= math.sin(rad) * length
    print(_x, _y, x, y)
    # ctx.line_to(x, y)
    # ctx.stroke()
    # ctx.move_to(x, y)
    breadth = 5
    r = math.radians(90-angle)
    x0 = _x + math.cos(r) * breadth 
    y0 = _y + math.sin(r) * breadth    
    x1 = _x - math.cos(r) * breadth 
    y1 = _y - math.sin(r) * breadth    
    x2 = x - math.cos(r) * breadth 
    y2 = y - math.sin(r) * breadth    
    x3 = x + math.cos(r) * breadth 
    y3 = y + math.sin(r) * breadth    
    ctx.move_to(x0, y0)
    ctx.line_to(x1, y1)
    ctx.line_to(x2, y2)
    ctx.line_to(x3, y3)
    ctx.line_to(x0, y0)
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
    length = 20
    angle = 25
    iterations = 2
    rule = {
        "X": "F[+X]F[-X]+X",
        "F": "FF",
    }
    s = lSysGenerate(axiom, rule, iterations)
    surface = draw(s, length, angle)

    # length, angle = 100, 30
    # breadth = 5
    # x, y = 256, 256
    # ctx.move_to(x, y)
    # rad = math.radians(angle)
    # _x = x + math.cos(rad) * length 
    # _y = x - math.sin(rad) * length
    # # ctx.line_to(x, y)
    # # ctx.stroke()
    # ctx.move_to(_x, _y)
    
    # ctx.set_source_rgb(1., 1., 0.)
    # rad = math.radians(90-angle)
    # x0 = x + math.cos(rad) * breadth 
    # y0 = y + math.sin(rad) * breadth    
    # ctx.move_to(x0, y0)
    # # ctx.stroke()

    # ctx.set_source_rgb(1., 0., 1.)
    # x1 = x - math.cos(rad) * breadth 
    # y1 = y - math.sin(rad) * breadth    
    # ctx.line_to(x1, y1)

    # x2 = _x - math.cos(rad) * breadth 
    # y2 = _y - math.sin(rad) * breadth    
    # ctx.line_to(x2, y2)

    # x3 = _x + math.cos(rad) * breadth 
    # y3 = _y + math.sin(rad) * breadth    
    # ctx.line_to(x3, y3)
    # ctx.line_to(x0, y0)
    # ctx.stroke()

    tkview(surface)

