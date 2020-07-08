sandwich_orders = ["chicken mayo", "BLT", "ham and cheese", "tuna mayo"]
finished_sandwiches = []

while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print(f"I made you a {sandwiches} sandwich!")
    finished_sandwiches.append(sandwiches)

print("\nHere are all of the completed sandwiches:")
for item in finished_sandwiches:
    print(item)
