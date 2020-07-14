from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import csv

filename = "data/world_fires_1_day.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    long_index = header_row.index("longitude")
    lats_index = header_row.index("latitude")
    longs, lats = [], []
    for row in reader:
        try:
            lo = float(row[long_index])
            la = float(row[lats_index])
        except ValueError:
            print("Values not found")
        else:
            longs.append(lo)
            lats.append(la)


data = [{
    "type": "scattergeo",
    "lon": longs,
    "lat": lats
}]

my_layout = Layout(title="World fires")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="world_fires.html")
