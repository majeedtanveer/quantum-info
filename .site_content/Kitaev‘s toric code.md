- Most commonly studied and experimentally pursued topological [[Quantum Error Correction|QEC]] code (experimental variant: „surface code“)
- $L \times L$ square lattice with physical qubits located on the edges:
![[Images/Pasted image 20250812101449.jpg]]
- The vertices are a star operator and correspond to the action of the two qubits around them
- All [[Quantum Error Correction#Stabilizer formalism|stabilizers]] mutually commute:
	$[S_Z^{(i)},S_Z^{j}]=[S_X^{(i)},S_X^{j}] \quad \forall i,j$ 
	$[S_X^{(i)},S_Z^{j}]=0 \quad \forall i,j$, because plaquette and vertex operators share zero or two qubits (even number of anticommutes)
- They define the codespace: $S_Z^{(i)}|\psi\rangle_L=S_X^{(j)}|\psi\rangle_L=|\psi\rangle_L$
- Here we consider lattice with periodic boundary conditions, i.e. embedded on the surface of a torus $\Rightarrow$ **toric code**
### Number of encoded logical qubits and logical operators
The number of logical qubits can be determined by counting the number of physical qubits and independent constraints:
- $L^2$ plaquettes $\Rightarrow$ $n^2=2L^2$ physical qubits (they re on the edges)
- $L^2$ plaquettes $\Rightarrow$ $L^2$ Z-stabilizers
- $L^2$ vertices $\Rightarrow$ $L^2$ X-stabilizers

However, not all stabilizers are independent, the $L^2$-th stabilizer is redundant:
$\prod_i S_Z^{(i)}=\mathbb{I} \quad \Rightarrow \prod_{i=1}^{L^2-1}S_Z^{(i)} = S_Z^{(L^2)}$
$\prod_i S_X^{(i)}=\mathbb{I} \quad \Rightarrow \prod_{i=1}^{L^2-1}S_X^{(i)} = S_X^{(L^2)}$
$\Rightarrow$ Only $2(L^2-1)$ independent X,Z-stabilizers

This yields for $k=n-\text{\# independent constraints}=(2L^2)-2(L^2-1)=2$

The toric code can host 2 encoded logical qubits. This is a **topological property**, and independent of the lattice size or lattice structure (square lattice, hexagonal lattice, etc.)

Logical operators $\{Z_L^{(1)},Z_L^{(2)},X_L^{(1)},X_L^{(2)}\}$ correspond to non.contractable string operators winding around the hole and the handle of the torus:
![[Images/Pasted image 20250812144047.jpg]]

![[Images/Pasted image 20250812144133.jpg]]

- All string operators commute with all stabilizers: $[O_L,S^{(i)}]=0 \quad \checkmark$
	- $Z_L^{(1)}$ and $Z_L^{(2)}$ touch an even number of vertices, the first half and last half of the vertex is combined to one full vertex in the torus
	- $X_L^{(1)}$ and $X_L^{(2)}$ touch an even number of plaquettes
- $X_L^{(i)}$ and $Z_L^{(i)}$ of the same encoded qubit anticommute as required: $\{X_L^{(i)},Z_L^{(i)}\}=0 \quad i=1,2 \quad \checkmark$
	- They share exactly **one single** physical qubit and thus the number of anticommutes is uneven
- Logical operators of different needed qubits commute as required:
	$[Z_L^{(1)},Z_L^{(2)}]=[X_L^{(1)},X_L^{(2)}]=0$
	$[Z_L^{(1)},X_L^{(2)}]=[X_L^{(1)},Z_L^{(2)}]=0$
	thus $[O_L^{(1)},O_L^{(2)}]=0 \quad \checkmark$
- Note that logical operators don‘t have unique qubit support (which means that they do not reach any arbitrary qubit normally) but can be deformed by multiplication with stabilizer operators which act trivially on logical states:
- ![[Images/Pasted image 20250813102404.jpg]]
The deformed operators have the same action on logical states:

$\tilde{Z}_L^{(1)}|\psi\rangle_L=Z_L^{(1)}S_Z|\psi\rangle_L=Z_L^{(1)}|\psi\rangle_L$

Commutation and anticommutation relations are preserved under such continuous deformations:
![[Images/Pasted image 20250813103016.jpg]]

Finally, one can write the logical basis states explicitly in the Z-Basis:
$$
\begin{align}
|0\rangle_L^{(1)}|0\rangle_L^{(2)} &\propto \frac{1}{2} (\mathbb{I}+Z_L^{(1)})\frac{1}{2} (\mathbb{I}+Z_L^{(2)}) \prod_+ \frac{1}{2} (\mathbb{I}+S_X^{(+)})\prod_\Box\frac{1}{2} (\mathbb{I}+S_Z^{(\Box)})|0\rangle^{\otimes n} \\
&= \prod_+ \frac{1}{2} (\mathbb{I}+S_X^{(+)})\frac{1}{2}(\mathbb{I}+Z_L^{(1)})\frac{1}{2} (\mathbb{I}+Z_L^{(2)})\prod_\Box\frac{1}{2} (\mathbb{I}+S_Z^{(\Box)}) |0\rangle^{\otimes n}\\
&=\prod_+ \frac{1}{2} (\mathbb{I}+S_X^{(+)}) |0\rangle^{\otimes n}\\
|1\rangle_L^{(1)}|0\rangle_L^{(2)} &= X_L^{(1)} |0\rangle_L^{(1)}|0\rangle_L^{(2)} \\
\end{align}
$$
Intuitively the following happens: We maximize the deformations of the strings, we can change the order of the terms because the logical operators commute with the stabilizers. The string could be deformed again generally. But in this case the $|0\rangle^{\otimes n}$ state is the eigenstate for the projector of the $Z$-basis for all qubits, so we get an eigenvalue +1 for those projectors, so only the $S_X^{(+)}$ projectors remain. Remember that the last stabilizer is redundant and doesn‘t change the subspace of the projectors, meaning that the eigenvalues of the stabilizers already have been considered.
Example L=2:
$$
\begin{aligned}

\Bigg(\prod_{i=1}^{4}\frac{\mathbb{I}+S_X^{(i)}}{2}\Bigg)\,|0\rangle^{\otimes 8}

&= \frac{1}{16}\,( \mathbb{I}+S_{X1})(\mathbb{I}+S_{X2})(\mathbb{I}+S_{X3})(\mathbb{I}+S_{X4})\,|0\rangle^{\otimes 8}\\

&= \frac{1}{8}\,( \mathbb{I}+S_{X1})(\mathbb{I}+S_{X2})(\mathbb{I}+S_{X3})\,|0\rangle^{\otimes 8} \qquad

\big(S_{X4}=S_{X1}S_{X2}S_{X3}\big)\\[4pt]

&= \frac{1}{8}\big(\mathbb{I}+S_{X1}+S_{X2}+S_{X3}

+S_{X1}S_{X2}+S_{X1}S_{X3}+S_{X2}S_{X3}+S_{X1}S_{X2}S_{X3}\big)\,|0\rangle^{\otimes 8}\\[4pt]

&= \frac{1}{8}\big(

|00000000\rangle+|11100010\rangle+|00011101\rangle+|11010001\rangle\\

&\qquad\qquad\quad\ 

+|11111111\rangle+|11001100\rangle+|00110011\rangle+|00101110\rangle

\big)

\end{aligned}
$$

### QEC using the toric code
- Errors on physical qubit show up as stabilizer „excitations“ (i.e. [[indirect measurement|-1 eigenvalue measurements]]) of adjacent plaquette and vertex operators:
- Idea: Syndrome information is used to make best possible guess about the homological class of the set of errors which have occurred on the system
	- Errors are created randomly and can diffuse
	- We want to detect the errors quickly and reliably, and keep them localized and remove them

![[Images/Pasted image 20250813172432.jpg]]

![[Images/Pasted image 20250813172634.jpg]]

The error correction succeeds iff the loop $X_L=C+E$ (Correction attempt $C$ + Error chain $E$) is a contractable loop. Note, that the error chain is unknown. This is equivalent to a concatenation of [[Quantum Error Correction#Stabilizer formalism|stabilizer]] operators which don‘t change the codespace per definition. A non contractable loop leads to a logical operation equivalent to a logical error.
### Robustness of the toric code
- Independently distributed, stochastic bit and phase flip errors on physical qubits occurring with probability $p$ can be corrected as long as $p<p_c=10.9\%$.
- Decoding (i.e. determining a correction attempt given an error syndrome) an be done e.g. using the **minimum-weight matching** (MWPM) algorithm: find correction chain with overall shortest length
![[Images/Pasted image 20250813173558.jpg]]


[[Surface Code|Planar surface codes]] are the physical implementation for the toric code.