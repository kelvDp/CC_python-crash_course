import csv
import matplotlib.pyplot as plt
from datetime import datetime

file_sitka = "data/sitka_weather_2018_simple.csv"
file_death_valley = "data/death_valley_2018_simple.csv"

with open(file_sitka) as f1:
    reader1 = csv.reader(f1)
    header_row1 = next(reader1)
    dates_sitka, lows_sitka, highs_sitka = [], [], []
    for row in reader1:
        current_date_sitka = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            low_sitka = int(row[6])
            high_sitka = int(row[5])
        except ValueError:
            print(f"Data missing for {current_date_sitka}")
        else:
            dates_sitka.append(current_date_sitka)
            lows_sitka.append(low_sitka)
            highs_sitka.append(high_sitka)

with open(file_death_valley) as f2:
    reader2 = csv.reader(f2)
    header_row2 = next(reader2)
    dates_dv, lows_dv, highs_dv = [], [], []
    for row in reader2:
        current_date_dv = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            low_dv = int(row[5])
            high_dv = int(row[4])
        except ValueError:
            print(f"Data missing for {current_date_dv}")
        else:
            dates_dv.append(current_date_dv)
            lows_dv.append(low_dv)
            highs_dv.append(high_dv)

plt.style.use("seaborn")
fig, ax = plt.subplots()
plt.plot(dates_sitka, lows_sitka, c="blue")
plt.plot(dates_sitka, highs_sitka, c="red")
plt.plot(dates_dv, lows_dv, c="blue")
plt.plot(dates_dv, highs_dv, c="red")
# to plot everything on the same graph

plt.ylim(-1, 141)
plt.title("Temperatures for Sitka and Death Valley - 2018", fontsize=20)
plt.xlabel("", fontsize=15)
fig.autofmt_xdate()
plt.ylabel("Temperatures (F)", fontsize=15)
plt.tick_params(axis="both", which="major", labelsize=14)

# if you want to plot on two seperate graphs:

# plt.style.use("seaborn")
# fig, ax = plt.subplots()
# ax.plot(dates_dv, lows_dv, c="blue")
# ax.plot(dates_dv, highs_dv, c="red")
#
# plt.ylim(-1, 141)
# plt.title("Temperatures for Death Valley - 2018", fontsize=20)
# plt.xlabel("", fontsize=15)
# fig.autofmt_xdate()
# plt.ylabel("Temperatures (F)", fontsize=15)
# plt.tick_params(axis="both", which="major", labelsize=14)


plt.show()
