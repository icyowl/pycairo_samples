from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# img = Image.new("RGB", (128, 128))

# a = np.ones((5, 5)) * 128
# print(a)
# im = Image.fromarray(a)

im = Image.open("aka.jpg")
a = np.array(im)
# print(a)
# print(a.shape)

cyan = 0, 156, 209
magenta = 236, 0, 140
yellow = 255, 255, 0
cmy = cyan, magenta, yellow



# im = np.resize([[[*yellow]]], (128, 128, 3))
# print(im)


ls = []
for i in range(128*128):
    ls.append(cmy[i%3])
im = np.array(ls).reshape((128, 128, 3))

plt.figure(figsize=(2,2))
plt.imshow(im)
plt.show()
