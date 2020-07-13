import matplotlib.pyplot as plt

from chapter_15.random_walk import RandomWalk

# Make a random walk
rw = RandomWalk()
rw.fill_walk()

# plot the points in the walk.
plt.style.use("classic")
fig,ax = plt.subplots()

ax.scatter(rw.x_values,rw.y_values,s=15)

plt.show()

# you can keep on running a random walk by running the above code in a while loop.
