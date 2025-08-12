An indirect measurement can be achieved by the following construction:
Consider a unitary (n-qubit)operator $U$ with eigenvalues $\pm 1$.
![[Images/Pasted image 20250811142111.png|500]]
$$
\begin{align}
U \lvert 0 \rangle \lvert \psi \rangle &= \lvert 0 \rangle \lvert \psi \rangle \quad \text{(no error)} \\
U \lvert 0 \rangle \lvert \psi \rangle &= -\lvert 0 \rangle \lvert \psi \rangle \quad \text{(error)} \\
\lvert 0 \rangle \lvert \psi \rangle &\xrightarrow{H} \frac{1}{\sqrt{2}}(\lvert 0 \rangle + \lvert 1 \rangle)\lvert \psi \rangle \\
&\xrightarrow{\text{CU}} \frac{1}{\sqrt{2}}(\lvert 0 \rangle\lvert \psi \rangle + \lvert 1 \rangle U\lvert \psi \rangle) \\
&\xrightarrow{H} \frac{1}{2}[(\lvert 0 \rangle + \lvert 1 \rangle)\lvert \psi \rangle + (\lvert 0 \rangle - \lvert 1 \rangle)U\lvert \psi \rangle] \\
&= |0\rangle\frac{1}{2}(\mathbb{I}+U)\lvert \psi \rangle + |1\rangle\frac{1}{2}(\mathbb{I}-U)\lvert \psi \rangle \\
&=|0\rangle P_+ |\psi\rangle+|1\rangle P_- |\psi\rangle
\end{align}

$$
$P_\pm= \frac{1}{2}(1\pm U)$ are projection operators on the $\pm1$ eigenspaces of $U$
$\rightarrow$ Realizes a measurement of $U$
The projectors share a common eigenbasis with U by construction and commute. The states of the codespace span the $P_+$ subspace and thus always the $|0\rangle$-state is measured with certainty. The elements outside the codespace (errors) span the $P_-$ subspace and thus always the $|1\rangle$-state is measured.

#### Example
In the 3-qubit code for unitary $U=Z_1Z_2$ the following circuit can be used to do an indirect measurement:
![[Images/Pasted image 20250811151031.png]]