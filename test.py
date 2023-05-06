import pickle 
import numpy as np
import matplotlib.pyplot as plt

p = "lchs.pkl"
with open(p, "rb") as f:
    lch = pickle.load(f)

arr = np.array(lch)
# L = arr[:, 0]
# chroma = arr[:, 1]
# hue = arr[:, 2]

# plt.plot(hue, L)
# plt.show()

hlc_list = []
for i in range(360):
    # if i: break
    h = i + 0.0
    idx, = np.where(arr[:,2] == h)
    l = [arr[i][0] for i in idx]
    c = [arr[i][1] for i in idx]
    val = h, (min(l), max(l)), (min(c), max(c))
    print(val)
    hlc_list.append(val)

with open('lch_list.pkl', 'wb') as f:
    pickle.dump(hlc_list, f)