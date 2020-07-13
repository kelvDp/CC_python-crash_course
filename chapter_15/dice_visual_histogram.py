# Rolling two dice results in larger numbers and a different distribution of
# results.

from chapter_15.die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

# create 2 die:
dice1 = Die()
dice2 = Die()

results = []
for roll_num in range(1000):
    result = dice1.roll() + dice2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = dice1.num_sides + dice2.num_sides

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {"title": "Result", "dtick": 1} # This setting controls the spacing between tick marks on the xaxis.
y_axis_config = {"title": "Frequency of Result"}

my_layout = Layout(title="Results of rolling two D6 dice a 1000 times", xaxis= x_axis_config, yaxis= y_axis_config)

offline.plot({"data": data, "layout": my_layout}, filename="d6_d6.html")