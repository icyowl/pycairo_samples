import tkinter as tk

class RGBdemo(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("RGB Demo")

        # RGB
        frame = tk.Frame(self.master)
        frame.pack()
        self.canvas_rgb = tk.Canvas(frame, width=320, height=40)
        self.rect_rgb = self.canvas_rgb.create_rectangle(0, 0, 320, 40, fill=self.rgbToHex((0, 0, 0)))
        self.canvas_rgb.pack(pady=16)

        # Red
        frame = tk.Frame(self.master)
        frame.pack()

        label = tk.Label(frame, text="R")
        label.pack(side=tk.LEFT, padx=8)
        
        self.canvas_r = tk.Canvas(frame, width=80, height=40)
        self.rect_r = self.canvas_r.create_rectangle(0, 0, 80, 40, fill=self.rgbToHex((0, 0, 0)))
        self.canvas_r.pack(side=tk.LEFT)

        self.scale_r_var = tk.IntVar()
        self.scale_pack(frame, self.scale_r_var, self.callback_r)

        # Green
        frame = tk.Frame(self.master)
        frame.pack()

        label = tk.Label(frame, text="G")
        label.pack(side=tk.LEFT, padx=8)
        
        self.canvas_g = tk.Canvas(frame, width=80, height=40)
        self.rect_g = self.canvas_g.create_rectangle(0, 0, 80, 40, fill=self.rgbToHex((0, 0, 0)))
        self.canvas_g.pack(side=tk.LEFT)

        self.scale_g_var = tk.IntVar()
        self.scale_pack(frame, self.scale_g_var, self.callback_g)

        # Blue
        frame = tk.Frame(self.master)
        frame.pack()

        label = tk.Label(frame, text="B")
        label.pack(side=tk.LEFT, padx=8)
        
        self.canvas_b = tk.Canvas(frame, width=80, height=40)
        self.rect_b = self.canvas_b.create_rectangle(0, 0, 80, 40, fill=self.rgbToHex((0, 0, 0)))
        self.canvas_b.pack(side=tk.LEFT)

        self.scale_b_var = tk.IntVar()
        self.scale_pack(frame, self.scale_b_var, self.callback_b)

    def scale_pack(self, frame, var, callback):
        tk.Scale(frame, 
                variable = var, 
                command = callback,
                orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                length = 256,           # 全体の長さ
                width = 20,             # 全体の太さ
                sliderlength = 10,      # スライダー（つまみ）の幅
                from_ = 0,            # 最小値（開始の値）
                to = 255,               # 最大値（終了の値）
                resolution=1,         # 変化の分解能(初期値:1)
                tickinterval=100         # 目盛りの分解能(初期値0で表示なし)
                ).pack(padx=8)

    @staticmethod
    def rgbToHex(rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb   

    def callback_r(self, event=None):
        r = self.scale_r_var.get()
        self.canvas_r.itemconfigure(self.rect_r, fill=self.rgbToHex((r, 0, 0)))
        g, b = self.scale_g_var.get(), self.scale_b_var.get()
        self.canvas_rgb.itemconfigure(self.rect_rgb, fill=self.rgbToHex((r, g, b)))

    def callback_g(self, event=None):
        g = self.scale_g_var.get()
        self.canvas_g.itemconfigure(self.rect_g, fill=self.rgbToHex((0, g, 0)))
        r, b = self.scale_r_var.get(), self.scale_b_var.get()
        self.canvas_rgb.itemconfigure(self.rect_rgb, fill=self.rgbToHex((r, g, b)))

    def callback_b(self, event=None):
        b = self.scale_b_var.get()
        self.canvas_b.itemconfigure(self.rect_b, fill=self.rgbToHex((0, 0, b)))
        r, g = self.scale_r_var.get(), self.scale_g_var.get()
        self.canvas_rgb.itemconfigure(self.rect_rgb, fill=self.rgbToHex((r, g, b)))



if __name__ == "__main__":

    root = tk.Tk()
    app = RGBdemo(master=root)
    app.mainloop()