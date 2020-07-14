# We can make our informative graph even more useful by including the low
# temperatures. We need to extract the low temperatures from the data file
# and then add them to our graph, as shown here:

import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "data/sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)

# plt.style.use("seaborn")
# fig, ax = plt.subplots()
# ax.plot(dates, lows, c="blue")
# ax.plot(dates, highs, c="red")
#
# plt.title("Daily high and low temperatures - 2018", fontsize = 24)
# plt.xlabel("", fontsize = 16)
# fig.autofmt_xdate()
# plt.ylabel("Temperatures (F)", fontsize = 16)
# plt.tick_params(axis="both", which="major", labelsize= 16)
#
# plt.show()

# Let’s add a finishing touch to the graph by using
# shading to show the range between each day’s high and low temperatures.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, lows, c="blue", alpha = 0.5)
ax.plot(dates, highs, c="red", alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha = 0.1)
# The alpha argument controls a color’s transparency.

plt.title("Daily high and low temperatures - 2018", fontsize = 24)
plt.xlabel("", fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize = 16)
plt.tick_params(axis="both", which="major", labelsize= 16)

plt.show()