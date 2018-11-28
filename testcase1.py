import unittest
from city_functions import city_function
class CityCountryTest(unittest.TestCase):
    """Tests for city_functions.py"""
    def test_city_function(self):
        """Do names like Santiago work?"""
        info = city_function("santiago", "chile")
        self.assertEqual(info, "Santiago, Chile")
unittest.main()