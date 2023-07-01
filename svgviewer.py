import io
import os
from PIL import Image, ImageTk
import tkinter as tk

import cairosvg
# o conda install -c "conda-forge/label/cf202003" cairosvg
# x conda install -c conda-forge cairosvg
# x pip install cairosvg
# cairosvgと依存libffiのバージョン違い

root = tk.Tk()

files = [f for f in os.listdir("./") if f[-4:] == ".svg"]
file = files[0]

with open(file, "rb") as f:
    buf = f.read()
    buf = cairosvg.svg2png(bytestring=buf)
    buf = Image.open(io.BytesIO(buf))
    img = ImageTk.PhotoImage(image=buf)

tk.Label(root, image=img).pack()
root.mainloop()