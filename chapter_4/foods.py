my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:] #takes whole list / do this because you can't simply copy over the list var name
#!!!can't do this: friend_foods = my_foods !!!

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
