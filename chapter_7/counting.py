#while loops will perform an action until a certain condition is met:

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#so while current number is less than or equal to 5 , it will run and increment the number
#so will print 1-5 and end loop

# Rather than breaking out of a loop entirely (with a break) without executing the rest of its
# code, you can use the continue statement to return to the beginning of the
# loop based on the result of a conditional test
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)