The Rx gate is one of the [[Rotation Gates]]. The Rx gate is a single-qubit rotation through angle $\varphi$ (radians) around the x-axis.

$R_x(\varphi) = \begin{pmatrix}  \cos\left(\frac{\varphi}{2}\right) & -i\sin\left(\frac{\varphi}{2}\right) \\  -i\sin\left(\frac{\varphi}{2}\right) & \cos\left(\frac{\varphi}{2}\right)  \end{pmatrix}$

## Identities
$R_x(\pi/4)=HTH=HR_z(\pi/4)H$

## Qiskit

```python
version 1.0
qubits 2
H q[0] # execute Hadamard gate on qubit 0
Rx q[0],-1.12  # rotation of -1.12 radians on qubit 0
```