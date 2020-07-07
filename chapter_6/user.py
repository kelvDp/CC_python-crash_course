# this is how you can access the key and value in a dict:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# .items() gives you access to the key and value
# .values() gives you access to only the values
# .keys() gives you access to the keys