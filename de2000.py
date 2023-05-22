import numpy as np
from skimage import color

RGB1 = np.array([32,32,32],np.uint8)
RGB2 = np.array([32,31,32],np.uint8)
# RGB1 = 32, 33, 45
def hex2rgb(hex: str) -> tuple:
    c = hex.strip("#")
    rgb = [int(x, 16) for x in (c[:2], c[2:4], c[4:])]
    return tuple(x/255. for x in rgb)

def rgb2lab(rgb):
    return color.rgb2lab(rgb)

def ciede2000(rgb1, rgb2):
    return color.deltaE_ciede2000(rgb2lab(rgb1), rgb2lab(rgb2))

bluegray = {
    50: "#eceff1",
    100: "#cfd8dc",
    200: "#b0bec5",
    300: "#90a4ae",
    400: "#78909c",
    500: "#607d8b",
    600: "#546e7a",
    700: "#455a64",
    800: "#37474f",
    900: "#263238"
}

indigo = {
    50: "#e8eaf6",
    100: "#c5cae9",
    200: "#9fa8da",
    300: "#7986cb",
    400: "#5c6bc0",
    500: "#3f51b5",
    600: "#3949ab",
    700: "#303f9f",
    800: "#283593",
    900: "#1a237e"
}

blue = {
    50: "#e3f2fd",
    100: "#bbdefb",
    200: "#90caf9",
    300: "#64b5f6",
    400: "#42a5f5",
    500: "#2196f3",
    600: "#1e88e5",
    700: "#1976d2",
    800: "#1565c0",
    900: "#0d47a1"
}

if __name__ == "__main__":

    pre_rgb = None
    for i in range(100, 900, 100):
        rgb = indigo[i]
        if pre_rgb:
            rgb1 = hex2rgb(pre_rgb) 
            rgb2 = hex2rgb(rgb)
            print(ciede2000(rgb1, rgb2))
        pre_rgb = rgb