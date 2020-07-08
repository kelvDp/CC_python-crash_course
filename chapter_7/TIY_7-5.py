flag = True

while flag:
    prompt = input("How old are you ? Enter quit to checkout")
    if prompt == "quit":
        break
    if int(prompt) < 3:
        print("Your ticket is free!")
    elif int(prompt) >= 3 and int(prompt) <= 12:
        print("Your ticket will be $10.")
    elif int(prompt) > 12:
        print("Your ticket will be $15.")