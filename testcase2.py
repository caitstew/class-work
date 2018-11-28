import unittest
from city_functions import city_function
class CityCountryTest(unittest.TestCase):
    """Tests for city_functions.py"""
    def test_city_function(self):
        """Do names like Santiago work?"""
        info = city_function("santiago", "chile")
        self.assertEqual(info, "Santiago, Chile")
    def test_city_country_population(self):
    	"""test santiago, chile with pop = 5000000 work"""
    	info = city_function("santiago", "chile", "5000000")
    	self.assertEqual(info, "Santiago, Chile - population: 5000000")
unittest.main()