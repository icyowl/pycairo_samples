import cairo
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
        "F": "F+F-F-F+F",
    }
    return ''.join([d.get(c) or c for c in s])


# surface = draw(s, length, angle)

WIDTH, HEIGHT = 512, 512 

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
c = cairo.Context(surface)

global a, x, y
a, x, y = 0, 256, 500

def start():
    global x, y
    x, y = 256, 500
    c.move_to(x, y)

def forward(length):
    global x, y
    y -= length
    c.line_to(x, y)
    c.stroke()
    c.move_to(x, y)

def left(length, angle):
    global x, y
    rad = math.radians(90-angle)
    x -= math.cos(rad) * length
    y -= math.sin(rad) * length
    print(x, y)
    c.line_to(x, y)
    c.stroke()
    c.move_to(x, y)

def right(length, angle):
    global x, y
    rad = math.radians(90-angle)
    x += math.cos(rad) * length
    y -= math.sin(rad) * length
    print(x, y)
    c.line_to(x, y)
    c.stroke()
    c.move_to(x, y)

def draw(s, length, angle):
    global x, y
    start()
    for c in s:
        if c in string.ascii_letters:
            forward(length)
        elif c == '-':
            left(length, angle)
        elif c == '+':
            right(length, angle)
        # elif c == "[":
        #     agl = t.heading()
        #     pos = [t.xcor(), t.ycor()]
        #     stack.append((agl, pos))
        # elif c == "]":
        #     agl, pos = stack.pop()
        #     t.setheading(agl)
        #     t.penup()
        #     t.goto(pos[0], pos[1])
        #     t.pendown()

axiom = "-F"
length = 5
angle = 90
iterations = 3

s = lSysGenerate(axiom, iterations)
print(s)
draw(s, length, angle)

root = tk.Tk()
label = tk.Label(root)
label.pack()

img = Image.frombuffer("RGBA", 
                    (surface.get_width(), surface.get_height()),
                    surface.get_data(),
                    "raw", "RGBA", 0, 1)
pimg = ImageTk.PhotoImage(img)
label.configure(image=pimg)

root.mainloop()