The Ry Gate is one of the [[Rotation Gates]]. The Ry gate is a single-qubit rotation through angle $\varphi$ (radians) around the y-axis.

$R_y(\varphi) = \begin{pmatrix}  \cos\left(\frac{\varphi}{2}\right) & -\sin\left(\frac{\varphi}{2}\right) \\  \sin\left(\frac{\varphi}{2}\right) & \cos\left(\frac{\varphi}{2}\right)  \end{pmatrix}$

## Qiskit

```python
version 1.0
qubits 2
H q[0] # execute Hadamard gate on qubit 0
Ry q[0],1.78 # Rotation of 1.78 radians around the y-axis on qubit 0
```