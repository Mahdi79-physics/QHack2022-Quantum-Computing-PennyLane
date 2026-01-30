import pennylane as qml
from pennylane import numpy as np

def compare_circuits(angles):
   

    # QHACK #

    dev = qml.device('default.qubit', wires=2)
    @qml.qnode(dev)
    def circuit1(angles):
        qml.RX(angles[0],wires = 0)
        qml.RY(angles[1],wires = 0)
        

        return qml.expval(qml.PauliX(0))

    @qml.qnode(dev)    
    def circuit2(angles):
        qml.RY(angles[1],wires = 1)
        qml.RX(angles[0],wires = 1)
        
        return qml.expval(qml.PauliX(1))

    expectation = np.abs(circuit1(angles) - circuit2(angles))
    return expectation 

        
    
    # QHACK #

angles = [3.79894785 , 0.71678115]
output = compare_circuits(angles)
print(output)
