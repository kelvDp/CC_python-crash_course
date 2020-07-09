from random import randint

lottery = [14, 2, 6, 47, 20, 12, 23, 4, 15, 10, "e", "a", "i","o","u"]

def choose_winner(list):
    luckynr1 = list[randint(0,len(list))]
    luckynr2 = list[randint(0, len(list))]
    luckynr3 = list[randint(0, len(list))]
    luckynr4 = list[randint(0, len(list))]
    winning_numbers = [luckynr1,luckynr2,luckynr3,luckynr4]
    print("Any ticket that matches the following numbers and/or letters win !")
    print(f"The winning characters are --> {winning_numbers}")


choose_winner(lottery)