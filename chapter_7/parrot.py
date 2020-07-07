# this is how we add and handle user input :
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#the answer that the user types in is in the form of a string, so if you want a number for example , you would have to cast it to an interger

# we can let the user decide when to quit a while loop :
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
# this loop will run until the user enters the word quit.
# can add an if statement to stop the loop from printing the word quit as an input

# can add a flag to the code above to make it more clean :
prompt_2 = "\nTell me something, and I will repeat it back to you:"
prompt_2 += "\nEnter 'quit' to end the program. "
active = True
while active: # so while active == true run this loop
    message = input(prompt)
    if message == 'quit':  # and if this happens make active False and stop loop
        active = False
    else:
        print(message)

