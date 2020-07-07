#you can also check whether a value is NOT in a list:

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

#checks to see if 'marie' is not on the list, and if she is not the print will go.
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")