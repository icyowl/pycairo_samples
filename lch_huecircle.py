# import pickle
# import matplotlib.pyplot as plt
# from matplotlib import patches
# from mycolorsys import lch_to_rgb

# if __name__ == "__main__":

# <<<<<<< HEAD
#     with open("lch_list.pkl", "rb") as f: lch_list = pickle.load(f)

#     fig, ax = plt.subplots(figsize=(4,4))

#     ax.set_title("Hue circle - lch")
# =======
#     print(rgb_to_hex(128, 128, 128))
#     print(hex_to_rgb("#808080"))

#     with open("lch_list", "rb") as f: lch_list = pickle.load(f)

#     fig, ax = plt.subplots(figsize=(4,4))

#     ax.set_title("Hue circle - hsl(dig, 100, 50)")
# >>>>>>> 9771e3341be7e9d5e3467288d4827c92863eda83
#     ax.set_xlim([-1, 1])
#     ax.set_ylim([-1, 1])
#     ax.axis("off")

# <<<<<<< HEAD
#     for i, (hue, (lmin, lmax), (cmin, cmax)) in enumerate(lch_list):
#         r, g, b = [x/255. for x in lch_to_rgb((lmax, cmax, hue))]
#         if 0. <= r <=1. and 0. <= g <= 1. and 0. <= b <= 1.:
#             w = patches.Wedge((0,0), 
#                             0.9, 
#                             width=0.3,
#                             theta1=i, 
#                             theta2=i+1, 
#                             color=(r, g, b))
#             ax.add_patch(w)
    
#     plt.show()
# =======
#     for i in lch_list:
#         rgb = [x/255. for x in hsl_to_rgb(i, 100, 50)]
#         w = patches.Wedge((0,0), 
#                         0.9, 
#                         width=0.3,
#                         theta1=i, 
#                         theta2=i+1, 
#                         color=rgb)
#         ax.add_patch(w)
    
#     #plt.show()
# >>>>>>> 9771e3341be7e9d5e3467288d4827c92863eda83
