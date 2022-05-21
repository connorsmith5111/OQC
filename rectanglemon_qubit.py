from qubit import Qubit


# Rectanglemon inherits from the Qubit class and also contains the rectangle area data.
class Rectanglemon(Qubit):
    coupled_list = dict()
    length_1 = 0
    length_2 = 0
    height_1 = 0
    height_2 = 0

    def __init__(self, frequency, length_1, height_1, length_2, height_2):
        super().__init__(frequency)
        self.length_1 = length_1
        self.height_1 = height_1
        self.length_2 = length_2
        self.height_2 = height_2

    # Overrides the calculate_frequency function from Qubit to implement its own frequency calculation.
    def calculate_frequency(self):
        return self.area_of_rectangle(self.length_1, self.height_1) + self.area_of_rectangle(self.length_2,
                                                                                             self.height_2)

    def area_of_rectangle(self, length, height):
        return length * height
