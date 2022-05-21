from qubit import Qubit
from math import pi


# Coaxmon inherits from the Qubit class and also contains the radius data.
class Coaxmon(Qubit):
    coupled_list = dict()

    center_radius = 0
    inner_radius = 0
    outer_radius = 0

    area_center = 0
    area_ring = 0

    def __init__(self, frequency, center, inner, outer):
        super().__init__(frequency)
        self.center_radius = center
        self.inner_radius = inner
        self.outer_radius = outer

    # Overrides the calculate_frequency function from Qubit to implement its own frequency calculation.
    def calculate_frequency(self):
        self.calculate_center()
        self.calculate_outer_ring(self.inner_radius, self.outer_radius)
        return self.area_center / self.area_ring

    def calculate_area_of_circle(self, radius):
        return pi * radius ** 2

    def calculate_center(self):
        self.area_center = self.calculate_area_of_circle(self.center_radius)

    def calculate_outer_ring(self, inner_circle, outer_circle):
        self.area_ring = (self.calculate_area_of_circle(outer_circle)) - (self.calculate_area_of_circle(inner_circle))
