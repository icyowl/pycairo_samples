import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("RGB Demo")     # ウィンドウタイトル

        self.canvasR = tk.Canvas(self.master, width=80, height=40)
        self.varR = tk.IntVar(value=0)
        r = self.varR.get()
        self.rect_r = self.canvasR.create_rectangle(0, 0, 80, 40, fill=self.rgbToHex((r, 0, 0)))
        self.canvasR.pack(anchor=tk.W, side=tk.LEFT)

        self.scale_var = tk.IntVar()
        scaleH = tk.Scale( self.master, 
                    variable = self.scale_var, 
                    command = self.slider_scroll,
                    orient=tk.HORIZONTAL,   # 配置の向き、水平(HORIZONTAL)、垂直(VERTICAL)
                    length = 256,           # 全体の長さ
                    width = 20,             # 全体の太さ
                    sliderlength = 10,      # スライダー（つまみ）の幅
                    from_ = 0,            # 最小値（開始の値）
                    to = 255,               # 最大値（終了の値）
                    resolution=1,         # 変化の分解能(初期値:1)
                    tickinterval=100         # 目盛りの分解能(初期値0で表示なし)
                    )
        scaleH.pack(side=tk.LEFT)
    
    @staticmethod
    def rgbToHex(rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb   

    def slider_scroll(self, event=None):
        '''スライダーを移動したとき'''
        # print(str(self.scale_var.get()))
        r = self.scale_var.get()
        # print(r)
        self.canvasR.itemconfigure(self.rect_r, fill=self.rgbToHex((r, 0, 0)))

if __name__ == "__main__":

    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()