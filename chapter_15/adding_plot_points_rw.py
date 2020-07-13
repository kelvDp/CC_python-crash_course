import matplotlib.pyplot as plt
from chapter_15.random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use("classic")
    fig,ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens, edgecolors="none", s=1)
    ax.scatter(0, 0, c="blue", edgecolors ="none", s=30)
    ax.scatter(rw.x_values[-1], rw.y_values[-1],c="purple", edgecolors="none", s=30 )
    plt.show()

    keeprunning = input("Would you like to keep running? 'yes' or 'no'")
    if keeprunning == "no":
        break
    else:
        continue

# A visualization is much more effective at communicating patterns in data if it
# fits nicely on the screen. To make the plotting window better fit your screen,
# adjust the size of Matplotlib’s output, like this:

# --snip--
# while True:
# # Make a random walk.
# rw = RandomWalk(50_000)
# rw.fill_walk()
# # Plot the points in the walk.
# plt.style.use('classic')
# fig, ax = plt.subplots(figsize=(15, 9))   *****
# --snip--

# you can pass a figsize argument to set the size of
# the figure. The figsize parameter takes a tuple, which tells Matplotlib the
# dimensions of the plotting window in inches.
# Matplotlib assumes that your screen resolution is 100 pixels per inch; if
# this code doesn’t give you an accurate plot size, adjust the numbers as
# necessary. Or, if you know your system’s resolution, pass plt.subplots() the
# resolution using the dpi parameter to set a plot size that makes effective use
# of the space available on your screen, as shown here:

# fig, ax = plt.subplots(figsize=(10, 6), dpi=128)  ****

