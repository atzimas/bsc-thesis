---
title: Implementing a Quantum Arithmetic Logic Unit using the Qiskit SDK
author: Athanasios Tzimas
toc: true
toc-title: Overview
theme: Madrid
header-includes:
- \usepackage{amsmath}
- \usepackage{amssymb}
- \usepackage{braket}
---

# Mathematical Elements of Quantum Computing

## Dirac Notation
* $\vec{u}=u_x\hat{i}+u_y\hat{j}+u_z\hat{k}=\begin{bmatrix}u_x\\ u_y\\ u_z\end{bmatrix}\rightarrow\ket{u}=\begin{bmatrix}u_1\\ u_2\\ \vdots\\ u_i\end{bmatrix},\ket{u}\in\mathbb{V}^n$
* Dual space $\mathbb{V}^{n\star}$ of $\mathbb{V}^n$ where:
$$\bra{u}=\begin{bmatrix}u_1^\star&\hdots&u_n^\star\end{bmatrix}=\begin{bmatrix}u_1\\ \vdots\\ u_n\end{bmatrix}^\dag$$

## Hilbert Space
* Inner product:
$$ \braket{u|v}=\begin{bmatrix}u_1^\star&\hdots&u_n^\star\end{bmatrix}\times\begin{bmatrix}v_1\\ \vdots\\ v_n\end{bmatrix}\text{ where }\ket{u},\ket{u}\in\mathbb{V}^n$$
* Now $\braket{u|v}=\ket{w}\in\mathbb{H}^{\otimes n}$

## Operators
* When applied to a vector, it transforms it.
* $A\ket{\psi}=\ket{\psi^\prime}$
* $\bra{\psi}A=\bra{\psi^\prime}$
* $(A+B)\ket{\psi}=A\ket{\psi}+B\ket{\psi}$
* $(AB)\ket{\psi}=A(B\ket{\psi})$

## Operators
* Operators can be represented as matrices:
$$A=\begin{bmatrix}
    A_{11} & A_{12} & \hdots & A_{1j} \\
    A_{21} & A_{22} & \hdots & A_{2j} \\
    \vdots & \vdots & \ddots & \vdots \\
    A_{i1} & A_{i2} & \hdots & A_{ij} \\
\end{bmatrix}$$
* Example; The *Identity* operator $I$:
$$
I =\begin{bmatrix}
    1 & 0 & \hdots & 0 \\
    0 & 1 & \hdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \hdots & 1 \\
\end{bmatrix},I\ket{\psi}=\ket{\psi}
$$

# Intro to Quantum Mechanics

## The Axioms of Quantum Mechanics
* A mathematical framework.
* Axioms
    * 1st Axiom: The *state vector* of a quantum system.
    $$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}=\begin{bmatrix}\alpha\\\beta\end{bmatrix}\text{ where }\alpha,\beta\in\mathbb{C}$$
    * 2nd Axiom: The time evolution of quantum system.
    $$\ket{\psi(t)}=U(t,t_0)\ket{\psi(t_0)}$$
    * 3rd Axiom: Measurements.
    $$P(i)=|\alpha_i|^2\text{ where }\{\ket{i}\}\in\mathbb{H}$$
    * 4th Axiom: Compount quantum systems.
    $$\ket{\psi} = \ket{\psi_1}\otimes\hdots\ket{\psi_n}=\ket{\psi_1\hdots\psi_n}\text{ where }\psi_n\in\mathbb{H}^{\otimes{n}}$$

# Intro to Quantum Computing

## The Qubit
* Bit: two states, $0$ or $1$ $\rightarrow$ Qubit: a linear combinations of two states
* The *computational basis* vectors: $\ket{0}=\begin{bmatrix}1\\0\end{bmatrix}$ and $\ket{1}=\begin{bmatrix}0\\1\end{bmatrix}$
* $\ket{q}=q_1\ket{0}+q_2\ket{1}$

