import pennylane as qml
from pennylane import numpy as np

def matrix_norm(mixed_state, pure_state):
    return np.sum(np.abs(mixed_state - np.outer(pure_state, np.conj(pure_state))))


def compare_circuits(num_wires, params):
    """Function that returns the matrix norm between the mixed- and pure-state versions of the same state.

    Args:
        - num_wires (int): The number of qubits / wires
        - params (list(np.ndarray)): Two arrays with num_wires floats that correspond to angles of y-rotations
        for each wire

    Returns:
        - mat_norm (float): The matrix one-norm
    """

    # QHACK #
    # define devices
    dev1 = qml.device('default.qubit', wires = num_wires)
    dev2 = qml.device('default.mixed', wires = num_wires)
    # add a decorator here
    @qml.qnode(dev1)
    def pure_circuit():
        """A circuit that contains `num_wires` y-rotation gates.
        The argument params[0] are the parameters you should use here to define the y-rotations.
        
        Returns:
            - (np.tensor): A state vector
        """
        for i in range(0 , num_wires):
            qml.RY(params[0][i] , wires = i)
        
        # create the circuit here
        return qml.state()

    # add a decorator here
    @qml.qnode(dev2)
    def mixed_circuit():
        """A circuit that contains `num_wires` y-rotation gates.
        The argument params[1] are the parameters you should use here to define the y-rotations.

        Returns:
            - (np.tensor): A density matrix
        """
        for i in range(0 , num_wires):
            qml.RY(params[1][i] , wires = i)
        # create the circuit here
        return qml.state()

    # QHACK #

    # DO NOT MODIFY any of the next lines in this scope
    mixed_state = mixed_circuit()
    pure_state = pure_circuit()
    mat_norm = matrix_norm(mixed_state, pure_state)

    return mat_norm


inputs1 = [2, 0.17085641, 4.69202289, 0.4478956, 3.69402896]
num_wires = int(inputs1[0])
l = int(len(inputs1[1:]) / 2)
params = [
    np.array(inputs1[1 : (l + 1)], dtype=float),  # for pure circuit
    np.array(inputs1[(l + 1) :], dtype=float),  # for mixed circuit
    ]

output = compare_circuits(num_wires, params)
print(f"{output:.6f}")


inputs2 = [4, 2.1051399, 5.02920013, 1.48450097, 4.06791362, 5.19513356, 0.65491091, 3.0127959, 4.03855719]

num_wires = int(inputs2[0])
l = int(len(inputs2[1:]) / 2)
params = [
    np.array(inputs2[1 : (l + 1)], dtype=float),  # for pure circuit
    np.array(inputs2[(l + 1) :], dtype=float),  # for mixed circuit
    ]

output = compare_circuits(num_wires, params)
print(f"{output:.6f}")
