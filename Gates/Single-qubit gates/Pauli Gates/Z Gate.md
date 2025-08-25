The Z Gate is as follows:

$Z = \begin{pmatrix}  1 & 0 \\  0 & -1  \end{pmatrix}$

## Identities

The Z Gate can be built from the [[X Gate]] and [[Hadamard-Gate|Hadamard-Gates]]:

$Z = HXH$

It can also be built from [[Rz gate]]:
$Z=iR_z(\pi)$

The Z-Gate can also be built from the [[T-Gate]]:
$Z = T^4= iR_z(\pi)$

## Qiskit

```python
qc.z(qr[0]) # execute Z-gate on qubit 0
```

### Eigenstates
$|0 \rangle$
$|1 \rangle$