![Bloch's sphere](images/bloch_sphere.pdf){ width=40%, height=40% }

# Quantum Gates

## Single-qubit Gates
* NOT/X gate: $X=\begin{bmatrix}0&1\\1&0\end{bmatrix}$

![The NOT gate diagram](images/x_gate.pdf)

* Hadamard gate: $H=\frac{1}{\sqrt{2}}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$

![The Hadamard gate diagram](images/hadamard_gate.pdf)

## Multi-qubit Gates
* Controlled-NOT gate: $CX=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\\\end{bmatrix}$

![The Controlled-NOT gate diagram](images/cx_gate.pdf)

## Multi-qubit Gates
* Controlled-CNOT gate

![The Controlled-CNOT gate diagram](images/ccx_gate.pdf)

* Swap gate:

![The Swap gate diagram](images/swap_gate.pdf)

## Quantum Circuits

* An example Quantum circuit

![The Quantum Half Adder circuit](images/half_adder.pdf)

# The Arithmetic Logic Unit

## The Unit
![The Arithmetic Logic Unit diagram](images/alu.pdf){ width=50%, height=50% }

## Operations and Opcodes
![An example opcode table of an ALU](images/alu_opcode_table.pdf){ width=50%, height=50% }

## An example ALU

![An example ALU that implements the opcode table (Fig.9)](images/alu_design.pdf){ width=70%, height=70% }

# A short guide to the Qiskit SDK

## Qiskit
* A Python library with "ready-to-use" software components to construct and simulate Quantum circuits
* Easy to install and use (using `pip`)
* Relatively new library (just hit version 1.0!)
* `QuantumCircuit, QuantumRegisters, ClassicalRegisters`

## Qiskit (cont.)
* Gates are implemented as class methods of the `QuantumCircuit` class
    * `.x()` for the NOT gate
    * `.h()` for the Hadamard gate
    * `.cx()` for the CNOT gate
    * `.ccx()` for the CCNOT gate
    * `.swap()` for the SWAP gate

## IBM Quantum Platform
* A Web API written in Python to send jobs to either a real Quantum Computer or a simulator
* Very easy to use and setup (Get an API Token $\rightarrow$ Setup and account in a Python enviroment $\rightarrow$ Profit!)
* Retrieve state probability counts anytime using the service
* Free (up to 10 compute minutes per month for a free account)

## Pass Managers and Transpilers
* IBM's quantum computers require ISA compatible circuits
* Easy: use the `QiskitRuntimeService.least_busy()` and `generate_preset_pass_manager()` methods from the Qiskit Runtime and Qiskit libraries

# Implementing the Quantum ALU

## Qiskit Implementation of the Adder-Subtractor circuit

![The Quantum Full Adder circuit](images/full_adder.pdf)

## Qiskit Implementation of the Adder-Subtractor circuit

* Import the appropriate classes
```py
from qiskit import QuantumCircuit, QuantumRegister
```
* Create the circuit
```py
qfa = QuantumCircuit(4)
qfa.ccx(0, 1, 3)
qfa.cx(0, 1)
qfa.ccx(1, 2, 3)
qfa.cx(1, 2)
qfa.cx(0, 1)
qfa = qfa.to_gate() # create the custom gate for later
```

## Qiskit Implementation of the Adder-Subtractor circuit
$$
A-B=A+(\lnot B)+1
$$

![The Quantum Adder-Subtractor circuit](images/quantum_adder_subtractor.pdf){ width=80%, height=65% }

## Qiskit Implementation of the Adder-Subtractor circuit
$$
A-B=A+(\lnot B)+1
$$

* Create the Adder-Subtractor circuit (for 2-qubit inputs)
```py
ctrl = QuantumRegister(1, 'ctrl')
a = QuantumRegister(2, 'a')
b = QuantumRegister(2, 'b')
cin = QuantumRegister(2, 'out')
overflow = QuantumRegister(1, 'overflow')
qas = QuantumCircuit(ctrl, a, b, cin, overflow)
```

* Get the 2s complement of $B$
```py
for i in range(2):
    qas.cx(ctrl, b[i])
qas.cx(ctrl, cin[0])
```

## Qiskit Implementation of the Adder-Subtractor circuit
$$
A-B=A+(\lnot B)+1
$$

* Append the Quantum Full Adder gate to the circuit for $n=2$ iterations
```py
for i in range(2):
    qas.append(qfa, [a[i], b[i], cin[i], overflow[:]])
    if i+1 > 2:
        qas.swap(cin[1+1], overflow)
```

* Revert $B$ to its initial state $\lnot(\lnot B)=B$
```py
for i in reversed(range(2)):
    qas.cx(ctrl, b[i])
```

## Qiskit Implementation of the Integer Multiplier

![An example of binary multiplication of 2-bit "wide" integers](images/multiplication_example.pdf){ width=20%, height=20%}

![The Integer Multiplier Circuit](images/multiplier.pdf){ width=50%, height=40%}

## Qiskit Implementation of the Integer Multiplier

* Initialize the circuit
```py
from qiskit import QuantumCircuit, QuantumRegister
a = QuantumRegister(2, 'a')
b = QuantumRegister(2, 'b')
out = QuantumRegister(8, 'out')
qmul = QuantumCircuit(a, b, out)
```
* Compute the partial products
```py
k = 0
for i in range(2):
    for j in range(2):
        qmul.ccx(a[i], b[j], out[k])
        k += 1
```

## Qiskit Implementation of the Integer Multiplier

* Append the Quantum Full Adder and produce the final products
```py
qmul.append(qfa, (out[1], out[2], out[4], out[5]))
qmul.append(qfa, (out[3], out[5], out[6], out[7]))
```

* Output is stored at register locations: `out[0]`, `out[4]`, `out[6]`, `out[7]`

## Qiskit Implementation of the Integer Comparator

![The Integer Comparator circuit](images/nko_comparator.pdf)

## Qiskit Implementation of the Integer Comparator
* Create the $S$ gate
```py
s = QuantumCircuit(4, name="S")
s.cx(0, 2)
s.ccx(0, 2, 3)
s.cx(1, 2)
s.ccx(1, 2, 3)
s = s.to_gate()
```

![](images/sgate.pdf)
![](images/sgate_raw.pdf)

## Qiskit Implementation of the Integer Comparator
* Create the $S^\dag$ quantum gate
```py
sdag = QuantumCircuit(4, name="Sdag")
sdag.ccx(1, 2, 3)
sdag.cx(1, 2)
sdag.ccx(0, 2, 3)
sdag.cx(0, 2)
sdag = sdag.to_gate()
```

![](images/sdaggate.pdf)
![](images/sdaggate_raw.pdf)

## Qiskit Implementation of the Integer Comparator
* Apply the S gate iteratively for $n=2$ qubits
```py
for i in range(2):
    circuit.append(s, (aux[i], a[i], b[i], aux[i+1]))
```
* `if A = B then A - B = 0`
```py
from qiskit.circuit.library import MCXGate
circuit.append(MCXGate(n, ctrl_state=0), (b[:] + eq[:]))
```
* `if A >= B then MSB(B) is set`
```py
circuit.cx(b[-1], gl)

```

## Qiskit Implementation of the Integer Comparator
* Finally, un-compute B to reset it to its initial state using the $S^\dag$ gate
```py
for i in reversed(range(2)):
    circuit.append(sdag, (aux[i], a[i], b[i], aux[i+1]))
```

# The Complete Picture
## QALU Operations

![The opcode table of the proposed QALU](images/opcode_table.pdf)

## The complete Quantum ALU

![The complete circuit of the Quantum ALU](images/qalu_complete.pdf)

## Experimental Results on a Real Quantum Computer
### Adder-Subtractor Sub-Unit
![The probability count of adding $3+2$ using the Quantum Arithmetic Logic Unit, executed on the Aer Simulator](images/adder_subtractor_aer_result.pdf){ width=60%, height=60% }

## Experimental Results on a Real Quantum Computer
### Adder-Subtractor Sub-Unit
![The probability counts of adding $3+2$ using the Quantum Arithmetic Logic Unit, executed on the IBM Osaka Quantum Computer](images/adder_subtractor_ibmq_result.pdf){ width=60%, height=60% }

## Experimental Results on a Real Quantum Computer
### Integer Multiplier Sub-Unit
![The probability count of multiplying $2\times 2$ using the Quantum Arithmetic Logic Unit, executed on the Aer Simulator](images/multiplier_aer_result.pdf){ width=60%, height=60% }

## Experimental Results on a Real Quantum Computer
### Integer Multiplier Sub-Unit
![The probability count of multiplying $2\times 2$ using the Quantum Arithmetic Logic Unit, executed on the IBM Kyoto Quantum Computer](images/multiplier_ibmq_result.pdf){ width=60%, height=60% }

## Experimental Results on a Real Quantum Computer
### Integer Comparator Sub-Unit
![The probability count of comparing $A=1$ to $B=1$ using the Quantum Arithmetic Logic Unit, executed on the Aer Simulator](images/nko_cmp_aer_result.pdf){ width=60%, height=60% }

## Experimental Results on a Real Quantum Computer
### Integer Comparator Sub-Unit
![The probability count of comparing $A=1$ to $B=1$ using the Quantum Arithmetic Logic Unit, executed on the IBM Osaka Quantum Computer](images/nko_cmp_ibmq_result.pdf){ width=60%, height=60% }