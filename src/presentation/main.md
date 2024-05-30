---
title: Implementing a Quantum Arithmetic Logic Unit using the Qiskit SDK
author: Athanasios Tzimas
header-includes:
- \usepackage{amsmath}
- \usepackage{amssymb}
- \usepackage{braket}
---

# Intro to Quantum Mechanics
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

# Mathematical Elements of Quantum Computing
## Dirac Notation
* $\vec{u}=u_x\hat{i}+u_y\hat{j}+u_z\hat{k}=\begin{bmatrix}u_x\\ u_y\\ u_z\end{bmatrix}\rightarrow\ket{u}=\begin{bmatrix}u_1\\ u_2\\ \vdots\\ u_i\end{bmatrix},\ket{u}\in\mathbb{V}^n$
* Dual space $\mathbb{V}^{n\star}$ of $\mathbb{V}^n$ where:
$$\bra{u}=\begin{bmatrix}u_1^\star&\hdots&u_n^\star\end{bmatrix}=\begin{bmatrix}u_1\\ \vdots\\ u_n\end{bmatrix}^\dag$$

# Mathematical Elements of Quantum Computing
## Hilbert Space
* Inner product:
$$ \braket{u|v}=\begin{bmatrix}u_1^\star&\hdots&u_n^\star\end{bmatrix}\times\begin{bmatrix}v_1\\ \vdots\\ v_n\end{bmatrix}\text{ where }\ket{u},\ket{u}\in\mathbb{V}^n$$

## Operators
* When applied to a vector, it transforms it.
* $A\ket{\psi}=\ket{\psi^\prime}$
* $\bra{\psi}A=\bra{\psi^\prime}$
* $(A+B)\ket{\psi}=A\ket{\psi}+B\ket{\psi}$
* $(AB)\ket{\psi}=A(B\ket{\psi})$

# Mathematical Elements of Quantum Computing
## Operators (cont.)
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

# The Qubit
* Bit: two states, $0$ or $1$ $\rightarrow$ Qubit: a linear combinations of two states
* The *computational basis* vectors: $\ket{0}=\begin{bmatrix}1\\0\end{bmatrix}$ and $\ket{1}=\begin{bmatrix}0\\1\end{bmatrix}$
* $\ket{q}=q_1\ket{0}+q_2\ket{1}$

![Bloch's sphere](images/bloch_sphere.pdf){ width=40%, height=40% }

# Quantum Gates
## Single-qubit Gates
* X gate: $X=\begin{bmatrix}0&1\\1&0\end{bmatrix}$

![The X gate diagram](images/x_gate.pdf)

* Hadamard gate: $H=\frac{1}{\sqrt{2}}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$

![The Hadamard gate diagram](images/hadamard_gate.pdf)

# Quantum Gates
## Multi-qubit Gates
* Controlled-X gate: $CX=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\\\end{bmatrix}$

![The Controlled-X gate diagram](images/cx_gate.pdf)

# Quantum Gates
## Multi-qubit Gates
* Controlled-CX gate

![The Controlled-CX gate diagram](images/ccx_gate.pdf)

* Swap gate:

![The Swap gate diagram](images/swap_gate.pdf)