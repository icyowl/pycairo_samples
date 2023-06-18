import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(0,1,0.01)
y1 = np.cos(np.pi*x)
y2 = np.cos(2*np.pi*x)
y3 = np.cos(3*np.pi*x)

fig, axs = plt.subplots(1,3,figsize=(12,4))
for ax in axs:
    ax.set_xlim((0,512))
    ax.set_ylim((0,512))
    ax.axis("off")

axs[0].plot(x, y1)
axs[1].plot(x, y2)
axs[2].plot(x, y3)

plt.show()