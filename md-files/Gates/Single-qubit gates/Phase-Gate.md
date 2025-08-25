The Phase-Gate S is as follows:

$X = \begin{pmatrix}  1 & 0 \\  0 & i  \end{pmatrix}$

## Identities

The Phase-Gate can be built from the [[T-Gate|T-Gates]]:

$S = T^2$

## Qiskit

```python
qc.s(qr[0]) # execute phase gate on qubit 0
qc.sdg(qr[0]) # execute conjugate transpose of the S gate on qubit 0
```