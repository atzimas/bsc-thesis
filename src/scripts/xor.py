from qiskit import QuantumCircuit, QuantumRegister

a = QuantumRegister(1, name="a")
b = QuantumRegister(1, name="b")
circuit = QuantumCircuit(a, b)

circuit.cx(a, b)

from qiskit.visualization import circuit_drawer

circuit_drawer(circuit, filename="xor.pdf", output="latex")