# Let’s start by loading the data and displaying it in a format that’s easier to
# read. This is a long data file, so instead of printing it, we’ll rewrite the data
# to a new file. Then we can open that file and scroll back and forth easily
# through the data:

import json

# Explore the structure of the data.
filename = "data/eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

# if you want to write it into a readable file:
# readable_file = "data/readable_eq_data.json"
# with open(readable_file, "w") as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data["features"]
# print(len(all_eq_dicts))

# Using the list containing data about each earthquake, we can loop through
# that list and extract any information we want. Now we’ll pull the magnitude
# of each earthquake:
# magnitudes = []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict["properties"]["mag"]
#     magnitudes.append(mag)
# print(magnitudes[:10])

# Next, we’ll pull the location data for each earthquake, and then we can
# make a map of the earthquakes.

# The location data is stored under the key "geometry". Inside the geometry
# dictionary is a "coordinates" key, and the first two values in this list are the
# longitude and latitude. Here’s how we’ll pull this data:
magnitudes, longs, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    magnitudes.append(mag)
    longs.append(lon)
    lats.append(lat)

print(magnitudes[:10])
print(longs[:5])
print(lats[:5])