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
print("\n")

######################
print("Oh wait...the table won't arrive in time, so I can only have two people over for dinner.")
popped_person1 = guest_list.pop() #pops last person
popped_person2 = guest_list.pop(0) #pops first person
popped_person3 = guest_list.pop(3)
popped_person4 = guest_list.pop(2)

print(f"{popped_person1}, I'm sorry but there is not going to be space for you ...")
print(f"{popped_person2}, I'm sorry but there is not going to be space for you ...")
print(f"{popped_person3}, I'm sorry but there is not going to be space for you ...")
print(f"{popped_person4}, I'm sorry but there is not going to be space for you ...")
print("\n")

print(f"{guest_list[0]} and {guest_list[1]}, you guys can still come over !")

del guest_list[:]  # can use slicing to delete everything

print(guest_list)