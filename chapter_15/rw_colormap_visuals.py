import matplotlib.pyplot as plt
from chapter_15.random_walk import RandomWalk


while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("classic")
    fig,ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)
    plt.show()

    keeprunning = input("Would you like to keep running? 'yes' or 'no'")
    if keeprunning == "no":
        break
    else:
        continue


# In addition to coloring points to show their position along the walk, it would
# be useful to see where each walk begins and ends. To do so, we can plot the
# first and last points individually after the main series has been plotted. We’ll
# make the end points larger and color them differently to make them stand
# out, as shown here:

# --snip--
# while True:
# --snip--
# ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=15)
# # Emphasize the first and last points.
# ax.scatter(0, 0, c='green', edgecolors='none', s=100)
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)
# plt.show()
# --snip--

# Let’s remove the axes in this plot so they don’t distract from the path of each
# walk. To turn off the axes, use this code:

# --snip--
# while True:
# --snip--
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)
# # Remove the axes.
# ax.get_xaxis().set_visible(False)
# ax.get_yaxis().set_visible(False)
# plt.show()
# --snip--
