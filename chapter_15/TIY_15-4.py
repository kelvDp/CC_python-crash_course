import matplotlib.pyplot as plt
from chapter_15.modified_rw_class import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("classic")
    fig,ax = plt.subplots()
    point_nrs = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_nrs, cmap=plt.cm.Blues, edgecolors="none", s=10)
    ax.scatter(0, 0, c="red", edgecolors="none", s=40)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="green", edgecolors="none", s=40)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keepgoing = input("Enter 'yes' or 'no' to keep going:")
    if keepgoing == "no":
        break
    else:
        continue
