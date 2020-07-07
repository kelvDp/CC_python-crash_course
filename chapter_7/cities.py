# can use a break statement to break out of a loop once a condition has been met :

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break # so will break out of loop once input is quit
    else:
        print(f"I'd love to go to {city.title()}!")

# be careful not to start an infinite loop that cannot end because there is nothing to change its condition
