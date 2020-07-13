from chapter_15.die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

dice1 = Die(8)
dice2= Die(8)

results = []
max_result = dice1.num_sides + dice2.num_sides

for roll_num in range(1001):
    result = dice1.roll() + dice2.roll()
    results.append(result)

frequencies = []
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


x_values = list(range(2,max_result+1))
data = [Bar(x= x_values, y= frequencies)]

x_axis_config = {"title":"Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Results"}

my_layout = Layout(title="Results of rolling two D8 a 1000 times", xaxis= x_axis_config, yaxis= y_axis_config)

offline.plot({"data": data, "layout": my_layout}, filename="d8_d8.html")
