There exist universal gate sets, from which any quantum circuit on n qubits can be built.

> [!IMPORTANT] CNOT + arbitrary single-qubit rotations = universal

> [!IMPORTANT] CNOT + small (finite) set of single qubit gates = universal

#### Examples
- {CNOT, H, T}

They allow one to **approximate** an arbitrary n-qubit circuit to arbitrary precision

#### Constructive Proof
1. Arbitrary n-qubit gates can be decomposed into products of n-qubit unitary operators that act in a [[2-dimensional subspace]] only.
Goal: Decompose n-qubit gate U into product of gates acting only with a unitary V on 2-dim subspace only:
(Rest of entries are zero)
$$
V_n = \begin{pmatrix}
1 &        &        &        &        &        &        &        &        &        \\
  & \ddots &        &        &        &        &        &        &        &        \\
  &        & a      &        &        &        & b      &        &        &        \\
  &        &        & 1      &        &        &        &        &        &        \\
  &        &        &        & \ddots &        &        &        &        &        \\
  &        &        &        &        & 1      &        &        &        &        \\
  &        & c      &        &        &        & d      &        &        &        \\
  &        &        &        &        &        &        & 1      &        &        \\
  &        &        &        &        &        &        &        & \ddots &        \\
  &        &        &        &        &        &        &        &        & 1      \\
\end{pmatrix}
$$

$V=\begin{pmatrix}a & b \\ c & d \end{pmatrix}$ unitary,
$V^\dagger V = \mathbb{I}$

Example d=3 for illustration purposes

$U=\begin{pmatrix}a & d & g \\ b & e & h \\ c & f & i \end{pmatrix}$, $U^\dagger U=\mathbb{I}$

We will find two-level unitaries $V_k$ such that $V_3V_2V_1U = \mathbb{I}$
If we manage, it follows that

$U^\dagger = V_3V_2V_1$
and thus  $U=V_1^\dagger V_2^\dagger V_3^\dagger$

If $V_k$ are unitaries so are their inverses $V_k^\dagger$ .

If $b=0$, set $V_1=\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$
If $b=0$, set $V_1=\begin{pmatrix}\frac{a^*}{\sqrt{|a|^2+|b|^2}} & \frac{b^*}{\sqrt{|a|^2+|b|^2}} & 0 \\ \frac{b}{\sqrt{|a|^2+|b|^2}} & \frac{-a}{\sqrt{|a|^2+|b|^2}} & 0 \\ 0 & 0 & 1 \end{pmatrix}$

Note: for both cases $V_1$ is a valid 2-level unitary
^
Now, one can check that
$V_1U=\begin{pmatrix}a’ & d’ & g’ \\ 0 & e’ & h’ \\ c’ & f’ & i’ \end{pmatrix}$
With some other entries denoted by prime’.
The key property is that now the left middle entry is now **zero** due to construction

Next, we will achieve to set the lower left entry to zero:

If $c’=0$, set $V_2=\begin{pmatrix} a’^* & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$
If $c’=0$, set $V_2=\begin{pmatrix}\frac{a’^*}{\sqrt{|a’|^2+|c’|^2}} & 0 & \frac{c’^*}{\sqrt{|a’|^2+|c’|^2}} \\ 0 & 1 & 0 \\ \frac{c’}{\sqrt{|a’|^2+|c’|^2}} & 0 & \frac{-a’}{\sqrt{|a’|^2+|c’|^2}} \end{pmatrix}$

In either case we will find:

$V_2V_1U=\begin{pmatrix}1 & d’’=0 & g’’=0 \\ 0 & e’’ & h’’ \\ 0 & f’’ & i’’ \end{pmatrix}$
$V_2V_1U$ is unitary thus $d’’=g’’=0$

Finally we set $V_3=\begin{pmatrix}1 & 0 & 0 \\ 0 & e’’^* & h’’^* \\ 0 & f’’^* & i’’^* \end{pmatrix}$
For d= $2^n$:

- We need to construct in general d-1 two-level matrices $U_1,U_2,…,U_{d-1}$ such that

