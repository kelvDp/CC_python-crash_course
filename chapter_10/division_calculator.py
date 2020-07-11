# Using Exceptions to Prevent Crashes
# Handling errors correctly is especially important when the program has
# more work to do after the error occurs. This happens often in programs that
# prompt users for input. If the program responds to invalid input
# appropriately, it can prompt for more valid input instead of crashing.

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number:")
#     if first_number == "q":
#         break
#     second_number = input("Second number:")
#     if second_number == "q":
#         break
#
#     answer = int(first_number)/ int(second_number)
#     print(answer)
# This program above does nothing to handle errors, so asking it
# to divide by zero causes it to crash

# We can make this program more error resistant by wrapping the line that
# might produce errors in a try-except block. The error occurs on the line that
# performs the division, so that’s where we’ll put the try-except block. This
# example also includes an else block. Any code that depends on the try block
# executing successfully goes in the else block:

while True:
    first_number = input("\nFirst number:")
    if first_number == "q":
        break
    second_number = input("Second number:")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:  # the else is what gets executed when the try block passes.
        print(answer)

# The only code that should go in a try block is code that
# might cause an exception to be raised.
