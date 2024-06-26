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

# What is Quantum Computing ?
* A field of science that studies computing applications on *quantum computers*
* A *quantum computer* is a computing device which uses quantum phonemena to encode, decode, process and transmit information.

# Mathematical Elements of Quantum Computing

## Dirac Notation
* Bra $\bra{\psi}$ & Ket $\ket{\psi}$
* $\ket{\psi}=\psi_1\ket{0}+\psi_2\ket{1}=\begin{bmatrix}\psi_1\\\psi_2\end{bmatrix},\ket{\psi}\in\mathbb{V}^2,\psi_i\in\mathbb{C}$
* $\bra{\psi}=\begin{bmatrix}\psi_1^*&\psi_2^*\end{bmatrix}=\begin{bmatrix}\psi_1\\\psi_2\end{bmatrix}^T,\ket{\psi}\in\mathbb{V}^{2^*},\psi_i\in\mathbb{C}$

* Hilber space; Inner product:
$$ \braket{u|v}=\begin{bmatrix}u_1^\star&\hdots&u_n^\star\end{bmatrix}\times\begin{bmatrix}v_1\\ \vdots\\ v_n\end{bmatrix}\text{ where }\ket{u},\ket{v}\in\mathbb{V}^n$$
* Then: $\braket{u|v}=\ket{w}\in\mathbb{H}^{\otimes n}$

## Operators
* An *operator* is a mathematical object that, when applied on a vector, it transforms it.
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
* Quantum register; $\ket{q}=\ket{q_1}\otimes\ket{q_2}\hdots\otimes\ket{q_n}=\ket{q_1q_2\hdots q_n},\ket{q}\in\mathbb{H}^{\otimes n}$

![Bloch's sphere](images/bloch_sphere.pdf){ width=40%, height=40% }

# The Circuit Model of Quantum Computing

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

![The Swap gate diagram](images/swap_gate.pdf){width=20%, height=20%}

# The Arithmetic Logic Unit
* An *arithmetic and logic unit* is hardware component of a classical
computer whose operative is to compute basic arithmetic operations and logical comparisons.
* Inputs; *opcode* + *general purpose register(s)* + *status register* + etc
* Outpus; *operation output* + *status*

![The Arithmetic Logic Unit diagram](images/alu.pdf){ width=40%, height=40% }

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

## IBM Quantum Platform
* A Web API written in Python to send jobs to either a real Quantum Computer or a simulator
* Very easy to use and setup (Get an API Token $\rightarrow$ Setup and account in a Python enviroment $\rightarrow$ Profit!)
* Pass Managers and Transpilers
    * IBM's quantum computers require ISA compatible circuits
    * Easy: use the `QiskitRuntimeService.least_busy()` and `generate_preset_pass_manager()` methods from the Qiskit Runtime and Qiskit libraries

## Coding a Quantum Circuit
### The Quantum Half Adder circuit
```py
# Instantiation and initialization
from qiskit import QuantumCircuit, QuantumRegister
a = QuantumRegister(1, 'A')
b = QuantumRegister(1, 'B')
o = QuantumRegister(1, 'O')
meas = ClassicalRegister(2, 'meas') # Used for measurements
circuit = QuantumCircuit(a, b, o, meas)

# The algorithm
circuit.ccx(a, b, o)
circuit.cx(a, b)

# Measurements
circuit.measure((b, o), meas)
# Alternatively
circuit.measure_all()
```
## Coding a Quantum Circuit
### The Quantum Half Adder circuit

![The Quantum Half Adder circuit](images/half_adder.pdf)

# Implementing the Quantum ALU


## Qiskit Implementation of the Adder-Subtractor circuit

![The Quantum Full Adder circuit](images/full_adder.pdf)

## Qiskit Implementation of the Adder-Subtractor circuit

![The Quantum Ripple-Carry Adder circuit $n=2$](images/varsized_full_adder_n2.pdf){width=70%, height=70%}


## Qiskit Implementation of the Adder-Subtractor circuit
$$
A-B=A+(\lnot B)+1
$$

![The Quantum Adder-Subtractor circuit](images/quantum_adder_subtractor.pdf){ width=80%, height=65% }

## Qiskit Implementation of the Integer Multiplier
![An example of binary multiplication ($2\times 3$)](images/multiplication_example.pdf){ width=20%, height=20%}

## Qiskit Implementation of the Integer Multiplier
![The Integer Multiplier Circuit](images/multiplier_diagram.pdf){ width=70%, height=70%}

## Qiskit Implementation of the Integer Comparator
![The Integer Comparator circuit](images/nko_comparator.pdf)

## Qiskit Implementation of the Integer Comparator
![](images/sgate.pdf)
![](images/sgate_raw.pdf)

## Qiskit Implementation of the Integer Comparator
![](images/sdaggate.pdf)
![](images/sdaggate_raw.pdf)

# The Complete Picture
## QALU Operations

![The opcode table of the proposed QALU](images/opcode_table.pdf)

## The complete Quantum ALU

![The complete circuit of the Quantum ALU](images/qalu_complete.pdf)

## Experimental Results on a Real Quantum Computer
### Adder-Subtractor Sub-Unit
![The probability count of adding $3-2$ using the Quantum Arithmetic Logic Unit, executed on the Aer Simulator](images/adder_subtractor_aer_result.pdf){ width=60%, height=60% }

## Experimental Results on a Real Quantum Computer
### Adder-Subtractor Sub-Unit
![The probability counts of adding $3-2$ using the Quantum Arithmetic Logic Unit, executed on the IBM Osaka Quantum Computer](images/adder_subtractor_ibmq_result.pdf){ width=60%, height=60% }

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