$$
U_{d-1}U_{d-2}…U_1U = \begin{pmatrix}1 & 0 & 0 & 0\\ 0 &  & …  \\0 & & … & \\ 0 &  & … &  \end{pmatrix}
$$
- Then d-2 for the second column, etc.
- In the end we manage to write the  $d \times d$ matrix $U$ by some two-level matrices $V_i$,
	$U=V_1…V_k$
	with $k \leq (d-1) + (d-2) + … + 1= \frac{d(d-1)}{2}$
	$\Rightarrow$ For an n-qubit system it follows that U can be written by at most
		$2^{n-1}(2^n-1) \leq 4^n$
		two-level matrices

Discussion:
- This is inefficient (exponential to n)
- For specific unitaries much more efficient decompositions may exist
- There exist however matrices which can not be decomposed into less than an exponential number of two-level unitaries
- Quantum computation and quantum algorithms are not about arbitrary unitaries, but realizing unitaries with a lot of structure which can be efficiently decomposed

2. Arbitrary such gates, acting only on two computational basis states in the $d=2^n$-dimensional Hilbert space of n-qubits can be written in terms of [[CNOT gate|CNOT gates]] and single-qubit [[Rotation Gates]].
Goal: Implement these $V_k$ two-level unitaries by [[CNOT gate|CNOT gates]] and single qubit rotations only:
Example 1) $n=3$ $d=2^3=8$ 

$$
V_k =
\left(
\begin{array}{cccccccc}
1 &        &        &        &        &        &        &        \\
  &  1     &        &        &        &        &        &        \\
  &        & 1      &        &        &        &        &        \\
  &        &        & 1      &        &        &        &        \\
  &        &        &        & 1      &        &        &        \\
  &        &        &        &        & 1      &        &        \\
  &        &        &        &        &        & a      & b      \\
  &        &        &        &        &        & c      &     d  \\
\end{array}
\right)
\quad
\begin{array}{c}
\\
\\
\\
\\
\\
\\
\leftarrow |110\rangle \\
\leftarrow |111\rangle
\end{array}

$$
$V=\begin{pmatrix}a & b \\ c & d \end{pmatrix}$ unitary,
$V^\dagger V = \mathbb{I}$

This acts non-trivially only on $|110 \rangle$ and $| 111 \rangle$. This means that V is applied to qubit 3 iff qubit 1 and 2 are in $|1 \rangle$.
This Toffoli-type 3 qubit gates (n qubit gates) can be built from CNOT-gates and controlled-U gates only with $V^2=U$:

![[Images/Pasted image 20250722152918.png]]

And 2-qubit [[Controlled-U Gate]] operations can be built from CNOTs and suitable chosen single-qubit operations A,B,C for which $ABC=\mathbb{I}$ and $AXBXC=U$ holds

![[Images/Pasted image 20250722153750.png]]

Every $U \in SU(2)$ (Group of $2 \times 2$ unitaries with determinant 1) can be written as $U=R_x(\alpha)R_y(\beta)R_z(\gamma)$ and or those the one-qubit unitaries would be

$A=R_x(\alpha)R_y\left(\frac{\beta}{2}\right)$
$B=R_y\left(\frac{-\beta}{2}\right)R_x\left(-\frac{\gamma + \alpha}{2}\right)$
$C=R_x\left(\frac{\gamma - \alpha}{2}\right)$

A general unitary V can be written as $e^{i \varphi} U$ where $U$ has determinant 1 and $e^{i \varphi}$ is a phase this can be achieved by using a Phase gate after the control qubit 
Example [[Hadamard-Gate]] from iH Gate which can be realized through rotations

![[Images/Pasted image 20250722160138.png]]
Example 2)

$$
V_k =
\left(
\begin{array}{cccccccc}
a &        &        &        &        &        &        &   b    \\
  &  1     &        &        &        &        &        &        \\
  &        & 1      &        &        &        &        &        \\
  &        &        & 1      &        &        &        &        \\
  &        &        &        & 1      &        &        &        \\
  &        &        &        &        & 1      &        &        \\
  &        &        &        &        &        & 1      &        \\
c &        &        &        &        &        &        &   d    \\
\end{array}
\right)
\quad
\begin{array}{c}
\leftarrow |000\rangle \\
\leftarrow |001\rangle \\
\\
\\
\\
\\
\leftarrow |110\rangle \\
\leftarrow |111\rangle
\end{array}
$$

Choose the last configuration and construct the unitary as such that it acts on that (Here $|111 \rangle$). Then note which other configuration it acts on (Here $|110 \rangle$). Then change one bit at a time from the start configuration (Here $|000 \rangle$) until you convert to said configuration it usually acts on (Here $|000 \rangle \rightarrow |100 \rangle \rightarrow |110 \rangle$). This is called Grey code which connects those states.

