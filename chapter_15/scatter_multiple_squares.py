import matplotlib.pyplot as plt

# To plot a series of points, we can pass scatter() separate lists of x- and yvalues,
# like this:
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# Writing lists by hand can be inefficient, especially when we have many
# points. Rather than passing our points in a list, let’s use a loop in Python to
# do the calculations for us.
# Here’s how this would look with 1000 points:

x_values = range(1,1001)
y_values = [x**2 for x in x_values]


plt.style.use("seaborn")
fig,ax = plt.subplots()
ax.scatter(x_values, y_values, s=10) # s argument to set the size of the dots used to draw the graph.

ax.set_title("Square numbers",fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])
# we use the axis() method to specify the range of each axis. This method requires four values: the min & max values
# for the xaxis and the y-axis. Here, we run the x-axis from 0 to 1100 and the y-axis from 0 to 1,100,000.

plt.show()

# To change the color of the points, pass c to scatter() with the name of a color
# to use in quotation marks, as shown here:
# ax.scatter(x_values, y_values, c='red', s=10)

# You can also define custom colors using the RGB color model:
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

