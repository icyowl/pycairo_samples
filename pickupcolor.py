from PIL import ImageColor, Image
import colorsys
import numpy as np

hex_code = '#169bbd'
rgb = ImageColor.getcolor(hex_code, "RGB")

hls = colorsys.rgb_to_hls(*rgb)

# print(hls)

im = Image.open('./jaromir-kalina3.jpg')
# rgb_im = im.convert('RGB')
arr_im = np.array(im)
w, h, c = arr_im.shape
arr = arr_im.reshape(w*h, c)
rgb = [int(np.mean(a)) for a in arr.T]
print(rgb)

hex_l = [format(c, 'x').zfill(2) for c in rgb]

hex_code = "#" + "".join(hex_l)
print(hex_code)