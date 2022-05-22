import qubit
import numpy as np


# The Hamiltonian class is responsible for printing the hamiltonian of a system given a list of arbitrary qubits.
class Hamiltonian:
    qubit_system = []

    def __init__(self, qubit_system):
        self.qubit_system = qubit_system

    # Builds two halves of the expression and concatenates them at the end to form the output string.
    def print_hamiltonian(self):
        frequency_expression = ""
        coupled_expression = ""
        # Loop through every qubit in the given list
        for qubit.Qubit in self.qubit_system:
            frequency = qubit.Qubit.calculate_frequency() / 2
            index = self.qubit_system.index(qubit.Qubit)
            coupled_list = qubit.Qubit.get_coupled_list()
            # Loop through the list of coupled qubits associated with this qubit
            for key in coupled_list:
                couple_strength = coupled_list.get(key)
                couple_index = self.qubit_system.index(key)
                coupled_expression += f"{couple_strength}X{index + 1}X{couple_index + 1} + "

            frequency_expression += f"{frequency}Z{index + 1} + "
        coupled_expression = coupled_expression[:-2]
        print("H = " + frequency_expression + coupled_expression)
        print("Hamiltonian Matrix:")
        self.print_matrix()

    # Calculates and prints the actual matrix representation of the hamiltonian
    def print_matrix(self):
        result = 0
        pauli_z = np.array([[1, 0], [0, -1]])
        pauli_x = np.array([[0, 1], [1, 0]])
        for qubit.Qubit in self.qubit_system:
            result = np.add(result, (qubit.Qubit.calculate_frequency() / 2) * pauli_z)
            coupled_list = qubit.Qubit.get_coupled_list()
            for key in coupled_list:
                result = np.add(result, (coupled_list.get(key) * (np.multiply(pauli_x, pauli_x))))
        print(result)
