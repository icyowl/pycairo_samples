import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
import os 


target = "#34f80a"

r_value = 0.8
g_value = 0.7
b_value = 0.6
r_color = [r_value, 0.0, 0.0]
g_color = [0.0, g_value, 0.0]
b_color = [0.0, 0.0, g_value]

plt.figure(figsize=(4,3))
ax = plt.axes()
plt.axis([0,5,0,5])

r = Rectangle((1.5, 3), 1, 0.8, color=r_color)
g = Rectangle((1.5, 2), 1, 0.8, color=g_color)
b = Rectangle((1.5, 1), 1, 0.8, color=b_color)
rgb = Rectangle((3, 1), 1, 2.8, color=[r_value, g_value, b_value])

ax.add_patch(r)
ax.add_patch(g)
ax.add_patch(b)
ax.add_patch(rgb)

plt.text(0.5, 3.2, f"R: {r_value}", size=12)
plt.text(0.5, 2.2, f"G: {g_value}", size=12)
plt.text(0.5, 1.2, f"B: {b_value}", size=12)

font = {"family": "YuGothic"}
if os.name == "nt": font["family"] = "Yu Gothic"

plt.title(f"RGB加法混色 {target}", **font)
plt.show()