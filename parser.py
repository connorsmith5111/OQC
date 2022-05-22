# Parser is responsible for handling the user input.
# It creates a qubit system which it then adds qubits to as it receives dats from the user.
import tokenizer
from qubit_system import QubitSystem

finished = False
couple_mode = False
qubit_system = QubitSystem()


# Function used for parsing during frequency mode.
def parse_frequencies(user_input):
    tokens = tokenizer.tokenize(user_input)
    try:
        if tokens[0].lower() == "s":
            frequency = parse_frequency(tokens[1])
            qubit_system.create_standard_qubit(frequency)
        elif tokens[0].lower() == "c":
            frequency = parse_frequency(tokens[1])
            parameter_list = tokens[2:5]
            if len(parameter_list) < 3:
                print("Three parameters are required for a coaxmon. Please try again.")
            else:
                new_parameter_list = parse_parameters(parameter_list)
                center_radius = new_parameter_list[0]
                inner_radius = new_parameter_list[1]
                outer_radius = new_parameter_list[2]
                qubit_system.create_coaxmon_qubit(frequency, center_radius, inner_radius, outer_radius)
        elif tokens[0].lower() == "r":
            frequency = parse_frequency(tokens[1])
            parameter_list = tokens[2:6]
            if len(parameter_list) < 4:
                print("Four parameters are required for a rectanglemon. Please try again.")
            else:
                new_parameter_list = parse_parameters(parameter_list)
                length_1 = new_parameter_list[0]
                height_1 = new_parameter_list[1]
                length_2 = new_parameter_list[2]
                height_2 = new_parameter_list[3]
                qubit_system.create_rectanglemon_qubit(frequency, length_1, height_1, length_2, height_2)
        elif tokens[0].lower() == "end":
            terminate_console()
        elif tokens[0].lower() == "couple":
            enter_couple_mode()
            print("In couple mode. Please write your coupling info")
        elif tokens[0].lower() == "help":
            user_help()
        else:
            print("Please specify the type of qubit.")
    except:
        print("Not a valid input. Please try again.")


# Function used for parsing during couple mode
def parse_couple(user_input):
    tokens = tokenizer.tokenize(user_input)
    try:
        if tokens[0].lower() == "end":
            terminate_console()
        elif tokens[0].lower() == "help":
            user_help()
        elif tokens[0].lower() == "print":
            qubit_system.create_hamiltonian()
            terminate_console()
        elif tokens[0].lower() == "frequency":
            exit_couple_mode()
        else:
            qubit_1 = int(tokens[0])
            qubit_2 = int(tokens[1])
            strength = float(tokens[2])
            qubit_system.update_coupling(qubit_1, qubit_2, strength)

    except:
        print("Not a valid input. Please try again.")


def parse_frequency(token):
    try:
        frequency = float(token)
        return frequency
    except ValueError:
        print("Not a valid input. Please try again.")


def parse_parameters(parameter_list):
    float_parameters = []
    for parameter in parameter_list:
        try:
            float_parameters.append(float(parameter))
        except ValueError:
            print("Not a valid input. Please try again.")
    return float_parameters


def user_help():
    print("Please define each qubit, in turn, on a separate line using the following format:\n "
          "<type> <frequency> [parameters]. Each value should be separated by a space.\n "
          "Use the return key to enter another qubit. Once all qubits have been entered\n "
          "type 'couple' to enter couple mode and define the couplings for each qubit.\n"
          "TYPES:\n"
          "       s         Standard Qubit\n"
          "       c         Coaxmon\n"
          "       r         Rectanglemon\n"
          "       couple    Enter couple mode\n"
          "       frequency Enter frequency mode\n"
          "       end       End the programme\n"
          "       help      Display help text\n"
          "FREQUENCY:\n"
          "       floating point number\n"
          "PARAMETERS:\n"
          "       center_radius inner_radius outer_radius          Coaxmon parameter list\n"
          "       length_1 height_1 length_2 height_2              Rectanglemon parameter list\n"
          "EXAMPLE INPUT:\n"
          "       c 10.0 4.2 5.5 6.0")


def terminate_console():
    global finished
    finished = True


def enter_couple_mode():
    print("Please define each COUPLING, in turn, on a separate line using the following format:\n "
          "<qubit_1> <qubit_2> <weight>. Each value should be separated by a space.\n "
          "Use the return key to enter another coupling. Once all couplings have been entered\n "
          "type 'print' to output the HAMILTONIAN of the system.\n"
          "QUBIT_1:\n"
          "       integer         Qubit label of first qubit i.e 1, 2 or 3\n"
          "QUBIT_2:\n"
          "       integer         Qubit label of the partner qubit being coupled with qubit_1\n"
          "STRENGTH:\n"
          "       floating point number          Coupling strength\n"
          "EXAMPLE INPUT:\n"
          "       1 2 0.5")
    global couple_mode
    couple_mode = True


def exit_couple_mode():
    global couple_mode
    couple_mode = False


def get_finished_state():
    global finished
    return finished


def get_couple_mode():
    global couple_mode
    return couple_mode
