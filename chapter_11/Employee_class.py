class Employee:

    def __init__(self,fname,lname,salary):
        self.first_name = fname
        self.last_name = lname
        self.salary = salary
        self.set_raise = 5000

    def give_raise(self):
        print(f"You get a ${self.set_raise} raise!")
        self.salary = self.salary + self.set_raise
        print(f"Your new salary is ${self.salary}")
        return self.salary


# person = Employee("dirk","black",1000)
#
# person.set_raise = 2000
#
# person.give_raise()