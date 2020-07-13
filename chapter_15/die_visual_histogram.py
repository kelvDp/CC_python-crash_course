# With a list of frequencies, we can make a histogram of the results. A
# histogram is a bar chart showing how often certain results occur. Here’s the
# code to create the histogram:

from chapter_15.die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline


die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value) # this will show how many times nr 1-6 is rolled.
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x = x_values, y = frequencies)]

x_axis_config = {"title": "Result"}
y_axis_config = {"title": "Frequency of Result"}

my_layout = Layout(title="Results of rolling a D6 1000 times", xaxis= x_axis_config, yaxis= y_axis_config)

offline.plot({"data": data, "layout": my_layout}, filename="d6.html")