With the following notation:

![[Images/Pasted image 20250723101736.png|300]]

We get the following circuit for our grey code:

![[Images/Pasted image 20250723103124.png]]

To realize $C^n(U)$ controlled-U operations in an efficient way, where one qubit undergoes U if n others are all in $|1\rangle$ like in this picture:

![[Images/Pasted image 20250723103523.png|200]]

One can use [[Toffoli Gate|Toffolis]] to concatenate the control qubits to [[Ancilla|Ancillas]]:
![[Images/Pasted image 20250723110031.png]]

Resource Count:
- For one 2-level unitary $(d=2^n)$ we need at most $2(n-1)$ controlled operations $C^{n-1}(X)$ to implement the swap of basis states according to the Grey Code, i. e. $O(n)$ of these operations
- Resource requirement for such $C^n(U): O(n)$ Toffolis. This amounts to $O(n)$ single qubit and CNOT gates
- We saw that we needed at most $O(4^n)$ two-level unitaries $V_i$ to decompose the n-qubit unitary $U$
> [!RESULT] Implementation of an arbitrary n-qubit unitary U can be realized by a quantum circuit containing $O(n^24^n)$ single-qubit and CNOT gates 

3. Arbitrary single-qubit rotations can be approximated by a finite set of single-qubit gates (e.g. [[T-Gate]] and [[Hadamard-Gate]])
A concatenation of Rotations is another [[Rotation Gates|Rotation]] with an angle of an **irrational** multiple of $\pi$ in the Bloch sphere. Example:
$$
\begin{aligned}
R_z(\pi/4)R_x(\pi/4) &= e^{-i\frac{\pi}{8}Z}e^{-\frac{\pi}{8}X} \\ 
&=(\cos\frac{\pi}{8}\mathbb{I}-i \sin{\frac{\pi}{8}}Z)(\cos\frac{\pi}{8}\mathbb{I}-i \sin{\frac{\pi}{8}}X) \\
&=\cos^2{\frac{\pi}{8}}\mathbb{I}-i \cos{\frac{\pi}{8}}\sin{\frac{\pi}{8}}X-i\sin{\frac{\pi}{8}}\cos{\frac{\pi}{8}}Z-\sin^2{\frac{\pi}{8}}ZX \\
&=\cos^2{\frac{\pi}{8}}\mathbb{I}-i \sin{\frac{\pi}{8}}(\cos{\frac{\pi}{8}}(X+Z)+\sin{\frac{\pi}{8}Y}) \\
&= \cos{\frac{\theta}{2}}\mathbb{I}-i \sin{\frac{\theta}{2}}(\vec{n} \cdot \vec{\sigma}) = R_\vec{n}(\theta)
\end{aligned}
$$
With $\vec{n}=(\cos\frac{\pi}{8},\sin\frac{\pi}{8},\cos\frac{\pi}{8})$ 
$\cos\frac{\theta}{2}=\cos^2\frac{\pi}{8}$ is a transcendental equation, this means that $\theta$ is an irrational multiple of $\pi$. That is why we never revisit the same point on the circle!
$\Rightarrow$ We can get arbitrarily close to any point in the circle
$\Rightarrow$ The circle is densely covered
We can construct another orthogonal vector (which are linearly independent) with [[Hadamard-Gate|H-Gates]]: 
$R_\vec{m}(\theta)=HR_\vec{n}(\theta)H$
Where we used the identities of the Hadamard for [[X Gate|X]],[[Y Gate|Y]] and [[Z Gate|Z]] Gates.
Arbitrary single-qubit rotations can be built up from rotations about two axes as:
$U=e^{i \alpha}R_\vec{n}(\beta)R_\vec{m}(\gamma)R_\vec{n}(\delta)$
$\Rightarrow$ Thus, we can approximate an arbitrary single-qubit operation $U$ by only [[Hadamard-Gate|H]] and [[T-Gate|T]].
The efficiency of the approximation is given by the [[Solovay-Kitaev-Theorem]]. For a given small desired error $\varepsilon$, a few rotations are sufficient to quickly get close to the desired $U$. 
Due to the [[Gottesmann-Knill theorem]] any [[Clifford Gates|Clifford Gate]] can be perfectly simulated efficiently.