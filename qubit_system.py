from qubit import Qubit
from coaxmon_qubit import Coaxmon
from rectanglemon_qubit import Rectanglemon
from hamiltonian import Hamiltonian


# A qubit system consists of any number of qubits and contains its hamiltonian.
class QubitSystem:
    qubits = []
    h = None

    def create_standard_qubit(self, frequency):
        self.qubits.append(Qubit(frequency))

    def create_coaxmon_qubit(self, frequency, center, inner, outer):
        self.qubits.append(Coaxmon(frequency, center, inner, outer))

    def create_rectanglemon_qubit(self, frequency, length_1, height_1, length_2, height_2):
        self.qubits.append(Rectanglemon(frequency, length_1, height_1, length_2, height_2))

    def update_coupling(self, qubit_1, qubit_2, strength):
        self.qubits[qubit_1 - 1].update_coupling(self.qubits[qubit_2 - 1], strength)

    def create_hamiltonian(self):
        self.h = Hamiltonian(self.qubits)
        self.h.print_hamiltonian()
