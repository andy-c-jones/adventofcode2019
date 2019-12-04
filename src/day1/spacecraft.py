from src.day1.module import Module
from src.day1.fuel import fuel_required_to_launch
from functools import reduce

class Spacecraft():
    def __init__(self, modules):
        self.modules = modules
    
    def fuel_required_to_launch(self):
        return reduce(lambda t, m: t + module_fuel(m), self.modules, 0)

def module_fuel(m):
    f = m.fuel_required_to_launch()
    return f + fuel_for_fuel_mass(f)

def fuel_for_fuel_mass(fuel_mass):
    f = fuel_required_to_launch(fuel_mass)
    if(f > 0):
        return f + fuel_for_fuel_mass(f)
    return 0