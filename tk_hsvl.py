import colorsys
import re
import tkinter as tk

def hsv2rgb(hsv: tuple) -> tuple:
    h, s, v = hsv
    rgb = colorsys.hsv_to_rgb(h/360., s/100., v/100.)
    return rgb

def hsl2rgb(hsl: tuple) -> tuple:
    h, s, l = hsl 
    rgb = colorsys.hls_to_rgb(h/360., l/100., s/100.)
    return rgb

def rgb2hex(rgb: tuple) -> str:
    rgb = tuple(round(x*255.) for x in rgb)
    return "#%02x%02x%02x" % rgb

def hex2rgb(hex: str) -> tuple:
    c = hex.strip("#")
    rgb = [int(x, 16) for x in (c[:2], c[2:4], c[4:])]
    return tuple(x/255. for x in rgb)

def rgb2hsv(rgb: tuple) -> tuple:
    h, s, v = colorsys.rgb_to_hsv(*rgb)
    return h*360., s*100., v*100.

def rgb2hsl(rgb: tuple) -> tuple:
    h, l, s = colorsys.rgb_to_hls(*rgb)
    return h*360., s*100., l*100.

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("HSV Model & HSL Model")
        self.default_bg = self.master["background"]

        frame_north = tk.Frame(self.master)
        frame_south = tk.Frame(self.master)
        frame_north.pack(padx=4, pady=4)
        frame_south.pack(padx=4, pady=4)

        frame_north_west = tk.Frame(frame_north)
        frame_north_east = tk.Frame(frame_north)
        frame_north_west.pack(side=tk.LEFT)
        frame_north_east.pack()

        frm_rb = tk.Frame(frame_north_west)
        frm_entry = tk.Frame(frame_north_west)
        frm_canvas = tk.Frame(frame_north_west)
        frm_rb.pack(anchor=tk.W)
        frm_entry.pack(anchor=tk.W)
        frm_canvas.pack(anchor=tk.W)

        self.var_rb = tk.IntVar()
        self.var_rb.set(0)
        rb_hsv = tk.Radiobutton(frm_rb, value=0, variable=self.var_rb, text="HSV", command=self.select_hsv)
        rb_hsv.pack(side=tk.LEFT, padx=2)
        rb_hsl = tk.Radiobutton(frm_rb, value=1, variable=self.var_rb, text="HSL", command=self.select_hsl)
        rb_hsl.pack(padx=4)

        lbl = tk.Label(frm_entry, text="Hex")
        lbl.pack(side=tk.LEFT, padx=2, pady=4)
        self.entry = tk.Entry(frm_entry, width=10)
        self.entry.pack(side=tk.LEFT, padx=2)
        btn = tk.Button(frm_entry, text="submit", command=self.check_color)
        btn.pack(padx=2)
        self.cel = tk.Canvas(frm_canvas, bg=self.default_bg, width=37, height=37)
        self.cel.pack(side=tk.LEFT, padx=4)
        self.cvs = tk.Canvas(frm_canvas, width=128, height=37)
        self.cvs.pack()

        self.draw_hue(frame_north_east)
        self.var_hue = tk.IntVar(value=0)
        self.scale_widget(frame_north_east)

        self.draw_matrix(frame_south, 0)
        tk.Frame(frame_south, height=8).pack() # 下の余白

    def select_hsv(self):
        self.lightness.delete("all")
        self.lightness.create_text(25, 15, text="Value")
        self.scale.config(variable=tk.IntVar(value=0))
        self.change_matrix(hue=0)

    def select_hsl(self):
        self.lightness.delete("all")
        self.lightness.create_text(30, 15, text="Lightness")
        self.scale.config(variable=tk.IntVar(value=0))
        self.change_matrix(hue=0)

    def select_func(self):
        is_hsl = self.var_rb.get()
        if is_hsl:
            func = lambda x: hsl2rgb(x)
        else:
            func = lambda x: hsv2rgb(x)
        
        return func

    def check_color(self):
        self.cvs.delete("all")
        hexcode = self.entry.get()
        if re.fullmatch(r"[0-9|a-f|A-F]{6}", hexcode[1:]) and hexcode.startswith("#"):
            self.cel.config(bg=hexcode)
            rgb = hex2rgb(hexcode)
            hsv = rgb2hsv(rgb)
            hsl = rgb2hsl(rgb)
            hue_int = round(hsv[0])
            self.cvs.create_text(
                4, 
                7, 
                anchor=tk.NW,
                text=f"HSV: {round(hsv[0],2)}, {round(hsv[1],2)}, {round(hsv[2],2)}"
                )
            self.cvs.create_text(
                4, 
                21, 
                anchor=tk.NW,
                text=f"HSL: {round(hsl[0],2)}, {round(hsl[1],2)}, {round(hsl[2],2)}"
                )
            self.scale.config(variable=tk.IntVar(value=hue_int))
            self.change_matrix(hue_int)
            if self.var_rb.get():
                x, sat = hsl[2], hsl[1]
            else:
                x, sat = hsv[2], hsv[1]
            self.mark_matrix(int(x/10), int(sat/10))
        else:
            self.cvs.create_text(
                4, 
                7, 
                anchor=tk.NW,
                text="example -> #5F9EA0",
            )
            self.cel.config(bg=self.default_bg)


    def draw_hue(self, frame):
        tk.Label(frame, text="hue").pack()
        hue_canvas = tk.Canvas(frame, width=360, height=47)
        hue_canvas.pack(padx=4)
        for i in range(360):
            hsv = i, 100., 100.
            rgb = hsv2rgb(hsv)
            hue_canvas.create_line(i, 0, i, 47, width=1, fill=rgb2hex(rgb))

    def draw_matrix(self, frame, hue):
        frm = tk.Frame(frame)
        frm.pack(padx=4)
        lbl = tk.Label(frm, text="Saturation")
        lbl.pack()
        self.lightness = tk.Canvas(frm, width=60, height=20)
        self.lightness.create_text(25, 15, text="Value")
        self.lightness.pack(padx=3, side=tk.LEFT)

        for i in range(11):
            xlim = tk.Canvas(frm, width=37, height=20)
            xlim.create_text(13, 11, text=f"{i*10}%")
            xlim.pack(padx=3, side=tk.LEFT)

        self.color_matrix = [[] for _ in range(11)]
        for i in range(11):
            val = i*10
            frm = tk.Frame(frame)
            frm.pack()
            ylim = tk.Canvas(frm, width=37, height=37)
            ylim.create_text(20, 20, text=f"{i*10}%")
            ylim.pack(padx=3, pady=3, side=tk.LEFT)
            for j in range(11):
                sat = j*10
                hsv = hue, sat, val
                rgb = hsv2rgb(hsv)
                canvas = tk.Canvas(frm, width=37, height=37, bg=rgb2hex(rgb))
                canvas.pack(padx=3, pady=3, side=tk.LEFT)
                self.color_matrix[i].append(canvas)

    def scale_widget(self, flame):
        self.scale = tk.Scale(flame, 
                    variable = self.var_hue, 
                    command = self.callback,
                    orient=tk.HORIZONTAL, 
                    length = 360,
                    width = 12,
                    sliderlength = 10,    # スライダー（つまみ）の幅
                    from_ = 0,
                    to = 360,
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=100      # 目盛りの分解能(初期値0で表示なし)
                    )
        self.scale.pack()
    
    def callback(self, event=None):
        func = self.select_func()
        self.scale.config(variable=self.var_hue)
        hue = self.var_hue.get()
        for i in range(11):
            for j in range(11):
                hsv = hue, j*10, i*10
                rgb = func(hsv)
                self.color_matrix[i][j].delete("mark")
                self.color_matrix[i][j].config(bg=rgb2hex(rgb))
        
    def change_matrix(self, hue):
        func = self.select_func()
        for i in range(11):
            for j in range(11):
                hsv = hue, j*10, i*10
                rgb = func(hsv)
                self.color_matrix[i][j].delete("mark")
                self.color_matrix[i][j].config(bg=rgb2hex(rgb))

    def mark_matrix(self, i, j):
        this_color = self.color_matrix[i][j].cget("bg")
        self.color_matrix[i][j].config(bg="black")
        self.color_matrix[i][j].create_rectangle(4, 4, 36, 36, fill=this_color, outline="white", tag="mark")


if __name__ == "__main__":

    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()
