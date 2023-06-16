import cairo
from collections import deque
import math
from PIL import Image, ImageTk
import string
import tkinter as tk


WIDTH, HEIGHT = 512, 512 

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

theta, w = 90, 5
x, y = 256, 480
stack = []

def start():
    ctx.move_to(x, y)

def forward(length):
    global theta, w, x, y
    rad = math.radians(theta)
    pre_x, pre_y = x, y
    x += math.cos(rad) * length
    y -= math.sin(rad) * length
    # print(x0, y0, x, y)

    rad = math.radians(90-theta)
    x0 = pre_x + math.cos(rad) * w 
    y0 = pre_y + math.sin(rad) * w    
    x1 = pre_x - math.cos(rad) * w 
    y1 = pre_y - math.sin(rad) * w    
    x2 = x - math.cos(rad) * w 
    y2 = y - math.sin(rad) * w    
    x3 = x + math.cos(rad) * w 
    y3 = y + math.sin(rad) * w    

    ctx.move_to(x0, y0)
    ctx.line_to(x1, y1)
    ctx.line_to(x2, y2)
    ctx.line_to(x3, y3)
    ctx.line_to(x0, y0)
    # ctx.close_path()
    # ctx.set_source_rgba(0, 0, 0, 1)
    ctx.fill_preserve()
    ctx.stroke()
    ctx.move_to(x, y)

def left(length, angle):
    global theta, w, x
    theta += angle
    w = w / 2
    x = x - w
    forward(length)

def right(length, angle):
    global theta, w, x
    theta -= angle
    w = w / 2
    x = x + w
    forward(length)

def append():
    global theta, w, x, y
    stack.append((theta, w, (x, y)))

def pop():
    global theta, w, x, y
    theta, w, (x, y) = stack.pop()
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
    buf = surface.get_data()
    img = Image.frombuffer("RGBA", (w, h), buf, "raw", "RGBA", 0, 1)
    image = ImageTk.PhotoImage(img)
    tk.Label(root, image=image).pack()
    root.mainloop()

def lSysGenerate(s, d, order):
    for i in range(order):
        s = ''.join([d.get(c) or c for c in s])

    return s

if __name__ == "__main__":

    axiom = "X"
    length = 5
    angle = 25
    iterations = 5
    rule = {
        "X": "F[+X]F[-X]+X",
        "F": "FF",
    }
    s = lSysGenerate(axiom, rule, iterations)
    surface = draw(s, length, angle)

    # length, angle = 100, 30
    # w = 5
    # x, y = 256, 256
    # ctx.move_to(x, y)
    # rad = math.radians(angle)
    # x0 = x + math.cos(rad) * length 
    # y0 = x - math.sin(rad) * length
    # # ctx.line_to(x, y)
    # # ctx.stroke()
    # ctx.move_to(x0, y0)
    
    # ctx.set_source_rgb(1., 1., 0.)
    # rad = math.radians(90-angle)
    # x0 = x + math.cos(rad) * w 
    # y0 = y + math.sin(rad) * w    
    # ctx.move_to(x0, y0)
    # # ctx.stroke()

    # ctx.set_source_rgb(1., 0., 1.)
    # x1 = x - math.cos(rad) * w 
    # y1 = y - math.sin(rad) * w    
    # ctx.line_to(x1, y1)

    # x2 = x0 - math.cos(rad) * w 
    # y2 = y0 - math.sin(rad) * w    
    # ctx.line_to(x2, y2)

    # x3 = x0 + math.cos(rad) * w 
    # y3 = y0 + math.sin(rad) * w    
    # ctx.line_to(x3, y3)
    # ctx.line_to(x0, y0)
    # ctx.stroke()

    tkview(surface)

