import unittest
from src.day1.module import Module
from src.day1.spacecraft import Spacecraft
from functools import reduce

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
        with open("./day1/input.txt", "r") as file:
            modules = []
            for mass in file.readlines():
                modules.append(Module(int(mass)))
            self.assertEqual(Spacecraft(modules).fuel_required_to_launch(), 4896902)