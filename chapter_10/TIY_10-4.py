
while True:
    user_name = input("What is your name? Enter q to sign out.")
    if user_name != "q":
        print(f"Hello {user_name}, welcome!")
        with open("guest_book.txt", "a") as f:
            f.write(f"{user_name}\n")
    if user_name == "q":
        break



