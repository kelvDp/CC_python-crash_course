import unittest
from chapter_11.Employee_class import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Jack", "Black", 3000)

    def test_give_default_raise(self):
        new_raise = self.employee.give_raise()
        self.assertEqual(new_raise, 8000)

    def test_give_custom_raise(self):
        self.employee.set_raise = 3000
        new_raise = self.employee.give_raise()
        self.assertEqual(new_raise, 6000)


if __name__ == "__main__":
    unittest.main()
