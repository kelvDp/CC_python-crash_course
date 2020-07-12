import unittest
from chapter_11 import city_function as city

class TestCityFunc(unittest.TestCase):
    """Test get_city function"""

    def test_city_country_name(self):
        formatted_name = city.get_city("johannesburg","south africa")
        self.assertEqual(formatted_name,"Johannesburg,South Africa")

if __name__ == "__main__":
    unittest.main()


