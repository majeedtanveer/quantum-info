The Rz Gate is one of the [[Rotation Gates]]. The Ry gate is a single-qubit rotation through angle $\varphi$ (radians) around the z-axis.

$R_z(\varphi) = \begin{pmatrix}  e^{-i\frac{\varphi}{2}} & 0 \\  0 & e^{i\frac{\varphi}{2}}  \end{pmatrix}$

## Identities
$R_z(\theta)=R_x(\pi/2)R_y(\theta)R_x(-\pi/2)$

## Qiskit

```python
version 1.0
qubits 2
H q[0] # execute Hadamard gate on qubit 0
Rz q[0],-1.12 # rotation around z-axis of -1.12 radians on qubit 0
```