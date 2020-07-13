from plotly.graph_objs import Bar, Layout
from plotly import offline
from chapter_15.die import Die

dice1, dice2 = Die(), Die()


results = [dice1.roll()*dice2.roll() for roll_nr in range(1001)]
max_result = dice1.num_sides * dice2.num_sides

frequency = [results.count(value) for value in range(2, max_result+1)]

x_values = list(range(2, max_result+1))
data = [Bar(x= x_values, y= frequency)]

x_axis_config = {"title": "Results", "dtick": 1}
y_axis_config = {"title": "Frequency of Results"}

my_layout = Layout(title= "Results of rolling two D6 1000 times and multiplying", xaxis= x_axis_config, yaxis= y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="multiplication2_0.html")