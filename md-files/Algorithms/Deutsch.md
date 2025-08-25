The Deutsch Algorithm was developed by David Deutsch (1992). This was the first algorithm that showed the potential computational power of quantum computation.
The Algorithm demonstrates typical features and ingredients of quantum computation for example [[Quantum Superposition]] and [[Quantum Entanglement]].

### Setting
- Consider a single bit $x= \{0,1\}$
- A black box that computes a function $f(x)$
- We do not know (and do not care) how, but every evaluation of f is extremely costly (e. g. in terms of computational time)
	$\Rightarrow$ Thus, we want to limit the number of evaluations of f to an absolute minimum

### Possible outcomes
 $f(0)=0;1$
 $f(1)=0;1$
$\Rightarrow$ 4 possibilities
So there are two cases:
$f(0)=f(1)$: f is constant, all bits are the same.
or
$f(0) \neq f(1)$: f is balanced, half of the bits are 0, the other half 1.

We are not interested in the individual values of $f(0)$ and $f(1)$ but only in the global property whether f is constant or balanced.

### Classical Computation
- First compute individual values $f(0)$ and $f(1)$. We get more information than we need, namely on the individual values.
- In a second step we compare the two values
$\Rightarrow$ We need **two** evaluations

### Quantum Computation
- **Claim**: We can do better, with a single evaluation of f. We won‘t (in fact must not) obtain any information on the individual values of f, yet we will be able to answer the question
- We will use two qubits,
	- $|x \rangle = \alpha_x | 0 \rangle + \beta_x | 1 \rangle$
	- $|y\rangle = \alpha_y | 0 \rangle + \beta_y | 1 \rangle$
- in an initial product state
	- $|x,y \rangle = | x \rangle | y \rangle$
- We will use a two-qubit unitary transformation
	- $U_f: | x \rangle | y \rangle \rightarrow |x,y \oplus f(x) \rangle$
	- Here $\oplus$ denotes addition modulo 2
- The transformation leaves the first qubit unchanged and acts on the second one as follows:
	- If $f(x)=0$ y is not changed
	- If $f(x)=1$ y is flipped $0 \rightarrow 1; 1 \rightarrow 0$
- Remarks:
	- After the transformation, the state $|x, y \oplus f(x) \rangle$ can not be written as a product state: $|x, y \oplus f(x) \rangle \neq |x \rangle | y \oplus f(x) \rangle$
	- $U_f$ is unitary and Hermitian because $U_f^2= \mathbb{I}$
	- Every application of $U_f$ requires **one** evaluation of f
- For $|+ \rangle |0 \rangle$ we get:
	- $U_f |+ \rangle |0\rangle = U_f \frac{1}{\sqrt{2}} (|0 \rangle |0\rangle + |1 \rangle |0\rangle) = \frac{1}{\sqrt{2}} (|0 \rangle |f(0)\rangle + |1 \rangle |f(1)\rangle)$
	- This state contains both functions in superposition in the second qubit and in general entangled with the first qubit
	- If we measure the first qubit the second qubit collapses to either $|f(0) \rangle$ or $|f(1) \rangle$ with probability 1/2. This is not better than one evaluation in a classical algorithm because we get to know the both individual values (with uncertainty). It is even worse.
	$\Rightarrow$ [[Quantum Parallelism]] is an ingredient for speedup but not enough. We also need [[Algorithmic Interference]], i. e. a way of constructively interfering the paths such that the information we are interested in (f balanced or constant) is **amplified**, and the information we don‘t care about (individual values $f(0)$ and $f(1)$) becomes inaccessible.
- If we prepare the $|-\rangle$-state we get the following:
	- $U_f |x \rangle |-\rangle = |x\rangle \frac{1}{\sqrt{2}}(|0 \oplus f(x) \rangle - |1 \oplus f(x) \rangle) = (-1)^{f(x)} |x \rangle |-\rangle$   
- For $|+ \rangle |- \rangle$ we get:
	- $U_f |+ \rangle |-\rangle = U_f \frac{1}{\sqrt{2}} (|0 \rangle |-\rangle + |1 \rangle |-\rangle) = \frac{1}{\sqrt{2}} ((-1)^{f(0)}|0 \rangle |-\rangle + (-1)^{f(1)}|1 \rangle |-\rangle)$  

| $f(0)$ | $f(1)$ | $U_f \|+ \rangle \|-\rangle$ |
| ------ | ------ | ---------------------------- |
| 0      | 0      | $\|+ \rangle \|-\rangle$     |
| 1      | 0      | $-\|- \rangle \|-\rangle$    |
| 0      | 1      | $\|- \rangle \|-\rangle$     |
| 1      | 1      | $-\|+ \rangle \|-\rangle$    |
- So the first qubit is measured as $|+ \rangle$ for a constant function and $| - \rangle$ for a balanced function 
- The information of the individual function values appear as a global phase factor ($\pm 1$) which can not be measured directly.
- Final Step: $X_1$ measurement
	$\rightarrow$ the probability of the $|+ \rangle$-state is 1 for f constant
	$\rightarrow$ the probability of the $|- \rangle$-state is 1 for f balanced

- With specific preparation of  and an [[Oracle]] which is an implementation of $f(x)$ 
- Remarks:
	- We evaluated f only once
	- Speedup due to [[Quantum Parallelism]] is 2 (Constant)


### Circuit implementation
![[Deutsch.png]]