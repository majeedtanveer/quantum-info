The Y Gate is as follows:

$Y = \begin{pmatrix}  0 & -i \\  i & 0  \end{pmatrix}$
## Identities

The Y Gate can be built from itself and [[Hadamard-Gate|H-Gates]]:

$-Y = HYH$

## Qiskit

```python
qc.y(qr[0]) # execute Y-gate on qubit 0
```

### Eigenstates
$|+ \rangle_i = \frac{1}{\sqrt{2}} (|0\rangle + i|1 \rangle)$
$|- \rangle_i = \frac{1}{\sqrt{2}} (|0\rangle - i|1 \rangle)$