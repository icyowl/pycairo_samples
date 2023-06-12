import cairo
import math
from PIL import Image, ImageTk
import tkinter as tk

def lSysGenerate(s, order):
    for i in range(order):
        s = lSysCompute(s)
    return s

def lSysCompute(s):
    d = {
        "F": "F+F",
    }
    return ''.join([d.get(c) or c for c in s])

def draw(s, lenght, angle):
    ...

axiom = "F"
length = 5
angle = 25.7
iterations = 2

s = lSysGenerate(axiom, iterations)
print(s)

surface = draw(s, length, angle)

WIDTH, HEIGHT = 512, 512 

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
c = cairo.Context(surface)

x0, y0 = 50, 50
x1, y1 = 180, 220    
x2, y2 = 350, 180
x3, y3 = 400, 50

c.move_to(x0, y0)
c.curve_to(x1, y1, x2, y2, x3, y3)        
c.stroke()

for x,y in [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]:
    c.arc(x-2, y-2, 4, 0, 2*math.pi)
    c.stroke()


# root = tk.Tk()
# label = tk.Label(root)
# label.pack()

# img = Image.frombuffer("RGBA", 
#                     (surface.get_width(), surface.get_height()),
#                     surface.get_data(),
#                     "raw", "RGBA", 0, 1)
# pimg = ImageTk.PhotoImage(img)
# label.configure(image=pimg)

# root.mainloop()