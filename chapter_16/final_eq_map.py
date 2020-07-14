import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

# To finish this map, we’ll add some informative text that appears when you
# hover over the marker representing an earthquake.

magnitudes, longs, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    title = eq_dict["properties"]["title"]
    magnitudes.append(mag)
    longs.append(lon)
    lats.append(lat)
    hover_texts.append(title)

data = [{
    "type": "scattergeo",
    "lon": longs,
    "lat": lats,
    "text": hover_texts,
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

offline.plot(fig, filename="final_global_eartquakes.html")