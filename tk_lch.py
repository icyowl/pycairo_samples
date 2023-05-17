import colour
import numpy as np
from numpy.typing import ArrayLike
from skimage import color
import tkinter as tk


def lch2rgb(lch: ArrayLike) -> np.ndarray:
    lab = colour.LCHab_to_Lab(lch)
    xyz = colour.Lab_to_XYZ(lab)
    srgb = colour.XYZ_to_sRGB(xyz)
    return srgb

def rgb2hex(srgb: ArrayLike) -> str:
    rgb = tuple(round(x*255.) for x in srgb)
    return "#%02x%02x%02x" % rgb


def lch2rgb(lch: ArrayLike):
    lab = color.lch2lab(lch)
    # print("lab", lab)
    lab = LCH_to_LAB(lch)
    xyz = color.lab2xyz(lab)
    rgb = color.xyz2rgb(xyz)
    return rgb


def LCH_to_LAB(lch: ArrayLike) -> np.ndarray:
    l, c, h = lch
    rad = h * np.pi / 180.
    a = c*np.cos(rad)
    b = c*np.sin(rad)

    return np.array([l, a, b]) #, dtype=np.float64)




func = np.vectorize(lambda x: 0. <= x <= 1.)

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("LCH Model")
        self.backgroundcolor = self.master["background"]

        frame_c = tk.Frame(self.master)
        frame_c.pack()
        self.hue_canvas(frame_c)

        frame_u = tk.Frame(self.master)
        frame_u.pack()
        self.var = tk.IntVar(value=0)
        self.scale_widget(frame_u)

        self.frame_d = tk.Frame(self.master)
        self.frame_d.pack(padx=10, pady=10)
        self.canvas_draw(self.frame_d, 0)

    def hue_canvas(self, frame):
        canvas = tk.Canvas(frame, width=360, height=47)
        canvas.pack()
        x = 0
        for i in range(360):
            lch = 60., 30., i
            rgb = lch2rgb(lch)
            if func(rgb).sum() == 3:
                color = rgb2hex(rgb)
            else:
                color = None
            canvas.create_line(x, 0, x, 64, width=1, fill=color)
            x += 1

    def canvas_draw(self, frame, hue):
        frm = tk.Frame(frame)
        frm.pack()
        lbl = tk.Label(frm, text="Saturation")
        lbl.pack()
        c = tk.Canvas(frm, width=37, height=20)
        c.create_text(20, 14, text="Value")
        c.pack(padx=3, side=tk.LEFT)
        for i in range(11):
            canvas = tk.Canvas(frm, width=37, height=20)
            canvas.create_text(20, 12, text=f"{i*10}%")
            canvas.pack(padx=3, side=tk.LEFT)

        self.color_matrix = [[] for _ in range(11)]
        for i in range(11):
            val = i*10
            text = "V=" + str(val).rjust(3, " ") + "%"
            frm = tk.Frame(frame)
            frm.pack()
            cc = tk.Canvas(frm, width=37, height=37)
            cc.create_text(20, 20, text=f"{i*10}%")
            cc.pack(padx=3, pady=3, side=tk.LEFT)
            for j in range(11):
                sat = j*10
                lch = val, sat, hue
                rgb = lch2rgb(lch)
                if func(rgb).sum() == 3:
                    color = rgb2hex(rgb)
                else:
                    color = self.backgroundcolor

                canvas = tk.Canvas(frm, width=37, height=37, bg=color)
                canvas.pack(padx=3, pady=3, side=tk.LEFT)
                self.color_matrix[i].append(canvas)

    def scale_widget(self, flame):
        scale = tk.Scale(flame, 
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
        scale.pack()
    
    def callback(self, event=None):
        hue = self.var.get()
        for i in range(11):
            for j in range(11):
                lch = i*10, j*10, hue
                rgb = lch2rgb(lch)
                if func(rgb).sum() == 3:
                    color = rgb2hex(rgb)
                else:
                    color = self.backgroundcolor
                self.color_matrix[i][j].config(bg=color)


if __name__ == "__main__":
    
    # lch = 60., 30., 18.
    # print(lch2rgb(lch))

    # https://github.com/scikit-image/scikit-image/issues/4506

    # https://github.com/scikit-image/scikit-image/blob/main/skimage/color/colorconv.py

    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()