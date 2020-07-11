num_one = input("Enter the first number:")
num_two = input("Enter the second number:")

try:
    answer = int(num_one) + int(num_two)
except ValueError:
    print("You can only enter numbers.You cannot enter any words.")
else:
    print(answer)

