import cairosvg
# o conda install -c "conda-forge/label/cf202003" cairosvg
# x conda install -c conda-forge cairosvg
# x pip install cairosvg
# cairosvgと依存libffiのバージョン違い
import io
import os
from PIL import Image, ImageTk
import tkinter as tk


def foo():
    root = tk.Tk()

    files = [f for f in os.listdir("./") if f[-4:] == ".svg"]
    file = files[0]
    file = "./tree1.svg"
    with open(file, "rb") as f:
        buf = f.read()
        buf = cairosvg.svg2png(bytestring=buf)
        buf = Image.open(io.BytesIO(buf))
        img = ImageTk.PhotoImage(image=buf)

    tk.Label(root, image=img).pack()
    root.mainloop()


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("SVGs Viewer")
        
        upper, lower = tk.Frame(self.master), tk.Frame(self.master)
        upper.pack()
        lower.pack()
        self.frames = [tk.Frame(upper).pack(side=tk.LEFT) for _ in range(3)]
        self.frames += [tk.Frame(lower).pack(side=tk.LEFT) for _ in range(3)]

        self.view(self.frames[0])

    def view(self, frame):
        file = "./tree1.svg"
        with open(file, "rb") as f:
            buf = f.read()
            buf = cairosvg.svg2png(bytestring=buf)
            buf = Image.open(io.BytesIO(buf))
            img = ImageTk.PhotoImage(image=buf)
        lbl = tk.Label(frame, image=img)
        lbl.image = img
        lbl.pack()


if __name__ == "__main__":

    root = tk.Tk()
    app = App(master=root)
    app.mainloop()

