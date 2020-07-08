sandwich_orders = ["chicken mayo","pastrami", "BLT", "ham and cheese","pastrami", "tuna mayo","pastrami"]
print(sandwich_orders)
print("\nUnfortunately the deli has run out of pastrami")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print("\nWe only have these sandwiches available:")
print(f"\t{sandwich_orders}")