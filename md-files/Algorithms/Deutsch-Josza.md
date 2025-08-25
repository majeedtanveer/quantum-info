The Deutsch-Josza Algorithm is the multifunction generalization of the [[Deutsch]] Algorithm.

### Problem
- For N=$2^n$, we are given an N-bit String $x \in \{0,1\}^N$ as input such that either:
1. all $x_i$ have the same value (“constant“) 
2. N/2 of the $x_i$ are 0, and $N/2$ are 1 (“balanced“)
- Here the index $i \in \{0,1\}^N$ from $i=0$ to $2^n-1$, to label all $N=2^N$ elements.
- We can view this again as a function $x_i=f(i)$
- **Goal**: find out whether x is constant or balanced
	- Note: We are not interested in the individual values $x_i$, but only in the global property whether x is constant or balanced
### Example
N=8, n=3
$x=(11111111); x$ constant
$x = (10010101); x$ balanced
### Classical Computation
- First compute individual values $x_0,x_1,x_2,…,x_{N-1}$
	- In this step we obtain more information than we need, namely on the individual values
- In a second step, we compare the values-
$\Rightarrow$ A classical algorithm requires in general $\frac{N}{2} + 1$ evaluations of x to answer the question (Worst case, if $x_{N/2+1}$ is the same as all before we know for certainty that the function is constant. With less evaluations we can only guess)
### Quantum Computation
- **Claim**: we can do better, with a single evaluation of f. We won‘t (in fact must not) obtain any information on the individual values $x_i=f(i)$, if we will be able to answer the question
#### The query setting
- Many quantum algorithms work with queries (including [[Grover]] and [[Shor]])
- We can think of the inputs as an N-bit memory, which we can access at any point of our choice (RAM)
- A memory access is via a so-called „black-box“, which outputs bit $x_i$ on input $i$
- As a quantum operation, this is realized by the (n+1)-qubit unitary $O_x: | i,b \rangle \rightarrow |i, b \oplus x_i \rangle$, with address register of n qubits $i \in \{0,1\}^n$ target bit $b \in \{0,1\}$
- **Remarks**:
	- After the transformation, the state $|i, b \oplus x_i \rangle$ is not necessarily a product state ($|i, b \oplus x_i \rangle \neq |i \rangle | b \oplus x_i \rangle$) , unless $|i \rangle$ is one compuational basis state
	- $O_x$ is unitary and hermitian because $O_x^2=\mathbb{I}$ 
	- Every application of $O_x$ requires one evaluation of $x$
#### Implementation
- We want to prepare an equal-weight superposition off all basis states on the first n qubits with [[Hadamard-Gate|H-Gates]]  
- If $|b \rangle = |0 \rangle$ then we get
	- $O_x \frac{1}{\sqrt{2^n}} \sum_{i \in \{0,1\}^n} |i \rangle | 0 \rangle = \frac{1}{\sqrt{2^n}} \sum_{i \in \{0,1\}^n} |i \rangle | x_i \rangle =  \frac{1}{\sqrt{2^n}} ( | 0 \rangle |x_0 \rangle + | 1 \rangle |x_1 \rangle + … + | N-1 \rangle |x_{N-1} \rangle)$
	- The state contains **all** function values in superposition in the target qubit, and (in general) entangled with the first n qubits
	- But we can access the information: If we measure the first qubits, the superposition collapses with probability $1/2^n$ to any computational state $|i \rangle |x_i \rangle$. This is not better than one evaluation in a classical algorithm. Similar to [[Deutsch]] we need [[Algorithmic Interference]] here.
- If $|b \rangle = |- \rangle$ then we get
	- $O_x |i \rangle |- \rangle = (-1)^{x_i} |i \rangle | - \rangle$ (see [[Deutsch]])
	- So the action of the phase [[Oracle]] is $|i \rangle \rightarrow (-1)^{x_i} | i \rangle$ which does nothing if $x_i=0$ and adds a phase if $x_i=1$, the oracle can be thus noted as $O_{x,\pm}$
- Now we reapply [[Hadamard-Gate|H-Gates]] and get the following in total:
$$
\begin{align*}
H^{\otimes n}O_{x,\pm} \frac{1}{\sqrt{2^n}} \sum_{i \in \{0,1\}^n} |i \rangle &= H^{\otimes n}\frac{1}{\sqrt{2^n}} \sum_{i \in \{0,1\}^n} (-1)^{x_i}|i \rangle \\
&=\frac{1}{2^n} \sum_{i \in \{0,1\}^n} (-1)^{x_i} \sum_{j \in \{0,1\}^n} (-1)^{i \cdot j} | j \rangle \\
\end{align*}
$$
For $x$ is constant, our state is $|0\rangle^{\otimes n}$ if all $x_i=0$ and $-|0\rangle^{\otimes n}$ if  all $x_i=1$ because this is the only $|j \rangle$ that survives. So if we measure this state we know for certainty that we have a constant function. If we measure a different state we know for certainty that we have a balanced function. We have again a global phase which is inaccessible which is important!

#### Comparison
- The Deutsch-Josza algorithm can be solved with certainty using only one quantum query and $O(n)$ other operations
- In contrast any classical deterministic algorithm needs at least N/2 +1 queries
	- Classical algorithm can solve this problem efficiently if we allow for a small error probability and can be in general better if we allow this

### Bernstein-Vazirani Algorithm

- It is identical to the Deutsch-Josza algorithm but with the additional property $x_i= (i \cdot a) \mod{2}$, the final measurement yields a with certainty
- Per definition of the [[Hadamard-Gate|H-Gates]] the following holds:
	- $H^{\otimes n} |a \rangle = \frac{1}{\sqrt{2^n}} \sum_{i \in \{0,1\}^n} (-1)^{a \cdot i} |i \rangle$
- After step (3) we have (with inserting $x_i$)
	- $H^{\otimes n}\frac{1}{\sqrt{2^n}} \sum_{i \in \{0,1\}^n} (-1)^{x_i}|i \rangle = H^{\otimes n}\frac{1}{\sqrt{2^n}} \sum_{i \in \{0,1\}^n} (-1)^{i \cdot a}|i \rangle = H^{\otimes n} H^{\otimes n} |a \rangle = |a \rangle$ 


### Algorithm steps summary
1. Start with an $|0 \rangle^{\otimes n}$ register
2. Apply a Hadamard to end the qubit
3. Apply a phase oracle query $O_{x,\pm}$ 
4. Apply another Hadamard to each qubit
5. Measure the final state

### Circuit implementation
![[Deutsch-Josza.png]]