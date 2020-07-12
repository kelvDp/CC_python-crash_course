from chapter_11 import name_function as name

print("Enter 'q' at any time to quit.")

while True:
    first = input("\nWrite your first name:")
    if first == "q":
        break

    last = input("Write your last name:")
    if last == "q":
        break

    formatted_name = name.get_formatted_name(first,last)
    print(f"\t Neatly formatted name : {formatted_name}.")

