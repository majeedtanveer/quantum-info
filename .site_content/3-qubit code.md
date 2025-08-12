### Idea
Distribute an arbitrary quantum state $|\psi \rangle=\alpha|0\rangle+\beta|1\rangle$ over an entangled state of $n=3$ physical qubits.
$\Rightarrow$ Encode $k=1$ logical qubit:
Basis states or **codewords** $|0\rangle_L=|000\rangle, |1\rangle_L=|111\rangle$ span the **codespace**, a subspace of the Hilbert space, in which arbitrary logical superpositions live:
$|\psi\rangle_L=\alpha|0\rangle_L+|1\rangle_L=\alpha|000\rangle + \beta|111\rangle$

$$
    \begin{equation}
        f(t) = \mu_1 f_1(t) + \mu_2 f_2(t).
    \end{equation}
$$


### Algorithm Steps
1. Encoding: quantum circuit $U_\text{enc}: |\psi\rangle\rightarrow|\psi\rangle_L$
	Use two [[Ancilla]] qubits initialized in $|0\rangle$:
	![[Images/Pasted image 20250810181304.png|400]]
	$|\psi\rangle|0\rangle|0\rangle\rightarrow|\psi\rangle_L$
2.  Possible occurrence of errors:
	E.g. bit flip error on qubit 1: $X_1$
	$|\psi\rangle_L = \alpha|000\rangle + \beta|111\rangle\xrightarrow{X_1}\alpha|100\rangle+\beta|011\rangle$
	How can we find out about the error that occurred on the system?
	- Direct measurement of all qubits would collapse the state into $|100\rangle$ or $|011\rangle$: Information about $\alpha$ and $|\beta\rangle$ would be lost.
	- Solution: we realize an [[indirect measurement]], using additional ancilla qubits and syndromes (measurements) $M_z^{(1)}$ and $M_z^{(2)}$

### Circuit implementation

![[Images/Pasted image 20250811152057.png]]

### Errors

| Error | $M_z^{(1)}(Z_1Z_2)$ | $M_z^{(2)}(Z_2Z_3)$ | Correction |
| ----: | :------------------ | :------------------ | ---------- |
| $X_1$ | -1                  | +1                  | $X_1$      |
| $X_2$ | -1                  | -1                  | $X_2$      |
| $X_3$ | +1                  | -1                  | $X_3$      |
$\Rightarrow$ No information gained about the encoded state ($\alpha$ and $\beta$ coefficients)
$\Rightarrow$ Strategy corrects up to one $X$-error on any qubit
2 simultaneous errors induce a logical bit flip error
Example $X_1X_2$ error:
$M_z^{(1)}=+1,M_z^{(2)}=-1$
$\alpha|110\rangle + \beta|001\rangle \xrightarrow{X_3} \alpha|111\rangle + \beta|000\rangle=\alpha|1\rangle_L + \beta|0\rangle_L$
$\Rightarrow$ QER fails
For 3 simultaneous errors $X_1X_2X_3$: is not detectable and directly induces a logical bit flip error.
Phase flip errors, e.g. $Z_1$ also is undetectable and directly induces a logical phase flip error.
$\Rightarrow$ 3-qubit code is not a **complete** code.

#### Robustness
The probability to correct error(s) is the following:
$p_\text{corr}=(1-p)^3+3p(1-p)^2=1-3p^2+2p^3$
![[Images/Pasted image 20250811154800.jpg]]

Here for $p<\frac{1}{2}$, $p_\text{corr} > 1-p$, thus better protection offered by 3-qubit code.

### Stabilizer code
The 3-qubit code can be formulated as a stabilizer QEC code:
$$
\left.

\begin{array}{l}

S_1=Z_1Z_2 \\

S_2=Z_2Z_3

\end{array}

\right\} \quad S_i|\psi\rangle_L=|\psi\rangle_L
$$
![[Images/Pasted image 20250811163959.png]]

The logical operators are $Z_L=Z_1Z_2Z_3$ and $X_L=X_1X_2X_3$
