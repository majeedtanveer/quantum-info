It is a $ [[9,1,1]] $ code based on the concatenation of the 3-qubit repetition code in the [[Z Gate|Z-]] and [[X Gate|X-Basis]]:
![[Pasted image 20250811180916.png]]
Explicit form of logical state:
\[
\begin{align*}
|\psi\rangle_L &=\alpha(|000\rangle+|111\rangle)(|000\rangle+|111\rangle)(|000\rangle+|111\rangle)/\sqrt{8} \\
&+ \beta(|000\rangle-|111\rangle)(|000\rangle-|111\rangle)(|000\rangle-|111\rangle)/\sqrt{8} \\
&= \alpha|0\rangle_L+\beta|1\rangle_L
\end{align*}
\]
- Bit flip errors $X_i$ are corrected by measuring $Z$-stabilizers: $\{Z_1Z_2,Z_2Z_3,Z_4Z_5,Z_5Z_6,Z_7Z_8,Z_8Z_9\}$
- Phase flip errors $Z_i$ are detected by measuring $X$-stabilizers $\{X_1X_2X_3X_4X_5X_6, X_4X_5X_6X_7X_8X_9\}$
Properties:
- Complete code: arbitrary error correctable
- Degenerate code: several errors (e.g. $Z_1$ and $Z_2$ and $Z_3$) have the same effect on logical states.
- Correction works if: correction attempt+ error=identity or a stabilizer $S$
- not-perfect/optimal: [[Quantum Hamming Bound]] says $\sum_{j=0}^1\binom{9}{j}3^j\cdot2^1 \leq 2^9 \Leftrightarrow 28 \leq 256$, thus the stabilizers span a subspace higher than needed in theory