import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "data/death_valley_2018_simple.csv"
place_name = ""
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    name_index = header_row.index("NAME")
    date_index = header_row.index("DATE")
    high_index = header_row.index("TMAX")
    low_index = header_row.index("TMIN")

    dates, lows, highs = [], [], []
    for row in reader:
        if not place_name:
            place_name = row[name_index]

        current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        try:
            low = int(row[low_index])
            high = int(row[high_index])
        except ValueError:
            print(f"Data missing for {current_date}")
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)


plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, lows, c="blue", alpha=0.5)
ax.plot(dates, highs, c="red", alpha=0.5)
plt.fill_between(dates, lows, highs, facecolor="blue", alpha=0.1)

title = f"Daily high and low temperatures -2018 \n{place_name}"
plt.title(title, fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
