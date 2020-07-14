import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/eq_data_30_day_m1.json"
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

# We can also customize each marker’s color to provide some classification to
# the severity of each earthquake.
data = [{
    "type": "scattergeo",
    "lon": longs,
    "lat": lats,
    "marker": {
        "size": [5*mag for mag in magnitudes],
        "color": magnitudes,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"}
    }
}]

my_layout = Layout(title="Global earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="color_global_eartquakes.html")