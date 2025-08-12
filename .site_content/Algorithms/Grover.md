The quantum search algorithm was proposed by Lev Grover in 1994.

### The problem
- Search through a search space of N elements.
- Assume for convenience $N=2^n$ $\rightarrow$ n bits of information to label one element
- Assume that the problem of interest has exactly $M <N$ solutions (typically $M \ll N$)
$\Rightarrow$ How fast can we find at least one of the solutions?
A particular instance of a problem is conveniently represented by a function $f$, which takes as an input an integer $x$, $0 \leq x \leq N-1$, and yields
	$f(x)=1$ if $x$ is a solution to the search problem
	$f(x)=0$ if $x$ is **not** a solution to the search problem

#### Example 
Hamiltonian path problem:
A particular graph $G$ specifies $f$.
Inputs $x$ correspond to paths (i.e. sequences of vertices)
	$$
f(x) = \begin{cases}
1 & \text{if } x \text{ is a Hamiltonian path in } G \\
0 & \text{otherwise}
\end{cases}
$$
![[Images/Pasted image 20250726113705.png]]

Note: One doesn‘t need to know a Hamiltonian path beforehand, to be able to recognize one!

### The Quantum Algorithm
#### [[Oracle]]
- Unitary operator $O_f$:
	$O_f | x,q \rangle = | x, q \oplus f(x) \rangle$
	Where $x$ is the input state of n qubits and $q$ the single oracle qubit (see [[Deutsch-Josza]])
- For $|q\rangle = |- \rangle$ this realizes the phase oracle i the usual way:
	$|x \rangle | - \rangle = (-1)^{f(x)} |x \rangle | - \rangle$
$\Rightarrow O_{f,\pm}|x\rangle = \begin{cases} - | x \rangle & \text{if } x \text{ is a solution } \\ | x \rangle & \text{otherwise} \end{cases}$
- The implementation of the oracle depends on the solutions!
- Discussion:
	- The oracle does not know any of the solution(s), it is only able to recognize a solution
	- The exact construction of the oracle is not important
	- It can however be constructed using e. g. known classical (efficient) algorithms, which are simply „run on a quantum computer“. Checking solutions is in P for any problem in NP
It is always possible to implement (with a polynomial overhead of [[Ancilla|Ancillas]] and circuit depth) a solution checking subroutine (see [[Deutsch-Josza]])
Examples:
- a solution checking whether a path x is Hamiltonian
- A subroutine checking whether an integer $p$ is a prime factor of the larger number $N$, e. g. by simple division: $q=N/p$ integer?
#### Grover‘s algorithm
1. Prepare initial state $| \psi \rangle = \frac{1}{\sqrt{2^N}} \sum_x | x \rangle$ (unbiased superposition)
2. Perform the Grover iteration $k$ times:
	- apply oracle $O_{f,\pm}$
	- Then apply „reflection operator“ $U=2|\psi \rangle \langle \psi | - \mathbb{I}$
3. Measure the qubits, yielding an outcome $x$

#### Circuit implementation
![[Images/Pasted image 20250726130507.png]]

### Functionality
Rewrite the initial state

$$

\begin{align}
| \Psi \rangle &= \frac{1}{\sqrt{N}} \sum_x | x\rangle = \frac{1}{\sqrt{N}} \left(\sum^{’’} |x \rangle + \sum^{’} |x \rangle \right) \\
&= \frac{1}{\sqrt{N}} \left(\sqrt{N-M} \frac{1}{\sqrt{N-M}} \sum^{’’} |x \rangle + \sqrt{M} \frac{1}{\sqrt{M}} \sum^{’} |x \rangle \right) \\
&= \sqrt{\frac{N-M}{N}} | \alpha \rangle + \sqrt{\frac{M}{N}} | \beta \rangle \\
&= \sqrt{1-\varepsilon} | \alpha \rangle + \sqrt{\varepsilon} | \beta \rangle
\end{align}
$$
With $\sum^{’’}$ being the sum over all states which are **not** solutions, $\sum^{’}$ being the sum over all states which are solutions and $\varepsilon = \frac{M}{n}$ typically $\varepsilon \ll 1$ (solutions are hard to find)
- Probability to find (measure) a particular solution $|x \rangle$ in $| \psi \rangle: \frac{1}{N}$ 
- Probability to find **any** solution. Projector onto solution subspace $\hat{P}= \sum^{’}|x \rangle \langle x | \rightarrow p = \langle \psi | \hat{P} | \psi \rangle = \frac{M}{N}=\varepsilon$  
The oracle unitary $O$ can be written as
	$O= 1-2 \sum^{’} |x \rangle \langle x |$
	Let‘s apply one Grover step $G=UO$ to $| \psi \rangle$:
