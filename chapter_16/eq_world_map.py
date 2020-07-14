# With the information we’ve pulled so far, we can build a simple world map.
# Although it won’t look presentable yet, we want to make sure the
# information is displayed correctly before focusing on style and presentation
# issues. Here’s the initial map:

import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

magnitudes, longs, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    magnitudes.append(mag)
    longs.append(lon)
    lats.append(lat)

# Map the earthquakes:

# data = [Scattergeo(lon=longs, lat=lats)]
# This is one of the simplest ways to define the data for a chart in Plotly.
# But it’s not the best way when you want to customize the presentation.
# Here’s an equivalent way to define the data for the current chart:
data = [{
    "type": "scattergeo",
    "lon": longs,
    "lat": lats
}]

my_layout = Layout(title="Global earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_eartquakes.html")
