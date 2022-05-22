import numpy as np


# Qubit class is the standard qubit and serves as the parent class for both coaxmon and rectanglemon.
# It contains the frequency data, listing coupled qubits and the corresponding couple strength.
class Qubit:
    frequency = 0

    def __init__(self, frequency):
        self.frequency = frequency
        self.coupled_list = dict()

    def update_coupling(self, qubit, strength):
        self.coupled_list.update({qubit: strength})

    def get_coupled_list(self):
        return self.coupled_list

    def calculate_frequency(self):
        return self.frequency
