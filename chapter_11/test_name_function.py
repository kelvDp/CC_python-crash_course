# Here’s a test case with one method that verifies that the function
# get_formatted_name() works correctly when given a first and last name:

import unittest
from chapter_11 import Working_n_func as name

# This class must inherit from the class unittest.TestCase so Python knows how to run the
# tests you write:
class NamesTestCase(unittest.TestCase):
    """This tests for name_function.py"""

# contains a single method that tests one aspect of get_formatted_name().
    def test_first_last_name(self):
        """Do names like Janis Joplin work??"""
        formatted_name = name.get_formatted_name("janis","joplin")
        self.assertEqual(formatted_name,"Janis Joplin")
# Assert methods verify that a result you received matches the result you expected to receive.

# Now that we know get_formatted_name() works for simple names again, let’s
# write a second test for people who include a middle name:
    def test_first_last_middle_name(self):
        formatted_name = name.get_formatted_name("wolfgang","mozzart","amadeus")
        self.assertEqual(formatted_name,"Wolfgang Amadeus Mozzart")

if __name__ == "__main__":
    unittest.main()

# This test will pass and This output indicates that the function get_formatted_name() will always
# work for names that have a first and last name unless we modify the
# function. When we modify get_formatted_name(), we can run this test again. If
# the test case passes, we know the function will still work for names like Janis
# Joplin.