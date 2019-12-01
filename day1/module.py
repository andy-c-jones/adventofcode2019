from day1.fuel import fuel_required_to_launch

class Module:
    def __init__(self, mass):
        self.mass = mass

    def fuel_required_to_launch(self):
        return fuel_required_to_launch(self.mass)