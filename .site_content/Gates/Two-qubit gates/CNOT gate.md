The CNOT gate (or Controlled-NOT gate) is two-qubit operation, where the first qubit is usually referred to as the control qubit and the second qubit as the target qubit. Expressed in basis states, the CNOT gate:

- leaves the control qubit unchanged and performs a Pauli-X gate on the target qubit when the control qubit is in state $\ket{1}$;
- leaves the target qubit unchanged when the control qubit is in state $\ket{0}$.
- is equivalent to adding the value of the control qubit qubit to the value of the second qubit, and writing the result into the second qubit
	- $\ket{a,b} \overset{CNOT}\longrightarrow \ket{a,b \oplus a}$

$CNOT = \begin{pmatrix}  1 & 0 & 0 & 0 \\  0 & 1 & 0 & 0 \\  0 & 0 & 0 & 1 \\  0 & 0 & 1 & 0 \end{pmatrix}$
![[Images/Pasted image 20250723104636.png|300]]

## Qiskit

```python
qc.cx(qr[0], qr[1]) # execute CNOT gate with control qubit 0 and target qubit 1
```