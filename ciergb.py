import colour
import matplotlib.pyplot as plt

# MSDS_CMFS: Multi-spectral distributions of the colour matching functions.
datasets = colour.colorimetry.datasets.MSDS_CMFS_RGB
target = 'Wright & Guild 1931 2 Degree RGB CMFs'

print(colour.colorimetry.datasets.MSDS_CMFS)
# data = datasets[target]

# df = data.to_dataframe()
# print(df.head())

# fig, ax = plt.subplots(figsize=(6,6))
# ax.plot(df["r_bar"], c="red", label="r(λ)")
# ax.plot(df["g_bar"], c="green", label="g(λ)")
# ax.plot(df["b_bar"], c="blue", label="b(λ)")
# ax.legend()
# plt.title(target)
# plt.show()