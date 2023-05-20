import colour
import numpy as np
from numpy.typing import ArrayLike
from skimage import color
import tkinter as tk
import tkinter.ttk as ttk
import re 

import warnings
# warnings.simplefilter('ignore')
warnings.simplefilter('error')

# def lch2rgb(lch: ArrayLike) -> np.ndarray:
#     lab = colour.LCHab_to_Lab(lch)
#     xyz = colour.Lab_to_XYZ(lab)
#     srgb = colour.XYZ_to_sRGB(xyz)
#     return srgb

def rgb2hex(srgb: ArrayLike) -> str:
    rgb = tuple(round(x*255.) for x in srgb)
    return "#%02x%02x%02x" % rgb

def hex2rgb(hex: str) -> tuple:
    c = hex.strip("#")
    rgb = [int(x, 16) for x in (c[:2], c[2:4], c[4:])]
    return tuple(x/255. for x in rgb)

def lch2rgb(lch: ArrayLike):
    # lab = color.lch2lab(lch)
    lab = LCH_to_LAB(lch)
    rgb = color.lab2rgb(lab)
    return rgb

def rgb2lch(rgb: ArrayLike):
    lab = color.rgb2lab(rgb)
    lch = LAB_to_LCH(lab)
    return lch

def LCH_to_LAB(lch: ArrayLike) -> np.ndarray:
    l, c, h = lch
    rad = h * np.pi / 180.
    a = c*np.cos(rad)
    b = c*np.sin(rad)
    return np.array([l, a, b]) #, dtype=np.float64)

def LAB_to_LCH(lab: ArrayLike) -> np.ndarray:
    # https://github.com/ytyaru/Python.ColorSpace.Converter.20210606081641/tree/master/src
    l, a, b = lab
    c = np.sqrt(a**2 + b**2)
    h = (np.arctan2(b, a) * (180 / np.pi) + 360) % 360
    return np.array([l, c, h])


