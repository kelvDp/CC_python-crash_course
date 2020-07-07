guest_list = ["Angela Yu" , "Jack Sparrow", "Michael Jackson"]

print(f"Dear {guest_list[0]}, I would like to invite you for dinner.")
print(f"Dear {guest_list[1]}, I would like to invite you for dinner.")
print(f"Dear {guest_list[2]}, I would like to invite you for dinner.")
print("\n")
print("I found a bigger dinner table!, so we can invite some more people!")
print("\n")

guest_list.insert(0,"John Doe") #adds item at beginning of list
guest_list.insert(2,"Jane Doe") #adds item in the middle of list
guest_list.append("Jack Black") #adds item to the end of list

#new guest-list invite:

print(f"Dear {guest_list[0]}, I would like to invite you for dinner.")
print(f"Dear {guest_list[1]}, I would like to invite you for dinner.")
print(f"Dear {guest_list[2]}, I would like to invite you for dinner.")
print(f"Dear {guest_list[3]}, I would like to invite you for dinner.")
print(f"Dear {guest_list[4]}, I would like to invite you for dinner.")
print(f"Dear {guest_list[5]}, I would like to invite you for dinner.")

