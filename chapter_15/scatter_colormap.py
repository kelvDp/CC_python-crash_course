# A colormap is a series of colors in a gradient that moves from a starting to an
# ending color. You use colormaps in visualizations to emphasize a pattern in
# the data. For example, you might make low values a light color and high
# values a darker color.

# The pyplot module includes a set of built-in colormaps. To use one of
# these colormaps, you need to specify how pyplot should assign a color to each
# point in the data set. Here’s how to assign each point a color based on its yvalue:

import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn")
fig,ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square numbers",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()

# If you want your program to automatically save the plot to a file, you can
# replace the call to plt.show() with a call to plt.savefig():
# plt.savefig('squares_plot.png', bbox_inches='tight')
# The first argument is a filename for the plot image, which will be saved in
# the same directory as scatter_squares.py. The second argument trims extra
# whitespace from the plot. If you want the extra whitespace around the plot,
# just omit the first argument.

