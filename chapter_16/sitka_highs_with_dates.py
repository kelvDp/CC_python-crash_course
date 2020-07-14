import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # shows all the headers in file
    # get dates and high temps from this file:
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")

plt.title("Daily high temperatures, July 8", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() #--> draws the date labels diagonally to prevent them from overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()