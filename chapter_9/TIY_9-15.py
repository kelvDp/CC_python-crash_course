from random import randint

lottery = [14, 2, 6, 47, 20, 12, 23, 4, 15, 10, "e", "a", "i", "o", "u"]


def choose_winner(lotto_list):
    luckynr1 = lotto_list[randint(0, len(lotto_list)-1)]
    luckynr2 = lotto_list[randint(0, len(lotto_list)-1)]
    luckynr3 = lotto_list[randint(0, len(lotto_list)-1)]
    luckynr4 = lotto_list[randint(0, len(lotto_list)-1)]
    winning_numbers = [luckynr1, luckynr2, luckynr3, luckynr4]
    return winning_numbers


my_ticket = [6, 23, "o", 14]
counter = 0

while True:
    winning_ticket = choose_winner(lottery)
    counter += 1
    if winning_ticket == my_ticket:
        break


print(f"The loop ran {counter} times!")
