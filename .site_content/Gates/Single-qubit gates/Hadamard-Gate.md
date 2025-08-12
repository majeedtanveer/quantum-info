The Hadamard-Gate is as follows:

$H = \frac{1}{\sqrt{2}} \begin{pmatrix}  1 & 1 \\  1 & -1  \end{pmatrix}$

The Hadamard Gate maps the Z-eigenstates to the X-Eigenstates and vice versa. The Hadamard Gate is unitary and hermitian.
## Identities

The Hadamard-Gate can be built from [[Rotation Gates]] like this:
$H = R_z(\pi) \cdot R_y(-\frac{\pi}{2})$
$H = R_x(\pi) \cdot R_y(\frac{\pi}{2})$

## Common Operations
$H \ket{0} = \frac{1}{\sqrt{2}} ( \ket{0} + \ket{1}) = \ket{+}$
$H \ket{1} = \frac{1}{\sqrt{2}} ( \ket{0} - \ket{1}) = \ket{-}$
Since $H^2= \mathbb{1}$:
$H \ket{+} = \ket{0}$
$H \ket{-} = \ket{1}$

With n-Hadamard gates on $|0 \rangle$ one can build an equal-weight superposition of all basis states on n qubits
$H^{\otimes n} |0 \rangle= \frac{1}{\sqrt{2^n}} \sum_{i \in \{0,1\}^n} |i \rangle$
In general applying $H^{\otimes n}$ to an arbitrary basis state $|i \rangle$ with $i \in \{ 0,1\}^n$ the following holds:
$H^{\otimes n} |i \rangle = \frac{1}{\sqrt{2^n}} \sum_{j \in \{0,1\}^n} (-1)^{i \cdot j} |j \rangle$,
with $i \cdot j = \sum_{k=1}^n i_n j_n$ as the inner product of the n-bit strings $i,j \in \{0,1\}^n$
Example:
$$
\begin{align}
H^{\otimes 2} |01 \rangle &=  \frac{1}{\sqrt{2^n}} \sum_{j \in \{0,1\}^n} (-1)^{01 \cdot j} |j \rangle\\
&= \frac{1}{2}((-1)^{01 \cdot 00} | 00 \rangle + (-1)^{01 \cdot 01} | 01 \rangle + (-1)^{01 \cdot 10} | 10 \rangle + (-1)^{01 \cdot 11} | 11 \rangle) \\
&= \frac{1}{2} (|00\rangle - |01\rangle + |10\rangle - |11\rangle) \\
&= \frac{1}{\sqrt{2}} (|0 \rangle + |1 \rangle ) \otimes \frac{1}{\sqrt{2}} (|0 \rangle - |1 \rangle)
\end{align}
$$
## Qiskit

```python
qc.h(qr[0]) # execute H-gate on qubit 0
```