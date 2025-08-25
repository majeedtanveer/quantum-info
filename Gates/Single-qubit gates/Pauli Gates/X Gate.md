The X Gate is as follows:

$X = \begin{pmatrix}  0 & 1 \\  1 & 0  \end{pmatrix}$

## Identities

The X Gate can be built from the [[Z Gate]] and [[Hadamard-Gate|H-Gates]]:

$X = HZH$

## Qiskit

```python
qc.x(qr[0]) # execute X-gate on qubit 0
```

### Eigenstates
$|+ \rangle = \frac{1}{\sqrt{2}} (|0\rangle + |1 \rangle)$
$|- \rangle = \frac{1}{\sqrt{2}} (|0\rangle - |1 \rangle)$