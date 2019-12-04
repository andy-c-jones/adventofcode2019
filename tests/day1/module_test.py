import unittest
from src.day1.module import Module

# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module,
# take its mass, divide by three, round down, and subtract 2.
# For example:
#     For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
#     For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
#     For a mass of 1969, the fuel required is 654.
#     For a mass of 100756, the fuel required is 33583.
class TestModule(unittest.TestCase):

    def test_fuel_required_to_launch_module_of_mass_12(self):
        self.assertEqual(Module(12).fuel_required_to_launch(), 2)

    def test_fuel_required_to_launch_module_of_mass_14(self):
        self.assertEqual(Module(14).fuel_required_to_launch(), 2)

    def test_fuel_required_to_launch_module_of_mass_1969(self):
        self.assertEqual(Module(1969).fuel_required_to_launch(), 654)

    def test_fuel_required_to_launch_module_of_mass_100756(self):
        self.assertEqual(Module(100756).fuel_required_to_launch(), 33583)
