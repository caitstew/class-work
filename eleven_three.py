class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    def give_raise(self, entered_raise=5000):
        self.annual_salary += entered_raise

import unittest

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.testemployee = Employee("caitlin", "stewart", 100000)
    def test_give_default_raise(self):
    	self.testemployee.give_raise()
        self.assertEqual(testemployee, "Caitlin Stewart will make $105000 next year.")
    def test_give_custom_raise(self):
        self.testemployee.give_raise()10000
    self.assertEqual(testemployee, "Caitlin Stewart will make $110000 next year.")
unittest.main()