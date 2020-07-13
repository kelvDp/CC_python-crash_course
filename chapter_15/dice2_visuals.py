# Let’s create a six-sided die and a ten-sided die, and see what happens when
# we roll them 50,000 times:

from chapter_15.die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

# create a D6 and a D10:
dice1 = Die()
dice2 = Die(10)

results = []
for roll_num in range(50_000):
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

my_layout = Layout(title="Results of rolling a D6 and a D10 50000 times", xaxis= x_axis_config, yaxis= y_axis_config)

offline.plot({"data": data, "layout": my_layout}, filename="d6_d10.html")