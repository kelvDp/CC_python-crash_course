from plotly.graph_objs import Bar, Layout
from plotly import offline
from chapter_15.die import Die

dice1 = Die()
dice2 = Die()
dice3 = Die()

results = []
max_result = dice1.num_sides + dice2.num_sides + dice3.num_sides

for roll_num in range(1000):
    result = dice1.roll() + dice2.roll() + dice3.roll()
    results.append(result)

frequencies = []
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(3,max_result+1))
data = [Bar(x= x_values, y= frequencies)]

x_axis_config = {"title":"Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Results"}

my_layout = Layout(title="Results of rolling three D6 1000 times", xaxis= x_axis_config, yaxis= y_axis_config)

offline.plot({"data": data, "layout": my_layout},filename="d6_d6_d6.html")