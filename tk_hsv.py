import colorsys
import os
import tkinter as tk
import tkinter.ttk as ttk

def hsv2rgb(hsv: tuple) -> tuple:
    h, s, v = hsv
    rgb = colorsys.hsv_to_rgb(h/360., s/100., v/100.)
    return tuple(round(x*255.) for x in rgb)

def hsl2rgb(hsl: tuple) -> tuple:
    h, s, l = hsl 
    rgb = colorsys.hsv_to_rgb(h/360., s/100., l/100.)
    return tuple(round(x*255.) for x in rgb)

def rgb2hex(rgb: tuple) -> str:
    return "#%02x%02x%02x" % tuple(rgb)

def hsv2hex(hsv):
    rgb = hsv2rgb(hsv)
    return rgb2hex(rgb)

def jpfont():
    if os.name == "posix":
        font = "Yu Gothic"
    return font

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("HSV Model for Web Page")
        self.primary = "#FDFDFD" # < gray 50
        self.secondary = "#F5F5F5" # gray 100
        self.alert = "#EF5350" # red 400
        self.master.tk_setPalette(background=self.primary)

        style = ttk.Style()
        style.theme_use('classic')
        style.configure('c.TButton', borderwidth=0, padding=[2], background=self.secondary)

        frame_W = tk.Frame(self.master)
        frame_E = tk.Frame(self.master)
        frame_NE = tk.Frame(frame_E)
        frame_CE = tk.Frame(frame_E)
        frame_SE = tk.Frame(frame_E)
        frame_W.pack(side=tk.LEFT)
        frame_E.pack()
        frame_NE.pack()
        frame_CE.pack()
        frame_SE.pack()

        self.var_hue = tk.IntVar(value=180)
        self.var_sat = tk.IntVar(value=50)
        self.var_val = tk.IntVar(value=50)

        self.create_sample(frame_W)
        self.create_scales(frame_CE)
        self.create_matrix(frame_SE, hue=180)

    def create_sample(self, frame):
        self.canvas = tk.Canvas(frame, width=380, height=100)
        self.canvas.pack()
        self.rect = self.canvas.create_rectangle(10.0, 10.0, 580.0, 90.0, outline=hsv2hex((180, 50, 50)), fill=hsv2hex((180, 50, 50)))
        self.canvas.create_text(180.0, 50.0, text="日本語のTitle", font=("YuGo-Bold","24"))

    def callback(self, event=None):
        hue, sat, val = self.var_hue.get(), self.var_sat.get(), self.var_val.get()
        self.canvas.itemconfigure(self.rect, fill=hsv2hex([hue, sat, val]))
        self.change_matrix(hue)
        # self.mark_matrix(i, j=int(val/100))

    def create_scales(self, flame):
        self.scale_h = tk.Scale(flame, variable=self.var_hue, command=self.callback, orient=tk.HORIZONTAL, 
                    length=360, width=8, sliderlength=8, from_=0, to=360, resolution=1, tickinterval=100
                    )
        self.scale_h.pack()
        self.scale_s = tk.Scale(flame, variable=self.var_sat, command=self.callback, orient=tk.HORIZONTAL, 
                    length=360, width=8, sliderlength=8, from_=0, to=100, resolution=1, tickinterval=50
                    )
        self.scale_s.pack()
        self.scale_v = tk.Scale(flame, variable=self.var_val, command=self.callback, orient=tk.HORIZONTAL, 
                    length=360, width=8, sliderlength=8, from_=0, to=100, resolution=1, tickinterval=50
                    )
        self.scale_v.pack()

    def create_matrix(self, frame, hue):
        frm = tk.Frame(frame)
        frm.pack(padx=4)
        lbl = tk.Label(frm, text="Saturation")
        lbl.pack()
        self.lightness = tk.Canvas(frm, width=37, height=20)
        self.lightness.create_text(20, 15, text="Value")
        self.lightness.pack(padx=3, side=tk.LEFT)

        for i in range(11):
            xlim = tk.Canvas(frm, width=27, height=20)
            xlim.create_text(16, 12, text=f"{i*10}")
            xlim.pack(padx=3, side=tk.LEFT)

        self.matrix = [[] for _ in range(11)]
        for i in range(11):
            val = i*10
            frm = tk.Frame(frame)
            frm.pack()
            ylim = tk.Canvas(frm, width=37, height=27)
            ylim.create_text(20, 15, text=f"{i*10}")
            ylim.pack(padx=3, pady=3, side=tk.LEFT)
            for j in range(11):
                sat = j*10
                hsv = hue, sat, val
                canvas = tk.Canvas(frm, width=27, height=27, bg=hsv2hex(hsv))
                canvas.pack(padx=3, pady=3, side=tk.LEFT)
                self.matrix[i].append(canvas)

    def change_matrix(self, hue):
        for i in range(11):
            for j in range(11):
                hsv = hue, j*10, i*10
                self.matrix[i][j].delete("mark")
                self.matrix[i][j].config(bg=hsv2hex(hsv))

    def mark_matrix(self, i, j):
        this_color = self.matrix[i][j].cget("bg")
        self.matrix[i][j].config(bg="black")
        self.matrix[i][j].create_rectangle(4, 4, 26, 26, fill=this_color, outline="white", tag="mark")



if __name__ == "__main__":

    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()