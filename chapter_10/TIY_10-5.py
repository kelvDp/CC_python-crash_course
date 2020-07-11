while True:
    name = input("What is your name ? Enter q to leave survey.")
    if name == "q":
        print("You have left the survey.")
        break
    answer = input("Why do you like programming?")
    survey = {name : answer}
    if name != "q":
        with open("survey.txt","a") as file_object:
            file_object.write(f"{survey}\n")
