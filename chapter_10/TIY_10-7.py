while True:
    num_one = input("Enter the first number:")
    num_two = input("Enter the second number:")
    try:
        answer = int(num_one) + int(num_two)
    except ValueError:
        print("You can only enter numbers.You cannot enter any words.")
        continue
    else:
        print(answer)
        yes_no = input("Do you want to stop? Enter 'yes' or 'no':")
        if yes_no == "no":
            break
        else:
            continue

