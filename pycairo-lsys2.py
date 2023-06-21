import cairo
from collections import deque
import math
from PIL import Image, ImageTk
import random
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
        self.w = 3

    def forward(self, length, opt1, opt2):
        theta = self.angle
        dx, dy = 0, 0
        if opt1 == "lean":
            if not opt2 == "long":
                theta = self.angle+21
                rad = math.radians(theta)
                dx = math.cos(rad) * length * 1.1
                dy = -math.sin(rad) * length * 1.1
            else:
                theta = self.angle+21+(0.5-random.random())*20
                rad = math.radians(theta)
                dx = math.cos(rad) * length * 4
                dy = -math.sin(rad) * length * 4
                self.ctx.set_source_rgba(128/256,128/256,128/256,1)
        elif opt1 == "long":
            rad = math.radians(self.angle)
            dx = math.cos(rad) * length * 4
            dy = -math.sin(rad) * length * 4
        else:
            if not opt2:
                rad = math.radians(self.angle)
                dx = math.cos(rad) * length 
                dy = -math.sin(rad) * length 
            elif opt2 == "short":
                rad = math.radians(self.angle)
                dx = math.cos(rad) * length / 6
                dy = -math.sin(rad) * length / 6
            elif opt2 == "long":
                theta = self.angle+(0.5-random.random())*20
                rad = math.radians(theta)
                dx = math.cos(rad) * length * 4
                dy = -math.sin(rad) * length * 4
                self.ctx.set_source_rgba(128/256,128/256,128/256,1)
        if opt2 == "tip":
            pass
        else:
            rad = math.radians(90-theta)
            x0 = self.x + math.cos(rad) * self.w 
            y0 = self.y + math.sin(rad) * self.w    
            x1 = self.x - math.cos(rad) * self.w 
            y1 = self.y - math.sin(rad) * self.w    
            x2 = self.x + dx - math.cos(rad) * self.w 
            y2 = self.y + dy - math.sin(rad) * self.w    
            x3 = self.x + dx + math.cos(rad) * self.w 
            y3 = self.y + dy + math.sin(rad) * self.w    

            self.ctx.move_to(x0, y0)
            self.ctx.line_to(x1, y1)
            self.ctx.line_to(x2, y2)
            self.ctx.line_to(x3, y3)
            self.ctx.line_to(x0, y0)
            self.ctx.fill_preserve()
            # self.ctx.line_to(self.x + dx, self.y + dy)
            self.ctx.stroke()
            self.ctx.set_source_rgba(0,0,0,1)
        self.x += dx
        self.y += dy
        self.ctx.move_to(self.x, self.y)




    # rad = math.radians(90-theta)
    # x0 = pre_x + math.cos(rad) * w 
    # y0 = pre_y + math.sin(rad) * w    
    # x1 = pre_x - math.cos(rad) * w 
    # y1 = pre_y - math.sin(rad) * w    
    # x2 = x - math.cos(rad) * w 
    # y2 = y - math.sin(rad) * w    
    # x3 = x + math.cos(rad) * w 
    # y3 = y + math.sin(rad) * w    

    # ctx.move_to(x0, y0)
    # ctx.line_to(x1, y1)
    # ctx.line_to(x2, y2)
    # ctx.line_to(x3, y3)
    # ctx.line_to(x0, y0)
    # # ctx.close_path()
    # # ctx.set_source_rgba(0, 0, 0, 1)
    # ctx.fill_preserve()
    # ctx.stroke()
    # ctx.move_to(x, y)


    def left(self, length, angle, opt1, opt2):
        self.angle += angle
        self.w = self.w / 2
        self.x = self.x - self.w
        self.forward(length, opt1, opt2)

    def right(self, length, angle, opt1, opt2):
        self.angle -= angle
        self.w = self.w / 2
        self.x = self.x + self.w
        self.forward(length, opt1, opt2)

    def append(self):
        self.stack.append((self.angle, self.w, (self.x, self.y)))

    def pop(self):
        self.angle, self.w, (self.x, self.y) = self.stack.pop()
        self.ctx.move_to(self.x, self.y)

    def draw(self, s, length, angle):
        for i, c in enumerate(s):
            opt1, opt2 = "", ""
            if 1020 <= i:
                opt1 = "lean"
            if i < 5:
                opt1 = "long"
            if i >= len(s) - 2:
                opt2 = "tip"
            else:
                if s[i+1] == "]" or s[i+2] == "]":
                    opt2 = "tip"
            if i < len(s) - 4:
                if s[i+4] == "]" and s[i+1] == "[":
                    if s[i+2] == "-":
                        opt2 = "tip"
                    else:
                        opt2 = "long"
            if 510 < i and i < 526:
                opt2 = "short"
            if c in string.ascii_letters:
                self.forward(length, opt1, opt2)
            elif c == '-':
                self.left(length, angle, opt1, opt2)
            elif c == '+':
                self.right(length, angle, opt1, opt2)
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

    # https://github.com/pvigier/lsystem *3dplot
    # https://gpfault.net/posts/generating-trees.txt.html *purple

    axiom = "X"
    length = 6
    angle = 25.7
    iterations = 5
    rule = {
        "X": "F[+X]F[-X]+X",
        "F": "FF"
    }

    s = lSysGenerate(axiom, rule, iterations)
    draw = Draw512(initial_angle=90, initial_x=256, initial_y=480)
    surface = draw.draw(s, length, angle)
    view(surface)