import colorsys
import numpy as np
from PIL import ImageColor, Image
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x200")
        self.title("DnD")

        self.label = frameDnD(self)
        self.label.pack()

class frameDnD(tk.Label):
    def __init__(self, parent):
        super().__init__(parent)
        self.textbox = tk.Text(self)
        # self.textbox.insert(0.0, "DnD, Hear")
        self.textbox.configure(state='disabled')

        ## ドラッグアンドドロップ
        self.textbox.drop_target_register(DND_FILES)
        self.textbox.dnd_bind("<<Drop>>", self.func)
        self.textbox.pack()

    def func(self, e):
        ## ここを編集してください
        print(e.data)
        message = '\n' + e.data
        # self.textbox.configure(state='normal')
        # self.textbox.insert(tk.END, message)
        # self.textbox.configure(state='disabled')
        # self.textbox.see(tk.END)

        p = e.data.strip("{").strip("}")
        im = Image.open(p)
        a = np.array(im)
        w, h, c = a.shape
        arr = a.reshape(w*h, c)
        rgb = [int(np.mean(a)) for a in arr.T]
        print(rgb)
        xrgb = "#%02x%02x%02x" % tuple(rgb[:3])
        print(xrgb)
        self.textbox.configure(bg=xrgb)


# hex_code = '#169bbd'
# rgb = ImageColor.getcolor(hex_code, "RGB")

# hls = colorsys.rgb_to_hls(*rgb)

# # print(hls)

# im = Image.open('./jaromir-kalina3.jpg')
# arr_im = np.array(im)
# w, h, c = arr_im.shape
# arr = arr_im.reshape(w*h, c)
# rgb = [int(np.mean(a)) for a in arr.T]
# print(rgb)

# hex_l = [format(c, 'x').zfill(2) for c in rgb]

# hex_code = "#" + "".join(hex_l)
# print(hex_code)

if __name__ == "__main__":
    app = App()
    app.mainloop()