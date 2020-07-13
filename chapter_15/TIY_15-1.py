import matplotlib.pyplot as plt
# first 5 numbers:
# x_values = [1, 2, 3, 4, 5]
# y_values = [x**3 for x in x_values]

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")

fig,ax = plt.subplots()
ax.scatter(x_values,y_values, s=10)

ax.set_title("Cubic Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Cubes of value",fontsize=14)
ax.tick_params(axis="both",labelsize=14)

plt.show()