favorite_nrs = {"Alex": [1, 2, 5],
                "Jack": [6],
                "Mike": [45, 6, 3, 8],
                "Grant": [7, 12],
                "Megan": [8]
                }

for person, number in favorite_nrs.items():
    print(f"{person}'s favorite numbers are : {number}")  # if you want to print their favorite numbers as lists
    # can also do:
    #for number in number:
    #print(number) 