from plotly.graph_objs import Bar, Layout
from plotly import offline
from chapter_15.die import Die

dice1 = Die()
dice2 = Die()

results = []
max_result = dice1.num_sides * dice2.num_sides

for roll_nr in range(1001):
    result = dice1.roll() * dice2.roll()
    results.append(result)

frequency = []
for value in range(2, max_result+1):
    freq = results.count(value)
    frequency.append(freq)


x_values = list(range(2, max_result+1))
data = [Bar(x= x_values, y= frequency)]

x_axis_config = {"title": "Results", "dtick": 1}
y_axis_config = {"title": "Frequency of Results"}

my_layout = Layout(title= "Results of rolling two D6 1000 times and multiplying", xaxis= x_axis_config, yaxis= y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="multiplication.html")