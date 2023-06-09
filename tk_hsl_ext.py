import colorsys
import os
import re
import tkinter as tk
import tkinter.ttk as ttk

def hsl2rgb(hsl: tuple) -> tuple:
    h, s, l = hsl
    rgb = colorsys.hls_to_rgb(h/360., l/100., s/100.)
    return tuple(round(x*255.) for x in rgb)

def rgb2hsl(rgb: tuple) -> tuple:
    r, g, b = [x/255. for x in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h*360, s*100, l*100

def rgb2hex(rgb: tuple) -> str:
    return "#%02x%02x%02x" % tuple(rgb)

def hex2rgb(code: tuple) -> tuple:
    c = code.strip("#")
    r, g, b = [int(x, 16) for x in (c[:2], c[2:4], c[4:])]
    return r, g, b

def hsl2hex(hsl):
    rgb = hsl2rgb(hsl)
    return rgb2hex(rgb)

def hex2hsl(code):
    rgb = hex2rgb(code)
    return rgb2hsl(rgb)

class Application(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("Hsl Model for Web Page")
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
        self.var_lit = tk.IntVar(value=50)

        tk.Label(frame_NW).pack()
        self.create_sample(frame_NW)
        self.create_entry(frame_SW)

        tk.Label(frame_NE).pack()
        self.draw_hue(frame_NE)
        self.create_scales(frame_CE)
        self.create_matrix(frame_SE, hue=180)
        self.mark_matrix(50, 50)
        tk.Label(frame_SE).pack()

    def entry_callback(self):
        hexrgb = self.entry.get()
        if re.fullmatch(r"[0-9|a-f|A-F]{6}", hexrgb[1:]) and hexrgb.startswith("#"):
            hue, sat, lit = hex2hsl(hexrgb)
            self.var_hue = tk.IntVar(value=round(hue))
            self.var_sat = tk.IntVar(value=round(sat))
            self.var_lit = tk.IntVar(value=round(lit))
            self.scale_h.config(variable=self.var_hue)
            self.scale_s.config(variable=self.var_sat)
            self.scale_v.config(variable=self.var_lit)
            self.change_matrix(hue)
            self.mark_matrix(sat, lit)
            self.cv_sample.itemconfigure(self.navbar, outline=hsl2hex([hue, sat, lit]), fill=hsl2hex([hue, sat, lit]))    
            self.cv_sample.itemconfigure(self.header, outline=hsl2hex([hue, sat, lit]), fill=hsl2hex([hue, sat, lit]))
            self.cv_sample.itemconfigure(self.title, fill=hsl2hex([hue, sat, lit]))
            self.cv_sample.itemconfigure(self.link, fill=hsl2hex([hue, sat, lit]))
            self.cv_sample.itemconfigure(self.body, outline=hsl2hex([hue, sat, lit]), fill=hsl2hex([hue, sat, lit]))
            self.cv_sample.itemconfigure(self.text, text=f"target color {hsl2hex([hue, sat, lit])}")
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
            hsl = i, 100., 50.
            hue_canvas.create_line(i, 0, i, 47, width=1, fill=hsl2hex(hsl))


    def create_sample(self, frame):
        self.cv_sample = tk.Canvas(frame, width=380, height=380)
        self.cv_sample.pack()
        hue, sat, lit = self.var_hue.get(), self.var_sat.get(), self.var_lit.get()
        self.navbar = self.cv_sample.create_rectangle(
            10.0,
            0.0,
            380.0,
            20.0,
            outline=hsl2hex([hue, sat-10, lit]), 
            fill=hsl2hex([hue, sat-10, lit]),
        )
        self.header = self.cv_sample.create_rectangle(
            10.0, 
            20.0, 
            380.0, 
            90.0, 
            outline=hsl2hex([hue, sat, lit]), 
            fill=hsl2hex([hue, sat, lit])
        )
        self.title = self.cv_sample.create_text(
            190.0, 
            45.0, 
            text="日本語のTitle", 
            font=("Yu Gothic","18", "bold"), 
            fill=hsl2hex([hue, sat+40, lit])
        )
        self.link = self.cv_sample.create_text(
            190.0,
            70.0,
            font=("Verdana", "12", "normal"),
            text="Home Blog Project About",
            fill=hsl2hex([hue, sat+30, lit])
        )
        self.body = self.cv_sample.create_rectangle(
            10.0,
            94.0,
            380.0,
            380.0,
            outline=hsl2hex([hue, sat-30, lit+30]),
            fill=hsl2hex([hue, sat-30, lit+30])
        )
        self.text = self.cv_sample.create_text(
            190.0,
            120.0,
            text=f"target color {hsl2hex([hue, sat, lit])}",
            font=("Yu Gothic", "12"),
            fill="#000"
        
        )


    def callback(self, event=None):
        hue, sat, lit = 203, 26, 92 #e5ecf0
        # 182, 18, 92 # e7eeee
        self.cv_sample.itemconfigure(self.navbar, outline=hsl2hex([hue, sat, lit]), fill=hsl2hex([hue, sat, lit]))
        self.cv_sample.itemconfigure(self.header, outline=hsl2hex([hue, sat, lit]), fill=hsl2hex([hue, sat, lit]))
        hue, sat, lit = 201, 16, 28
        self.cv_sample.itemconfigure(self.title, fill=hsl2hex([hue, sat, lit]))
        hue, sat, lit = self.var_hue.get(), self.var_sat.get(), self.var_lit.get()
        self.cv_sample.itemconfigure(self.link, fill=hsl2hex([hue, sat, lit]))

        hue, sat, lit = self.var_hue.get(), self.var_sat.get(), self.var_lit.get()
        self.cv_sample.itemconfigure(self.body, outline=hsl2hex([hue, sat, lit]), fill=hsl2hex([hue, sat, lit]))
        

        self.cv_sample.itemconfigure(self.text, text=f"target color {hsl2hex([hue, sat, lit])}")
        self.change_matrix(hue)
        self.mark_matrix(sat, lit)

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
        frm_lit = tk.Frame(frame)
        tk.Label(frm_lit, text="light").pack(side=tk.LEFT, padx=8)
        self.scale_v = tk.Scale(frm_lit, variable=self.var_lit, command=self.callback, orient=tk.HORIZONTAL, 
                    length=360, width=8, sliderlength=8, from_=0, to=100, resolution=1, tickinterval=50
                    )
        self.scale_v.pack()
        frm_lit.pack()


    def create_matrix(self, frame, hue):
        frm = tk.Frame(frame)
        frm.pack(padx=4)
        lbl = tk.Label(frm, text="Saturation")
        lbl.pack()
        self.lightness = tk.Canvas(frm, width=37, height=20)
        self.lightness.create_text(20, 15, text="Light")
        self.lightness.pack(padx=3, side=tk.LEFT)

        for i in range(11):
            xlim = tk.Canvas(frm, width=27, height=20)
            xlim.create_text(16, 12, text=f"{i*10}")
            xlim.pack(padx=3, side=tk.LEFT)

        self.matrix = [[] for _ in range(11)]
        for i in range(11):
            lit = i*10
            frm = tk.Frame(frame)
            frm.pack()
            ylim = tk.Canvas(frm, width=37, height=27)
            ylim.create_text(20, 15, text=f"{i*10}")
            ylim.pack(padx=3, pady=3, side=tk.LEFT)
            for j in range(11):
                sat = j*10
                hsl = hue, sat, lit
                canvas = tk.Canvas(frm, width=27, height=27, bg=hsl2hex(hsl))
                canvas.pack(padx=3, pady=3, side=tk.LEFT)
                self.matrix[i].append(canvas)

    def change_matrix(self, hue):
        for i in range(11):
            for j in range(11):
                hsl = hue, j*10, i*10
                self.matrix[i][j].delete("mark")
                self.matrix[i][j].config(bg=hsl2hex(hsl))

    def mark_matrix(self, sat, lit):
        i = int(lit/10)
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