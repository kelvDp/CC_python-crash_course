class User:

    def __init__(self,f_name,l_name,age,height):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.height = height


    def describe_user(self):
        print(f"This is {self.first_name} {self.last_name}. This person is {self.age} years old and is {self.height} cm tall. ")


    def greet_user(self):
        print(f"Heyy there {self.last_name}! How are you ?")


person_1 = User("Michael","Doe", 19, 177)
person_2 = User("John","Doe", 20, 150)
person_3 = User("Alex","Doe", 36, 165)
person_4 = User("Mark","Doe", 14, 136)


person_1.describe_user()
person_1.greet_user()
print("\n")

person_2.describe_user()
person_2.greet_user()
print("\n")

person_3.describe_user()
person_3.greet_user()
print("\n")

person_4.describe_user()
person_4.greet_user()
print("\n")
