cars = ["audi" , "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw": #goes through list, and if the item name matches bmw it will print it in caps
        print(car.upper())
    else:
        print(car.lower()) #and it will just print all of the other names in lower.

#you have to pay attention to capitalization because testing for equality in python is case sensitive :
# cars = "Audi"
#cars == "audii"    --> will return false but :
#cars.lower() == "audi"  --> will return true



