ordinal_numbers = list(range(1,10))

for num in ordinal_numbers:
    if num == 1:
        print("1st")
    if num == 2:
        print("2nd")
    if num == 3:
        print("3rd")
    if num in range(4,10):
        print(f"{num}th")