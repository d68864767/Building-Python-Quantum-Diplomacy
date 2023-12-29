# main.py

# Importing required libraries
from quantum_diplomacy import QuantumDiplomacy

def main():
    # Create an instance of QuantumDiplomacy
    quantum_diplomacy = QuantumDiplomacy()

    # Run the QuantumDiplomacy
    quantum_state = quantum_diplomacy.run()

    # Print the quantum state
    print(quantum_state)

if __name__ == "__main__":
    main()
