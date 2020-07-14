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

# We want viewers to
# immediately see where the most significant earthquakes occur in the world.
# To do this, we’ll change the size of markers depending on the magnitude
# of each earthquake:
data = [{
    "type": "scattergeo",
    "lon": longs,
    "lat": lats,
    "marker": {
        "size": [5*mag for mag in magnitudes]
    }
}]

my_layout = Layout(title="Global earthquakes")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="customized_global_eartquakes.html")