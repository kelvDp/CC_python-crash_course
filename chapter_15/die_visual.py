from chapter_15.die import Die

# Before creating a visualization based on the Die class, let’s roll a D6, print the
# results, and check that the results look reasonable:

# Create a D6:
die = Die()

# make some rolls and store results in a list:
# results = []
#
# for roll_num in range(101):
#     result = die.roll()
#     results.append(result)
#
# print(results)

# We’ll analyze the results of rolling one D6 by counting how many times we
# roll each number:
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value) # this will show how many times nr 1-6 is rolled.
    frequencies.append(frequency)

print(frequencies)
