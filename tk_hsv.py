import colorsys
import tkinter as tk

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

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("HSV Model")

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
            hsv = i, 100., 50.
            rgb = hsv2rgb(hsv)
            canvas.create_line(x, 0, x, 64, width=1, fill=rgb2hex(rgb))
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
                hsv = hue, sat, val
                rgb = hsv2rgb(hsv)
                canvas = tk.Canvas(frm, width=37, height=37, bg=rgb2hex(rgb))
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
                hsv = hue, j*10, i*10
                rgb = hsv2rgb(hsv)
                self.color_matrix[i][j].config(bg=rgb2hex(rgb))


if __name__ == "__main__":

    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()