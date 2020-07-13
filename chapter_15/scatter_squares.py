# Sometimes, it’s useful to plot and style individual points based on certain
# characteristics.

import matplotlib.pyplot as plt

# To plot a single point, use the scatter() method. Pass the single (x, y)
# values of the point of interest to scatter() to plot those values:

plt.style.use("seaborn")
# fig,ax = plt.subplots()
# ax.scatter(2, 4)

fig,ax = plt.subplots()
ax.scatter(2, 4, s=200) # s argument to set the size of the dots used to draw the graph.

ax.set_title("Square numbers",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()