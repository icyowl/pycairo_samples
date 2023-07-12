import cairosvg
# o conda install -c "conda-forge/label/cf202003" cairosvg
# x conda install -c conda-forge cairosvg
# x pip install cairosvg
# cairosvgと依存libffiのバージョン違い
import io
import os
from PIL import Image, ImageTk
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("SVG Viewer")
        
        upper, lower = tk.Frame(self.master), tk.Frame(self.master)
        upper.pack(padx=2)
        lower.pack(padx=2, anchor=tk.W)
        frames = []
        for i in range(6):
            if i < 3:
                frames.append(tk.Frame(upper))
                frames[i].pack(side=tk.LEFT)
            else:
                frames.append(tk.Frame(lower))
                frames[i].pack(side=tk.LEFT)

        filenames = [f for f in os.listdir("./") if f[-4:] == ".svg"]
        for i, filename in enumerate(filenames):
            if i < 6:
                self.view(frames[i], filename)

    def view(self, frame, filename):
        with open(filename, "rb") as f:
            buf = f.read()
            buf = cairosvg.svg2png(bytestring=buf)
            img = Image.open(io.BytesIO(buf))
            img = ImageTk.PhotoImage(image=img.resize((256, 256)))
            lbl = tk.Label(frame, image=img)
            lbl.image = img
            lbl.pack(padx=2, pady=2)
            tk.Label(frame, text=filename).pack()

if __name__ == "__main__":

    root = tk.Tk()
    app = App(master=root)
    app.mainloop()

