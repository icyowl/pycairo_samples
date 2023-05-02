import colour
import matplotlib.pyplot as plt

# colour.plotting.colour_style()
# colour.plotting.plot_visible_spectrum()

# res = colour.colorimetry.RGB_ColourMatchingFunctions()

datasets = colour.colorimetry.datasets.MSDS_CMFS_RGB
target = 'Wright & Guild 1931 2 Degree RGB CMFs'
# key =  'Stiles & Burch 1955 2 Degree RGB CMFs'
# key = 'Stiles & Burch 1959 10 Degree RGB CMFs'
data = datasets[target]

df = data.to_dataframe()
print(df.head())

fig, ax = plt.subplots(figsize=(6,6))
ax.plot(df["r_bar"], c="red", label="r(λ)")
ax.plot(df["g_bar"], c="green", label="g(λ)")
ax.plot(df["b_bar"], c="blue", label="b(λ)")
ax.legend()
plt.title(target)
plt.show()