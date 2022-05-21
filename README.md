# OQC
Python developed console program, designed to take qubit frequency and coupling information and output the hamiltonian.

To run, execute the main.py file using the following command in your terminal:

python3 main.py

You will be greeted with the following message, explaining how to use the software:

          "Please define each qubit, in turn, on a separate line using the following format: "
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
          "       c 10.0 4.2 5.5 6.0"
