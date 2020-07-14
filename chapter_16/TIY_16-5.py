"""This is just a better version for TIY_16-2"""

import csv
import matplotlib.pyplot as plt
from datetime import datetime


def get_weather_data(file):
    """Func to retrieve data from weather file"""
    with open(file) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        date_index = header_row.index("DATE")
        high_index = header_row.index("TMAX")
        low_index = header_row.index("TMIN")

        for row in reader:
            current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
            try:
                low = int(row[low_index])
                high = int(row[high_index])
            except ValueError:
                print(f"Data missing from {current_date}.")
            else:
                dates.append(current_date)
                lows.append(low)
                highs.append(high)


filename = "data/sitka_weather_2018_simple.csv"
dates, lows, highs = [], [], []
get_weather_data(filename)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.plot(dates, highs, c="red", alpha=0.5)
plt.fill_between(dates, lows, highs, facecolor="blue", alpha=0.2)

file_two = "data/death_valley_2018_simple.csv"
dates, lows, highs = [], [], []
get_weather_data(file_two)

ax.plot(dates, lows, c="blue", alpha=0.5)
ax.plot(dates, highs, c="red", alpha=0.5)
plt.fill_between(dates, lows, highs, facecolor="blue", alpha=0.1)

title = "Daily highs and lows for Sitka and Death Valley -2018"
plt.title(title, fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize=16)

plt.show()
