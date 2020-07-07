while True:
    prompt = "What pizza toppings would you like ?"
    prompt += "\nEnter quit when you are done."
    topping = input(prompt)
    print(f"I'll add some {topping} to your pizza!")
    if topping == "quit":
        break
