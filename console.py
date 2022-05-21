import parser


def run():
    # Initial message displayed, informing user how to use the program.
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
    # Main loop responsible for maintaining lifecycle of program.
    # Checks if parser is in a finished state along with the mode.
    while not parser.get_finished_state():
        if not parser.get_couple_mode():
            parser.parse_frequencies(input("> "))
        else:
            parser.parse_couple(input("> "))


