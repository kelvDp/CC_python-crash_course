import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "data/sitka_weather_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Data missing for {current_date}")
        else:
            dates.append(current_date)
            rainfall.append(rain)

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c="blue")

plt.title("Daily rainfall for Sitka - 2018", fontsize=24)
plt.xlabel("", fontsize=16)
plt.ylabel("Rainfall Amounts", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
