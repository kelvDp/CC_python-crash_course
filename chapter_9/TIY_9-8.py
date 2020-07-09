class User:

    def __init__(self, f_name, l_name):
        self.first_name = f_name
        self.last_name = l_name

    def describe_user(self):
        print(f"This is {self.first_name} {self.last_name}.")

    def greet_user(self):
        print(f"Heyy there {self.last_name}! How are you ?")


class Admin(User):

    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privilege = Privileges()


class Privileges:

    def __init__(self):
        privileges = ["can add a post", "can delete a post", "can ban users"]
        self.privileges = privileges

    def show_privileges(self):
        print("An admin on this website can do the following:")
        for privilage in self.privileges:
            print(f"\t{privilage}")


admin = Admin("John", "Doe")

admin.privilege.show_privileges()
