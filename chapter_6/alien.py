# dictionaries have a key:value pair (js object)
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])  # you index with the key and not a numerical index
print(alien_0['points'])  # this will return the value associated with the key

# Adding new key value pairs:

print(alien_0)

alien_0['x_position'] = 0  # you basically give it a key name (var name) and assign it a value
alien_0['y_position'] = 25
print(alien_0)  # will now show new key:value pair

# this means that you can start of with an empty dictionary and just keep on adding new key:values

# Modifying values in a dictionary:

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Removing key:value pairs:

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# you can also nest dictionaries and lists etc inside of each other and vice versa:
alien_00 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# now you can pass these dictionaries into a list to make it easier to loop through.:
aliens = [alien_00, alien_1, alien_2]
for alien in aliens:
    print(alien)

# we can use the method from above to quickly generate 30 aliens for example:
# Make an empty list for storing aliens.
aliensT = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliensT.append(new_alien)

# you can also access the new list and change the first few aliens as well:
# for alien in aliensT[:3]:
#     if alienT['color'] == 'green':
#         alienT['color'] = 'yellow'
#         alienT['speed'] = 'medium'
#         alienT['points'] = 10
# can expand on this with elif and else statements too

# Show the first 5 aliens.
for alien in aliensT[:5]:
    print(alien)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

