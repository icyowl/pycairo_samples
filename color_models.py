import colour
from colour.models import RGB_COLOURSPACE_sRGB
from mycolorsys import *
import numpy as np

h = "#7fb1b2"
rgb = hex_to_rgb(h)
a = np.array([x/255. for x in rgb])
print(a)

RGB = np.array([0.45595571, 0.03039702, 0.04087245])
illuminant_RGB = np.array([0.31270, 0.32900])
illuminant_XYZ = np.array([0.34570, 0.35850])
matrix_RGB_to_XYZ = np.array(
    [
        [0.41240000, 0.35760000, 0.18050000],
        [0.21260000, 0.71520000, 0.07220000],
        [0.01930000, 0.11920000, 0.95050000],
    ]
)
res = colour.RGB_to_XYZ(
    a, illuminant_RGB, illuminant_XYZ, matrix_RGB_to_XYZ, "Bradford"
    )
print(res)

res = colour.sRGB_to_XYZ(a)
print(res)