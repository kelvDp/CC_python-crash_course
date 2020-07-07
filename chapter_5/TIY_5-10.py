current_users = ["admin", "kelv", "Lilsh", "zana", "klein"]

new_users = ["snowy", "g", "alexi", "max", "Zana"]

for user in new_users:
    if user.lower() in current_users:
        print(f"{user.lower()} has already been taken, please choose another username.")
    else:
        print("This username is available, welcome!")


