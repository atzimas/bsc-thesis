from qiskit import QuantumCircuit, QuantumRegister

a = QuantumRegister(2, name="a")
b = QuantumRegister(2, name="b")
pp = QuantumRegister(4, name="pp")
o = QuantumRegister(1, name="o")

circuit = QuantumCircuit(a, b, pp, o)

k = 0
for i in a:
    for j in b:
        circuit.ccx(i, j, pp[k])
        k += 1

adder = QuantumCircuit(4, name="Full Adder")
adder.ccx(0, 1, 3)
adder.cx(0, 1)
adder.ccx(1, 2, 3)
adder.cx(1, 2)
adder.cx(0, 1)
adder = adder.to_gate()

circuit.append(adder, (pp[1], pp[2], pp[3], o))

from qiskit.visualization import circuit_drawer

circuit_drawer(circuit, filename="multiplier.pdf", output="latex")