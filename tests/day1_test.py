import unittest
from src.day1.fuel import fuel_required_to_launch
from src.day1.module import Module
from src.day1.spacecraft import Spacecraft
from functools import reduce

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


class TestSpacecraft(unittest.TestCase):

# the fuel needed to launch the craft is the sum of the fuel needed
# to launch the modules
    def test_fuel_required_to_launch_spacecraft(self):
        self.assertEqual(Spacecraft([Module(12)]).fuel_required_to_launch(), 2)
        self.assertEqual(Spacecraft([Module(12), Module(12)]).fuel_required_to_launch(), 4)
        self.assertEqual(Spacecraft([Module(12), Module(12), Module(12)]).fuel_required_to_launch(), 6)

    def test_fuel_required_to_launch_spacecraft_when_fuel_needs_fuel(self):
        self.assertEqual(Spacecraft([Module(1000)]).fuel_required_to_launch(), 483)
        self.assertEqual(Spacecraft([Module(500), Module(500)]).fuel_required_to_launch(), 468)
        self.assertEqual(Spacecraft([Module(120), Module(380), Module(500)]).fuel_required_to_launch(), 458)
        self.assertEqual(Spacecraft([Module(43539)]).fuel_required_to_launch(), 21740)
        self.assertEqual(Spacecraft([Module(12355), Module(2345)]).fuel_required_to_launch(), 7301)
        self.assertEqual(Spacecraft([Module(2345), Module(54325), Module(45388)]).fuel_required_to_launch(), 50946)

    def test_day1_input(self):
        with open("./src/day1/input.txt", "r") as file:
            modules = []
            for mass in file.readlines():
                modules.append(Module(int(mass)))
            self.assertEqual(Spacecraft(modules).fuel_required_to_launch(), 4896902)
