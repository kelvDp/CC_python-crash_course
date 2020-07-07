# if you ask for a key that does not exist, it will give an error :
# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) # since there is not a key named points in the dict

# you can use the get method to avoid this:
# The get() method requires a key as a first argument. As a second optional
# argument, you can pass the value to be returned if the key doesn’t exist:
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
# If the key 'points' exists in the dictionary, you’ll get the corresponding
# value. If it doesn’t, you get the default value. In this case, points doesn’t exist,
# and we get a clean message instead of an error:
# No point value assigned. And if you leave out the second argument, it will return None
