class User:

    def __init__(self,f_name,l_name,age,height):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
        self.height = height
        self.login_attempts = 0

    def describe_user(self):
        print(f"This is {self.first_name} {self.last_name}. This person is {self.age} years old and is {self.height} cm tall. ")

    def greet_user(self):
        print(f"Heyy there {self.last_name}! How are you ?")

    def display_login_attempts(self):
        print(self.login_attempts)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login(self):
        self.login_attempts = 0


user_1 = User("Jane","Doe",24,150)
user_1.display_login_attempts() # original number
print("\n")

user_1.increment_login_attempts()
user_1.display_login_attempts()
print("\n")

user_1.increment_login_attempts()
user_1.display_login_attempts()
print("\n")

user_1.increment_login_attempts()
user_1.display_login_attempts()
print("\n")

user_1.increment_login_attempts()
user_1.display_login_attempts()
print("\n")

# to revert login attempts back to 0 :
user_1.reset_login()
user_1.display_login_attempts()