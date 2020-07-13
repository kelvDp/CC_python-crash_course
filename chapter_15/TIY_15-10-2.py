from plotly.graph_objs import Bar, Layout
from plotly import offline
from chapter_15.random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

x_values = rw.x_values
y_values = rw.y_values
data = [Bar(x= x_values, y= y_values)]

x_axis_config = {"title":"X-axis", "dtick": 1}
y_axis_config = {"title": "Y-axis"}

my_layout = Layout(title="Random walk", xaxis= x_axis_config, yaxis= y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="rwHistogram.html")