func = np.vectorize(lambda x: 0. <= x <= 1.)

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("LCH Model")
        self.primary = "#FDFDFD" # < gray 50
        self.secondary = "#F5F5F5" # gray 100
        self.alert = "#EF5350" # red 400
        self.master.tk_setPalette(background=self.primary)
        # self.master["background"] = self.alert

        style = ttk.Style()
        style.theme_use('classic')
        style.configure('c.TButton', borderwidth=0, padding=[2], background=self.secondary)

        frame_N = tk.Frame(self.master, bg=self.primary)
        frame_S = tk.Frame(self.master)
        frame_N.pack(padx=8, pady=8, anchor=tk.W)
        frame_S.pack(padx=8, pady=8)
        frame_N_West = tk.Frame(frame_N, bg=self.primary)
        frame_N_Center = tk.Frame(frame_N, padx=8)
        frame_N_East = tk.Frame(frame_N)
        frame_N_West.pack(side=tk.LEFT)
        frame_N_Center.pack(side=tk.LEFT)
        frame_N_East.pack()

        self.create_16entry(frame_N_West)

        self.hue_canvas(frame_N_Center)
        self.var = tk.IntVar(value=0)
        self.scale_widget(frame_N_Center)

        self.create_2colors(frame_N_East)

        self.canvas_draw(frame_S, 0)

    def create_16entry(self, frame):
        frm_entry = tk.Frame(frame)
        frm_canvas = tk.Frame(frame)
        frm_entry.pack(anchor=tk.W, padx=8)
        frm_canvas.pack(anchor=tk.W)
        lbl = tk.Label(frm_entry, text="Hex")
        lbl.pack(side=tk.LEFT, padx=2, pady=4, anchor=tk.W)
        self.entry = tk.Entry(frm_entry, width=10, bg="#FFF")
        self.entry.pack(side=tk.LEFT, padx=2)
        btn = ttk.Button(
            frm_entry, 
            text="submit", 
            style="c.TButton", 
            command=self.color_entry
            )
        btn.pack(padx=2)
        self.canvas_2lch = tk.Canvas(frm_canvas, width=47, height=47, bg=self.secondary)
        self.canvas_2lch.pack(side=tk.LEFT, padx=4)
        self.lbl_2lch = tk.Label(frm_canvas, text="")
        self.lbl_2lch.pack(side=tk.LEFT)

    def color_entry(self):
        # Hex submit押した
        self.lbl_2lch.config(text="")
        hexrgb = self.entry.get()
        if re.fullmatch(r"[0-9|a-f|A-F]{6}", hexrgb[1:]) and hexrgb.startswith("#"):
            self.canvas_2lch.config(bg=hexrgb)
            rgb = hex2rgb(hexrgb)
            lch = rgb2lch(rgb)
            hue_int = round(lch[2])
            self.lbl_2lch.config(
                text=f"{round(lch[0],2)}, {round(lch[1],2)}, {round(lch[2],2)}",
                fg="#000"
            )
            self.var.set(value=hue_int)
            self.change_matrix(hue_int)
            i, j = lch[0], lch[1]
            self.mark_matrix(int(i/10), int(j/10))
        else:
            self.lbl_2lch.config(text="example: #5F9EA0", fg=self.alert)
            self.canvas_2lch.config(bg=self.secondary)

    def create_2colors(self, frame):
        frm = tk.Frame(frame)
        tk.Label(frm, text="Lch").pack(side=tk.LEFT, padx=2)
        self.entry1 = tk.Entry(frm, width=16)
        self.entry1.pack(side=tk.LEFT, padx=2)
        ttk.Button(frm, text="→", style="c.TButton", command=self.left_color).pack(side=tk.LEFT)
        tk.Label(frm, text="Hex").pack(side=tk.LEFT, padx=2)
        self.label1 = tk.Label(frm, text="", anchor=tk.W, width=12)
        self.label1.pack(side=tk.LEFT)
        frm.pack(anchor=tk.W, padx=8, pady=8)

        frm = tk.Frame(frame)
        tk.Label(frm, text="Lch").pack(side=tk.LEFT, padx=2)
        self.entry2 = tk.Entry(frm, width=16)
        self.entry2.pack(side=tk.LEFT, padx=2)
        ttk.Button(frm, text="→", style="c.TButton", command=self.right_color).pack(side=tk.LEFT)
        tk.Label(frm, text="Hex").pack(side=tk.LEFT, padx=2)
        self.label2 = tk.Label(frm, text="", anchor=tk.W, width=12)
        self.label2.pack(side=tk.LEFT)
        frm.pack(anchor=tk.W, padx=8, pady=8)

        frm = tk.Frame(frame)
        tk.Label(frm, width=4).pack(side=tk.LEFT, anchor=tk.W)
        self.canvas2colors = tk.Canvas(frm, width=94, height=47, bg=self.secondary)
        self.canvas2colors.pack(side=tk.LEFT, anchor=tk.W)
        frm.pack(anchor=tk.W)


    def left_color(self, event=None):
        s = self.entry1.get()
        lch = [float(x) for x in s.split(",")]
        rgb = lch2rgb(lch)
        hexrgb = rgb2hex(rgb)
        self.label1.config(text=hexrgb)
        self.canvas2colors.create_rectangle(0, 0, 47, 47, outline=hexrgb, fill=hexrgb)

    def right_color(self, event=None):
        s = self.entry2.get()
        lch = [float(x) for x in s.split(",")]
        rgb = lch2rgb(lch)
        hexrgb = rgb2hex(rgb)
        self.label2.config(text=hexrgb)
        self.canvas2colors.create_rectangle(47, 0, 94, 47, outline=hexrgb, fill=hexrgb)

        # color.deltaE_ciede2000(lab1, lab2) # 色差


    def hue_canvas(self, frame):
        tk.Label(frame, text="Hue: L=60, c=60").pack()
        canvas = tk.Canvas(frame, width=360, height=47)
        canvas.pack()
        x = 0
        for i in range(360):
            lch = 60., 60., i
            rgb = lch2rgb(lch)
            canvas.create_line(i, 0, i, 64, width=1, fill=rgb2hex(rgb))

    def canvas_draw(self, frame, hue):
        frm = tk.Frame(frame)
        frm.pack()
        lbl = tk.Label(frm, text="Chroma")
        lbl.pack()
        c = tk.Canvas(frm, width=60, height=20)
        c.create_text(32, 14, text="Lightness")
        c.pack(padx=3, side=tk.LEFT)
        for i in range(15):
            canvas = tk.Canvas(frm, width=37, height=20)
            canvas.create_text(20, 12, text=f"{i*10}")
            canvas.pack(padx=3, side=tk.LEFT)

        self.color_matrix = [[] for _ in range(11)]
        for i in range(11):
            val = i*10
            frm = tk.Frame(frame)
            frm.pack()
            cc = tk.Canvas(frm, width=58, height=37)
            cc.create_text(40, 20, text=f"{i*10}")
            cc.pack(padx=3, pady=3, side=tk.LEFT)
            for j in range(15):
                sat = j*10
                lch = val, sat, hue
                try:
                    rgb = lch2rgb(lch)
                    bg_color = rgb2hex(rgb)
                except (TypeError, UserWarning) as e:
                    print(e)
                    bg_color = self.secondary
                canvas = tk.Canvas(frm, width=37, height=37, bg=bg_color)
                canvas.pack(padx=3, pady=3, side=tk.LEFT)
                self.color_matrix[i].append(canvas)

    def scale_widget(self, flame):
        self.scale = tk.Scale(flame, 
                    variable = self.var, 
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
        hue = self.var.get()
        for i in range(11):
            for j in range(15):
                lch = i*10, j*10, hue
                try:
                    rgb = lch2rgb(lch)
                    bg_color = rgb2hex(rgb)
                except (TypeError, UserWarning, DeprecationWarning) as e:
                    # print(e)
                    bg_color = self.secondary
                self.color_matrix[i][j].delete("all")
                self.color_matrix[i][j].config(bg=bg_color)

    def change_matrix(self, hue):
        for i in range(11):
            for j in range(15):
                lch = i*10, j*10, hue
                try:
                    rgb = lch2rgb(lch)
                    self.color_matrix[i][j].delete("all")
                    self.color_matrix[i][j].config(bg=rgb2hex(rgb))
                except:
                    self.color_matrix[i][j].config(bg=self.secondary)

    def mark_matrix(self, i, j):
        this_color = self.color_matrix[i][j].cget("bg")
        self.color_matrix[i][j].config(bg="black")
        self.color_matrix[i][j].create_rectangle(4, 4, 36, 36, fill=this_color, outline="white", tag="mark")


if __name__ == "__main__":
    
    # lch = 60., 30., 18.
    # print(lch2rgb(lch))

    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()

    # https://github.com/scikit-image/scikit-image/blob/main/skimage/color/colorconv.py

