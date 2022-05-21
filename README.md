# OQC
Python developed console program, designed to take qubit frequency and coupling information and output the hamiltonian.

To run, execute the main.py file using the following command in your terminal, from within the OQC direcotory:

python3 main.py

You will be greeted with the following message, explaining how to use the software:

          "Please define each qubit, in turn, on a separate line using the following format:"
          "<type> <frequency> [parameters]. Each value should be separated by a space."
          "Use the return key to enter another qubit. Once all qubits have been entered"
          "type 'couple' to enter couple mode and define the couplings for each qubit."
          "TYPES:"
          "       s         Standard Qubit"
          "       c         Coaxmon"
          "       r         Rectanglemon"
          "       couple    Enter couple mode"
          "       frequency Enter frequency mode"
          "       end       End the programme"
          "       help      Display help text"
          "FREQUENCY:"
          "       floating point number"
          "PARAMETERS:"
          "       center_radius inner_radius outer_radius          Coaxmon parameter list"
          "       length_1 height_1 length_2 height_2              Rectanglemon parameter list"
          "EXAMPLE INPUT:"
          "       c 10.0 4.2 5.5 6.0"
