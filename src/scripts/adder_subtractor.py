from qiskit import QuantumCircuit, QuantumRegister

ctrl = QuantumRegister(1, name="ctrl")
a = QuantumRegister(1, name="a")
b = QuantumRegister(1, name="b")
cin = QuantumRegister(1, name="cin")
o = QuantumRegister(1, name="o")

circuit = QuantumCircuit(ctrl, a, b, cin, o)

circuit.cx(ctrl, b)
circuit.cx(ctrl, cin)

adder = QuantumCircuit(4, name="Full Adder")
adder.ccx(0, 1, 3)
adder.cx(0, 1)
adder.ccx(1, 2, 3)
adder.cx(1, 2)
adder.cx(0, 1)
adder = adder.to_gate()

circuit.append(adder, (a[:] + b[:] + cin[:] + o[:]))

from qiskit.visualization import circuit_drawer

circuit_drawer(circuit, filename="adder_subtractor.pdf", output="latex")