from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import json

filename = "data/eq_data_7_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

title = all_eq_data["metadata"]["title"]
all_eq_dict = all_eq_data["features"]

magnitudes, longs, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dict:
    magnitudes.append(eq_dict["properties"]["mag"])
    longs.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    hover_text.append(eq_dict["properties"]["title"])

data = [{
    "type": "scattergeo",
    "lon": longs,
    "lat": lats,
    "text": hover_text,
    "marker": {
        "size": [5 * mag for mag in magnitudes],
        "color": magnitudes,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"}
    }
}]

my_layout = Layout(title=title)

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="recent_eqs.html")