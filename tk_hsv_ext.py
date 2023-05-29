import colorsys
import os
import re
import tkinter as tk
import tkinter.ttk as ttk

def hsv2rgb(hsv: tuple) -> tuple:
    h, s, v = hsv
    rgb = colorsys.hsv_to_rgb(h/360., s/100., v/100.)
    return tuple(round(x*255.) for x in rgb)

def rgb2hsv(rgb: tuple) -> tuple:
    r, g, b = [x/255. for x in rgb]
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return h*360, s*100, v*100

def rgb2hex(rgb: tuple) -> str:
    return "#%02x%02x%02x" % tuple(rgb)

def hex2rgb(code: tuple) -> tuple:
    c = code.strip("#")
    r, g, b = [int(x, 16) for x in (c[:2], c[2:4], c[4:])]
    return r, g, b

def hsv2hex(hsv):
    rgb = hsv2rgb(hsv)
    return rgb2hex(rgb)

def hex2hsv(code):
    rgb = hex2rgb(code)
    return rgb2hsv(rgb)

BG_sat, BG_val = 0.0, 98.0
TXT_sat, TXT_val = 1.0, 99.0
TXT_sat, TXT_val = 30.0, 30.0

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
        frame_NNW = tk.Frame(frame_W)
        frame_NW = tk.Frame(frame_W)
        frame_SW = tk.Frame(frame_W)
        frame_NE = tk.Frame(frame_E)
        frame_CE = tk.Frame(frame_E)
        frame_SE = tk.Frame(frame_E)
        frame_W.pack(side=tk.LEFT, anchor=tk.N)
        frame_NW.pack()
        frame_SW.pack()
        frame_E.pack()
        frame_NE.pack()
        frame_CE.pack()
        frame_SE.pack()

        self.var_hue = tk.IntVar(value=180)
        self.var_sat = tk.IntVar(value=50)
        self.var_val = tk.IntVar(value=50)

        tk.Label(frame_NW).pack()
        self.create_sample(frame_NW)
        self.create_entry(frame_SW)

        tk.Label(frame_NE).pack()
        self.draw_hue(frame_NE)
        self.create_scales(frame_CE)
        self.create_matrix(frame_SE, hue=180)
        self.mark_matrix(50, 50)
        tk.Label(frame_SE).pack()

    def text_color(self, sat, val):
        ...

    def background_color(self, sat, val):
        ...

    def entry_callback(self):
        hexrgb = self.entry.get()
        if re.fullmatch(r"[0-9|a-f|A-F]{6}", hexrgb[1:]) and hexrgb.startswith("#"):
            hue, sat, val = hex2hsv(hexrgb)
            self.var_hue = tk.IntVar(value=round(hue))
            self.var_sat = tk.IntVar(value=round(sat))
            self.var_val = tk.IntVar(value=round(val))
            self.scale_h.config(variable=self.var_hue)
            self.scale_s.config(variable=self.var_sat)
            self.scale_v.config(variable=self.var_val)
            self.change_matrix(hue)
            self.mark_matrix(sat, val)
            self.cv_sample.itemconfigure(self.header, outline=hsv2hex([hue, sat, val]), fill=hsv2hex([hue, sat, val]))
            self.cv_sample.itemconfigure(self.title, fill=hsv2hex([hue, TXT_sat, TXT_val]))
            self.cv_sample.itemconfigure(self.body, outline=hsv2hex([hue, BG_sat, BG_val]), fill=hsv2hex([hue, BG_sat, BG_val]))
            self.cv_sample.itemconfigure(self.text, text=f"primary color {hsv2hex([hue, sat, val])}")
        else:
            ...
            # self.lbl_2lch.config(text="example: #5F9EA0", fg=self.alert)
            # self.canvas_2lch.config(bg=self.secondary)

    def create_entry(self, frame):
        frm_entry = tk.Frame(frame)
        frm_entry.pack(padx=8, pady=16)
        tk.Label(frm_entry, text="Hex").pack(side=tk.LEFT)
        self.entry = tk.Entry(frm_entry, width=10, bg="#fff")
        self.entry.pack(side=tk.LEFT, padx=2)
        btn = ttk.Button(
            frm_entry, 
            text="submit", 
            style="c.TButton", 
            command=self.entry_callback
            )
        btn.pack(padx=2)

    def draw_hue(self, frame):
        tk.Label(frame, text="").pack(side=tk.LEFT, padx=18)
        hue_canvas = tk.Canvas(frame, width=360, height=27)
        hue_canvas.pack()
        for i in range(360):
            hsv = i, 100., 100.
            hue_canvas.create_line(i, 0, i, 47, width=1, fill=hsv2hex(hsv))


    def create_sample(self, frame):
        self.cv_sample = tk.Canvas(frame, width=380, height=380)
        self.cv_sample.pack()
        hue, sat, val = self.var_hue.get(), self.var_sat.get(), self.var_val.get()
        h, s, v = 198, 8, 86
        self.navbar = self.cv_sample.create_rectangle(
            10.0,
            0.0,
            380.0,
            20.0,
            outline=hsv2hex([h, s, v]), 
            fill=hsv2hex([h, s, v]),
        )
        print(hsv2hex([h, s, v]))
        self.header = self.cv_sample.create_rectangle(
            10.0, 
            20.0, 
            380.0, 
            90.0, 
            outline=hsv2hex([h, s, v]), 
            fill=hsv2hex([h, s, v])
        )
        self.title = self.cv_sample.create_text(
            190.0, 
            45.0, 
            text="日本語のTitle", 
            font=("Yu Gothic","18", "bold"), 
            fill=hsv2hex([200., 26., 32.]) # #3c4b52
        )
        self.link = self.cv_sample.create_text(
            190.0,
            70.0,
            font=("Verdana", "12", "normal"),
            text="Home Blog Project About",
            fill=hsv2hex([200., 39., 41.]) # #405b69
        )
        self.body = self.cv_sample.create_rectangle(
            10.0,
            94.0,
            380.0,
            380.0,
            outline=hsv2hex([hue, BG_sat, BG_val]),
            fill=hsv2hex([hue, BG_sat, BG_val])
        )
        self.text = self.cv_sample.create_text(
            190.0,
            120.0,
            text=f"primary color {hsv2hex([hue, sat, val])}",
            font=("Yu Gothic", "12"),
            fill="#000"
        )


    def callback(self, event=None):
        hue, sat, val = self.var_hue.get(), self.var_sat.get(), self.var_val.get()
        self.cv_sample.itemconfigure(self.navbar, outline=hsv2hex([hue, sat, val]), fill=hsv2hex([hue, sat, val]))
        print(hsv2hex([hue, sat, val]))
        # self.cv_sample.itemconfigure(self.header, outline=hsv2hex([hue, sat, val]), fill=hsv2hex([hue, sat, val]))
        # self.cv_sample.itemconfigure(self.title, fill=hsv2hex([hue, sat, val]))
        # self.cv_sample.itemconfigure(self.link, fill=hsv2hex([hue, sat, val]))
        self.cv_sample.itemconfigure(self.body, outline=hsv2hex([198, BG_sat, BG_val]), fill=hsv2hex([198, BG_sat, BG_val]))
        # self.cv_sample.itemconfigure(self.text, text=f"primary color {hsv2hex([hue, sat, val])}")
        self.change_matrix(hue)
        self.mark_matrix(sat, val)
        # print(hsv2hex([hue, sat, val]))

    def create_scales(self, frame):
        frm_hue = tk.Frame(frame)
        tk.Label(frm_hue, text="hue").pack(side=tk.LEFT, padx=8)
        self.scale_h = tk.Scale(frm_hue, variable=self.var_hue, command=self.callback, orient=tk.HORIZONTAL, 
                    length=360, width=8, sliderlength=8, from_=0, to=360, resolution=1, tickinterval=100
                    )
        self.scale_h.pack()
        frm_hue.pack()
        frm_sat = tk.Frame(frame)
        tk.Label(frm_sat, text="sat").pack(side=tk.LEFT, padx=8)
        self.scale_s = tk.Scale(frm_sat, variable=self.var_sat, command=self.callback, orient=tk.HORIZONTAL, 
                    length=360, width=8, sliderlength=8, from_=0, to=100, resolution=1, tickinterval=50
                    )
        self.scale_s.pack()
        frm_sat.pack()
        frm_val = tk.Frame(frame)
        tk.Label(frm_val, text="val").pack(side=tk.LEFT, padx=8)
        self.scale_v = tk.Scale(frm_val, variable=self.var_val, command=self.callback, orient=tk.HORIZONTAL, 
                    length=360, width=8, sliderlength=8, from_=0, to=100, resolution=1, tickinterval=50
                    )
        self.scale_v.pack()
        frm_val.pack()


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

    def mark_matrix(self, sat, val):
        i = int(val/10)
        j = int(sat/10)
        this_color = self.matrix[i][j].cget("bg")
        self.matrix[i][j].config(bg="black")
        gap = 4
        if os.name == "posix":
            gap = 6
        self.matrix[i][j].create_rectangle(gap, gap, 26, 26, fill=this_color, outline="#fff", tag="mark")

if __name__ == "__main__":

    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()

#   /* new */
#   --primarycolor:#cad6db;
#   --secondarycolor:#3c4b52;
#   --linkcolor:#405b69;
#   --hovercolor: #283a42;
#   --nenu-active-color: var(--hovercolor);
#   --page-backgroundcolor: #fafcfc;