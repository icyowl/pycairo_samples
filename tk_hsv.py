import colorsys
import tkinter as tk
from mycolorsys import hsv_to_rgb


class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("HSV Demo")

        frame_c = tk.Frame(self.master)
        frame_c.pack(pady=10)
        self.hue_canvas(frame_c)

        frame_u = tk.Frame(self.master)
        frame_u.pack(pady=5)
        self.var = tk.IntVar(value=0)
        self.scale_widget(frame_u)

        self.frame_d = tk.Frame(self.master)
        self.frame_d.pack(padx=10, pady=10)
        self.canvas_draw(self.frame_d, 0)

    def hue_canvas(self, frame):
        canvas = tk.Canvas(frame, width=540, height=64)
        canvas.pack()
        x = 0
        for i in range(360):
            rgb = colorsys.hsv_to_rgb(i/360, 1.0, 0.5)
            rgb = tuple(int(x*255) for x in rgb)
            hrgb = "#%02x%02x%02x" % rgb
            canvas.create_line(x, 0, x, 64, width=1.5, fill=hrgb)
            x += 1.5


    def canvas_draw(self, frame, hue):
        frm = tk.Frame(frame)
        frm.pack()
        tk.Label(frm, text="Sat =", width=5).pack(side=tk.LEFT)
        for i in range(11):
            canvas = tk.Canvas(frm, width=50, height=20)
            canvas.create_text(28, 14, text=f"{i*10}%")
            canvas.pack(padx=3, pady=3, side=tk.LEFT)

        self.color_matrix = [[] for _ in range(11)]
        for i in range(11):
            val = i*10
            text = "V=" + str(val).rjust(3, " ") + "%"
            frm = tk.Frame(frame)
            frm.pack()
            label = tk.Label(frm, text=text)
            label.pack(side=tk.LEFT)
            for j in range(11):
                sat = j*10
                r, g, b = hsv_to_rgb(hue, sat, val)
                canvas = tk.Canvas(frm, width=50, height=50, bg=self.rgb2hex((r, g, b)))
                canvas.pack(padx=3, pady=3, side=tk.LEFT)
                self.color_matrix[i].append(canvas)

    def scale_widget(self, flame):
        scale = tk.Scale(flame, 
                    variable = self.var, 
                    command = self.callback,
                    orient=tk.HORIZONTAL, 
                    length = 540,
                    width = 20,
                    sliderlength = 10,    # スライダー（つまみ）の幅
                    from_ = 0,
                    to = 360,
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=100      # 目盛りの分解能(初期値0で表示なし)
                    )
        scale.pack()
    
    @staticmethod
    def rgb2hex(rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb   

    def callback(self, event=None):
        hue = self.var.get()
        for i in range(11):
            for j in range(11):
                r, g, b = hsv_to_rgb(hue, j*10, i*10)
                self.color_matrix[i][j].config(bg=self.rgb2hex((r, g, b)))


if __name__ == "__main__":

    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()