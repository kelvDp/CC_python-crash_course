# Exceptions
# Python uses special objects called exceptions to manage errors that arise
# during a program’s execution. Whenever an error occurs that makes Python
# unsure what to do next, it creates an exception object.If you write code that
# handles the exception, the program will continue running without halting and giving a traceback

# We can avoid traceback errors by adding in try-except blocks of code:
# A try-except block asks
# Python to do something, but it also tells Python what to do if an exception is
# raised.

# --------- ZeroDivisionError -------------
# if you try dividing a number by 0 , python will give a traceback error
# i.e ---> this code will produce an error :
# print(5/0)

# So we can use a try-except block to handle this:
try:
    print(5/0)
except ZeroDivisionError:  # you tell it what error you might expect from the code and how to handle the error
    print("You can't devide by zero!")




