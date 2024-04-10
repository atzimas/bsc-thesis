from qiskit import QuantumCircuit, QuantumRegister

a = QuantumRegister(1, name="a")
b = QuantumRegister(1, name="b")
cin = QuantumRegister(1, name="cin")
o = QuantumRegister(1, name="o")

circuit = QuantumCircuit(a, b, cin, o)

from qiskit.visualization import circuit_drawer

circuit.ccx(a, b, o)
circuit_drawer(circuit, filename="full_adder_step1.pdf", output="latex")
circuit.cx(a, b)
circuit_drawer(circuit, filename="full_adder_step2.pdf", output="latex")
circuit.ccx(b, cin, o)
circuit_drawer(circuit, filename="full_adder_step3.pdf", output="latex")
circuit.cx(b, cin)
circuit_drawer(circuit, filename="full_adder_step4.pdf", output="latex")
circuit.cx(a, b)

circuit_drawer(circuit, filename="full_adder.pdf", output="latex")