import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "data/san_francisco.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, lows, highs = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            low = int(row[6])
            high = int(row[5])
        except ValueError:
            print(f"Data missing for {current_date}.")
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, lows, c="blue")
ax.plot(dates, highs, c="red")

plt.title("Daily highs and lows for San Francisco -2018", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
