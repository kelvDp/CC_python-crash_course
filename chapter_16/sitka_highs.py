import csv
import matplotlib.pyplot as plt

filename = "data/sitka_weather_07-2018_simple.csv"

# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     print(header_row)
# next() function returns the next line in the file when passed the reader object.

# To make it easier to understand the file header data, we print each header
# and its position in the list:

# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)
# The enumerate() function returns both the index of each item and the value
# of each item as you loop through a list

# Here we see that the dates and their high temperatures are stored in columns 2 and 5.
# To explore this data, we’ll process each row of data in the file and extract the values with the indexes 2
# and 5.

# Now that we know which columns of data we need, let’s read in some of that
# data. First, we’ll read in the high temperature for each day:
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) # shows all the headers in file
    # get high temps from this file:
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)
# The reader object continues from where it left off in the CSV file and automatically returns each line
# following its current position. Because we’ve already read the header row, the loop will begin at
# the second line where the actual data begins.

# To visualize the temperature data we have, we’ll first create a simple plot of
# the daily highs using Matplotlib, as shown here:

# plot the high temps:
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(highs, c="red")

plt.title("Daily high temperatures, July 8", fontsize=24)
plt.xlabel("", fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
