import matplotlib.pyplot as plt
from chapter_15.die import Die

dice1 = Die()
dice2 = Die()

results = []
max_result = dice1.num_sides + dice2.num_sides

for nr_rolls in range(1001):
    res = dice1.roll() + dice2.roll()
    results.append(res)

x_values = list(range(2, max_result + 1))
y_values = []
for value in range(2, max_result + 1):
    freq = results.count(value)
    y_values.append(freq)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)
plt.show()
