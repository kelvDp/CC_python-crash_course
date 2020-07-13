import matplotlib.pyplot as plt

# To use any of the styles, add one line of code before starting to
# generate the plot:

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("seaborn")

fig,ax = plt.subplots()
ax.plot(input_values,squares,linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Squares of values", fontsize=14)

ax.tick_params(axis="both", labelsize=14)

plt.show()