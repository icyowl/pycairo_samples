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

def hex2hsv(hex: str) -> tuple:
    hx = hex.strip("#")
    rgb = [int(x, 16) for x in (hx[:2], hx[2:4], hx[4:])]
    rgb = [x/255. for x in rgb]
    h, s, v = colorsys.rgb_to_hsv(*rgb)

    return h*360., s*100., v*100.

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("HSV & HSL Model")

        frame_north = tk.Frame(self.master)
        frame_south = tk.Frame(self.master)
        frame_north.pack(padx=4, pady=4)
        frame_south.pack(padx=4, pady=4)

        frame_north_west = tk.Frame(frame_north)
        frame_north_east = tk.Frame(frame_north)
        frame_north_west.pack(side=tk.LEFT)
        frame_north_east.pack()

        frm_entry = tk.Frame(frame_north_west)
        frm_canvas = tk.Frame(frame_north_west)
        frm_entry.pack()
        frm_canvas.pack()
        lbl = tk.Label(frm_entry, text="Hex")
        lbl.pack(side=tk.LEFT)
        self.entry = tk.Entry(frm_entry, width=8)
        self.entry.pack(side=tk.LEFT)
        btn = tk.Button(frm_entry, text="submit", width=4, command=self.check_color)
        btn.pack()
        self.cvs = tk.Canvas(frm_canvas, width=180, height=50, bg="gray")
        self.cvs.pack()

        self.hue_canvas(frame_north_east)
        self.var = tk.IntVar(value=0)
        self.scale_widget(frame_north_east)

        self.canvas_draw(frame_south, 0)

    def check_color(self):
        self.cvs.delete("message")
        hc = self.entry.get()
        h, s, v = hex2hsv(hc)
        hue_int = round(h)
        self.cvs.create_text(
            100, 
            20, 
            text=f"{round(h,2)},{round(s,2)}, {round(v,2)}", 
            tag="message"
            )
        self.scale.config(variable=tk.IntVar(value=hue_int))
        self.change_matrix(hue_int)
        self.mark_matrix(int(v/10), int(s/10))


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
        self.scale.config(variable=self.var)
        hue = self.var.get()
        for i in range(11):
            for j in range(11):
                hsv = hue, j*10, i*10
                rgb = hsv2rgb(hsv)
                self.color_matrix[i][j].delete("mark")
                self.color_matrix[i][j].config(bg=rgb2hex(rgb))
        
    def change_matrix(self, hue):
        for i in range(11):
            for j in range(11):
                hsv = hue, j*10, i*10
                rgb = hsv2rgb(hsv)
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