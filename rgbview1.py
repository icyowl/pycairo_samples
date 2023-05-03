import tkinter as tk

class Red(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("RGB Demo")

        frame = tk.Frame(self.master)
        frame.pack()

        label = tk.Label(frame, text="R")
        label.pack(side=tk.LEFT, padx=8)
        
        self.canvas = tk.Canvas(frame, width=80, height=40)
        self.rect = self.canvas.create_rectangle(0, 0, 80, 40, fill=self.rgbToHex((0, 0, 0)))
        self.canvas.pack(side=tk.LEFT)

        self.scale_var = tk.IntVar()
        self.scale_pack(frame, self.scale_var, self.callback)

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

    def callback(self, event=None):
        r = self.scale_var.get()
        self.canvas.itemconfigure(self.rect, fill=self.rgbToHex((r, 0, 0)))



if __name__ == "__main__":

    root = tk.Tk()
    app = Red(master=root)
    app.mainloop()