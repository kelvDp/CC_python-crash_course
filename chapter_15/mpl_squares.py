# plot a simple line graph using Matplotlib, and then customize it to
# create a more informative data visualization. We’ll use the square number
# sequence 1, 4, 9, 16, 25 as the data for the graph.

import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] # ---> this will be the data that we will visualize
#
# # The variable fig represents the entire figure or collection of plots that are
# # generated. The variable ax represents a single plot in the figure and is the
# # variable we’ll use most of the time.
#fig,ax = plt.subplots()
# ax.plot(squares)
#
# plt.show() #--> this will open up the visualization of the data

# Matplotlib allows you to adjust every feature of a visualization.
# We’ll use a few of the available customizations to improve this plot’s
# readability

# fig,ax = plt.subplots()
# ax.plot(squares, linewidth=3)
#
# # Set chart title and label axes.
# ax.set_title("Square numbers", fontsize=24)
# ax.set_xlabel("Value",fontsize=14)
# ax.set_ylabel("Square of values", fontsize=14)
#
# # set size of tick labels:
# ax.tick_params(axis="both", labelsize=14)
#
# plt.show()

# When you give plot() a sequence of numbers, it assumes the first data
# point corresponds to an x-coordinate value of 0, but our first point
# corresponds to an x-value of 1. We can override the default behavior by
# giving plot() the input and output values used to calculate the squares:

fig,ax = plt.subplots()
ax.plot(input_values,squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of values", fontsize=14)

# set size of tick labels:
ax.tick_params(axis="both", labelsize=14)

plt.show()