$$
\begin{align}
O | \psi \rangle &= O(\sqrt{1-\varepsilon} | \alpha \rangle + \sqrt{\varepsilon} | \beta \rangle) \\
&= \sqrt{1-\varepsilon} | \alpha \rangle - \sqrt{\varepsilon} | \beta \rangle \\
&= (\sqrt{1-\varepsilon} | \alpha \rangle + \sqrt{\varepsilon} | \beta \rangle)- 2\sqrt{\varepsilon} | \beta \rangle \\
&= |\psi \rangle - 2 \sqrt{\varepsilon} | \beta \rangle \\
UO |\psi \rangle &= (2 |\psi \rangle \langle \psi | - \mathbb{I})(|\psi \rangle - 2 \sqrt{\varepsilon} | \beta \rangle) \\
&= 2  |\psi \rangle - |\psi \rangle - 4 \sqrt{\varepsilon} \langle \psi|\beta\rangle |\psi \rangle + 2\sqrt{\varepsilon} |\beta \rangle \\
&= (1-4 \varepsilon)|\psi \rangle+2\sqrt{\varepsilon} | \beta \rangle \\
&= (1-4\varepsilon) (\sqrt{1-\varepsilon} | \alpha \rangle + \sqrt{\varepsilon} | \beta \rangle)+2\sqrt{\varepsilon} | \beta \rangle \\
&= (1-4 \varepsilon) \sqrt{1-\varepsilon} |\alpha \rangle + \sqrt{\varepsilon}(3-4 \varepsilon)|\beta \rangle
\end{align}
$$
Now, the probability to find the system in any solution sate measuring $UO\psi\rangle$ is
	$p=(\sqrt\varepsilon(3-4\varepsilon))^2=9 \varepsilon=9\frac{M}{N}$, the probability has increased by a factor of 9!

#### Geometric Visualization
- Dynamics takes place only in a 2-dimensional subspace spanned by $|\alpha\rangle$ and $|\beta\rangle$
$|\psi \rangle=\cos\frac{\theta}{2} |\alpha \rangle + \sin \frac{\theta}{2} |\beta \rangle$
	Parameterization with $\cos\frac{\theta}{2}=\sqrt{\frac{N-M}{N}}=\sqrt{1-\varepsilon}$ and $\sin\frac{\theta}{2}=\sqrt{\frac{M}{N}}=\sqrt{\varepsilon}$ 
![[Images/Pasted image 20250726153118.png]]

$\rightarrow$ State is rotated towards $|\psi \rangle$ (the solutions):
	$G|\psi \rangle = \cos{\frac{3\theta}{2}} |\alpha \rangle + \sin{\frac{3\theta}{2}} |\beta \rangle$
	$G^k|\psi \rangle = \cos{\frac{2k+1}{2} \theta} |\alpha \rangle + \sin{\frac{2k+1}{2} \theta} |\beta \rangle$
How many times $k$ should $G$ be applied?
$\sin{\frac{2k+1}{2}\theta} \approx 1$
$\frac{2k+1}{2}\theta \approx \frac{\pi}{2} \rightarrow k \approx \frac{\pi}{2\theta}$
$\sin\frac{\theta}{2} \approx \frac{\pi}{2} = \sqrt{\frac{M}{N}}$
$\rightarrow \tilde{k} \approx \frac{\pi}{4}\sqrt{\frac{N}{M}}$ are optimal

>[!IMPORTANT] $O(\sqrt{\frac{N}{M}})$ oracle queries suffice to find a solution with probability close to 1

Compare to classical case $O(\frac{N}{M})$
$\rightarrow$ Quadratic Speeedup

### Discussion
The Grover algorithm can be used to speed up NP-complete problems.
Example: Hamiltonian Path problem
Brute Force search $n^n=2^{n \cdot \log(n)}$ Paths
Quantum speed-up: reduction to $O(2^{n\cdot\log(n)/2})$

#### Optimality
One can **prove** that there exists no quantum algorithm that can perform he task with less than $O\left(\sqrt{\frac{N}{M}}\right)$ oracle inquiries.
This, the Grover algorithm is **optimal**

If we choose the integer $k$ closest to $\tilde{k}$, the failure probability will still be small:
$$
\begin{align}
p_\mathrm{fail} &= \cos\left({\frac{2k+1}{2}\theta}\right)^2 \\
&= \cos\left({\frac{2\tilde{k}+1}{2}\theta} + (k-\tilde{k}) \theta \right)^2 \\
&= \cos\left(\frac{\pi}{2} + (k-\tilde{k}) \theta \right)^2 \\
&= \sin\left((k-\tilde{k}) \theta \right)^2 \\
&\leq \sin\left(\frac{\theta}{2}\right)^2
\mathrm{for} \, |k-\tilde{k}| \leq \frac{1}{2}, \mathrm{and} \, \theta \ll 1 \\
&= \frac{M}{N} \; \mathrm{small}
\end{align}
$$

Number of queries:
$k \leq \frac{\pi}{2 \theta} \leq \frac{\pi}{4}\sqrt{\frac{N}{M}}$
$\Rightarrow$ Number of queries does not grow.
### Problems
- If we don‘t know $M$, we don‘t know how many steps $k$ t apply - if $k$ get‘s too big, the success probability decreases again
- Assumption of knowing beforehand the number $M$ of solutions can be relaxed: A slightly more complicated algorithm (basically running the above algorithm with systematic different for $k$) still finds a solution with an expected number of queries $O\left(\sqrt{\frac{N}{M}}\right)$
- The algorithm can also be modified o estimate the number of solutions: [[Quantum Counting]]