import colorsys
import numpy as np
import os
from PIL import ImageColor, Image
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x250")
        self.title("DnD")

        self.label = frameDnD(self)
        self.label.pack()

        self.textbox = tk.Text(self, height=8)
        self.textbox.configure(state='normal')
        self.textbox.pack()


class frameDnD(tk.Label):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.dropbox = tk.Text(self, height=12)
        self.dropbox.insert(tk.END, "Drop here!")
        self.dropbox.configure(state='disabled')
        self.dropbox.drop_target_register(DND_FILES)
        self.dropbox.dnd_bind("<<Drop>>", self.func)
        self.dropbox.pack()

    def func(self, e):
        # print(e.data)
        self.parent.textbox.delete('1.0', tk.END)
        
        message = os.path.basename(e.data)
        self.parent.textbox.insert(tk.END, message)
        # self.textbox.configure(state='disabled')
        # self.textbox.see(tk.END)

        p = e.data.strip("{").strip("}")
        im = Image.open(p)
        a = np.array(im)
        w, h, c = a.shape
        arr = a.reshape(w*h, c)

        rgb = [int(np.mean(a)) for a in arr.T]
        self.parent.textbox.insert(tk.END, "\n" + " ".join(str(c) for c in rgb))

        color = "#%02x%02x%02x" % tuple(rgb[:3])
        self.parent.textbox.insert(tk.END, "\n" + color)
        self.dropbox.configure(bg=color)


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