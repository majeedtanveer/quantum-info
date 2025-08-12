### Order finding
- The problem of order finding is equivalent to factoring
- We will develop an efficient quantum algorithm for order finding hoch in turn provides an efficient way to factor
- The quantum algorithm for order finding will be using [[Quantum Phase Estimation]]
For positive integers $x$ and $N$, $x<N$, with no common factors (i.e. $x$ and $N$ are coprime) the **order** of $x$ modulo $N$ is defined to be the smallest integer $r$, such that 
$$
x^r=1 \mod N
$$
Example: $x=3, N=7$

$$
\begin{aligned}
x^1 \mod N = 3^1 \mod 7 = 3 \\
x^2 \mod N = 3^2 \mod 7 = 2 \\
x^3 \mod N = 3^3 \mod 7 = 6 \\
x^4 \mod N = 3^4 \mod 7 = 4 \\
x^5 \mod N = 3^5 \mod 7 = 5 \\
x^6 \mod N = 3^6 \mod 7 = 1 \\
\end{aligned}
$$
$\rightarrow$ order of 3 modulo 7 is $r=6$
This is then cyclic, if we continue:
$x^7 \mod N = 3$
Since $x^{r+i} \mod N = (x^rx^i) \mod N=(x^r \mod N)(x^i \mod N) \mod N= x^i \mod N$

>[!IMPORTANT] Order finding is believed (not proven!) To be a hard problem on a classical computer

No algorithm is known to solve the problem using resources that are polynomial in the $O(L)$ bits needed to specify the problem, where $L=\lceil \log N \rceil$is the number of bits needed to specify $N$.
In essence, the quantum algorithm for order finding is the quantum phase estimation algorithm applied to the unitary $U |y\rangle\equiv|xy\mod N\rangle$, where $|y\rangle$ is an $L$-qubit state, $y \in \{0,1\}^L$
Not that we are using the convention that when $N \leq y \leq 2^L-1$ the expression $xy \mod N=y$.
In other words, $U$ acts non-trivially only when $0 \leq y \leq N-1$.
The following states $|u_s\rangle\equiv \frac{1}{\sqrt{r}} \sum_{k=0}^{r-1} \exp\left(-\frac{2 \pi i s k}{r}\right) |x^k \mod N\rangle$ are eigenstates of $U$ as shown below:
$$
\begin{aligned}
U|u_s\rangle &= \frac{1}{\sqrt{r}} \sum_{k=0}^{r-1} \exp\left(-\frac{2 \pi i s k}{r}\right) U|x^k \mod N\rangle \\
&= \frac{1}{\sqrt{r}} \sum_{k=0}^{r-1} \exp\left(-\frac{2 \pi i s k}{r}\right) |x^{k+1} \mod N\rangle \\
&= \frac{1}{\sqrt{r}} \sum_{k’=1}^{r} \exp\left(-\frac{2 \pi i s (k’-1)}{r}\right) |x^{k’+1} \mod N\rangle \\
&=\exp\left(\frac{2 \pi i s}{r}\right)\frac{1}{\sqrt{r}} \sum_{k’=0}^{r-1} \exp\left(-\frac{2 \pi i s k’}{r}\right) |x^{k’+1} \mod N\rangle \\
&=\exp\left(\frac{2 \pi i s}{r}\right)|u_s\rangle
\end{aligned}
$$
We used $k’=k+1$ and the fact that the $k’=r$ term is the same as the $k’=0$ term which allows us to shift the sum. Using phase estimation will allow is it obtain with high accuracy the corresponding eigenvalues $\exp\left(-\frac{2 \pi i s}{r}\right)$ from which we will be able to obtain the order $r$ with some extra work.
Problem: Preperation of $|u_s\rangle$ would require knowledge about $r$ so this is impossible.
However we don‘t need this since the superposition of all eigenstates (using the [[Kronecker Delta]] identity):
$$
\begin{aligned}
\frac{1}{\sqrt{r}}\sum_{s=0}^{r-1} |u_s\rangle &= \frac{1}{r}\sum_{s=0}^{r-1}\sum_{k=0}^{r-1} \exp\left(-\frac{2 \pi i s k}{r}\right) |x^k \mod N\rangle \\
&= \frac{1}{r}\sum_{k=0}^{r-1} r \delta_{k0} |x^k \mod N\rangle \\
&= |x^0 \mod N\rangle \\
&= |1\rangle = |0\rangle|0\rangle…|0\rangle|1\rangle
\end{aligned}
$$

### Modular exponentiation
For each $s$ in the range 0 to $r-1$ this will lead an estimate of the phase $\varphi \approx \frac{s}{r}$ that is accurate to $2L+1$ bits, and with probability at least $(1-\varepsilon)/r$.

For the algorithm to be efficient, we need efficient procedures to implement controlled $U^{2^j}$-operations. This can be achieved by a technique called **modular exponentiation**.

We need to realize the transformation
$$
\begin{aligned}
|z\rangle | y \rangle &\rightarrow |z\rangle U^{z_t 2 ^{t-1}}…U^{z_1 2 ^{0}} |y\rangle \\
&= |z\rangle |x^{z_t2^{t-1}} \times … \times x^{z_12^{0} y \mod N} \\
&= |z\rangle|x^zy \mod N \rangle
\end{aligned}
$$
This can be achieved using **reversible computing** using temporarily a third register.
For that we compute $x^{2^j} \mod N$ by squaring $x^{2^j-1} \mod N$ up to $x^{2^t-1}$.
$\rightarrow$ Since $t=2L+1 + \left\lceil \log{\left(2+\frac{1}{2 \varepsilon}\right)}\right\rceil$ These are $O(L)$ squaring operations.
Each requires $O(L^2)$ operations (standard multiplication).
$\rightarrow$ $O(L^3)$ operations which can be translated into a reversible quantum circuit with $O(L^3)$ quantum gates which realizes $|z\rangle = |z\rangle|x^zy \mod N \rangle$
### Continued Fractions Algorithm
The last step to get $r$ is using the **Continued Fractions Algorithm** whose use is allowed to the following theorem:
For a rational number $\frac{s}{r}$ such that $\left|\frac{s}{r}-\varphi\right| \leq \frac{1}{2r^2}$ then $s/r$ is a convergent of the continued fractions for $\varphi$, and thus can be calculated in $O(L^3)$ steps.
Since $\varphi$ is accurate to $2L+1$ bits it follows
$\left|\frac{s}{r}-\varphi\right| \leq \frac{1}{2^{2L+1}} \leq \frac{1}{2r^2}$ since $r \leq N \leq 2^L$. Thus this theorem applies.

#### Functionality
Since $P \in N=2$. Thus the theorem applies.

Express real numbers by integers

$[a_0, a_1, ..., a_M] = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{... + \cfrac{1}{a_M}}}}$

#### Example 
Imagine that $S=5$ and $r=6$
such that $\varphi = \frac{5}{6}= 0.833...$

Imagine we have measured the outcome
$\tilde{\varphi} = 0. \varphi_1 \varphi_2 \varphi_3 \varphi_4 \varphi_5 = 0.110101$
meaning $\tilde{\varphi} = 1 \cdot \frac{1}{2} + 1 \cdot \frac{1}{4} + 0 \cdot \frac{1}{8} + 1 \cdot \frac{1}{16} + 0 \cdot \frac{1}{32} + 1 \cdot \frac{1}{64} = \frac{53}{64}$

Write $\frac{53}{64}$ as a continued fraction:

$\frac{53}{64} = 0 + \frac{1}{\frac{64}{53}} = 0 + \frac{1}{1 + \frac{11}{53}}$

$= 0 + \frac{1}{1 + \frac{1}{\frac{53}{11}}} = 0 + \frac{1}{1 + \frac{1}{4 + \frac{9}{11}}}$

$= 0 + \frac{1}{1 + \frac{1}{4 + \frac{1}{1 + \frac{2}{9}}}}$

$= 0 + \frac{1}{1 + \frac{1}{4 + \frac{1}{1 + \frac{1}{4 + \frac{1}{2}}}}}$

$\implies [a_0, ..., a_5] = [0, 1, 4, 1, 4, 2]$

Continued fraction algorithm requires $O(L^3)$ steps.

If we stop after 1 step: $\frac{1}{1} \leftarrow$ not $r$
" 2 steps: $\cfrac{1}{1 + \cfrac{1}{4}} = \frac{4}{5} \leftarrow$ not $r$
" 3 steps: $\cfrac{1}{1 + \cfrac{1}{4 + \cfrac{1}{1}}} = \frac{5}{6} \leftarrow$ found $r!$ $\checkmark$

The algorithm provides efficiently numbers $\frac{s'}{r'}$.
The denominator $r'$ is our candidate for the order $r$.
We can check whether $r'$ is the order by calculating $x^{r'} \pmod{N}$, and if this is $=1$, we have found $r$. Checking solutions in NP are always efficient.

### Costs
- [[Hadamard-Gate|Hadamard-gates]]: $O(L)$ gates
- Inverse [[Quantum Fourier Transform|FT]]: $O(L^2)$ gates
- Modular exponentiation: $O(L^3)$ gates
- Classical continued fraction algorithm: $O(L^3)$ gates
- Without proof: f the order finding attempt fails, one only needs to repeat a constant number of times to obtain the order r with high probability
$\Rightarrow$ Overall cost $O(L^3)$, this can be reduced to almost $O(L^2)$ by using known algorithms for fast integer multiplications modulo $N$

### The quantum algorithm
- Inputs:
	- Blackbox $U$ which performs $|j\rangle|k\rangle \rightarrow |j\rangle|x^jk \mod N \rangle$ for x being a coprime to the $L$-bit number $N$ to be factored
	- Use $t=2L+1 + \left\lceil \log{\left(2+\frac{1}{2 \varepsilon}\right)}\right\rceil$ qubits for the first register, prepared all in $|0\rangle$
	- Prepare $L$ qubits the second register in the $|1\rangle$ state
- Outputs:
	- The order $r$, i.e. the smallest integer $r$ for which $x^r=1 \mod N$
- Runtime:
	- $O(L^3)$ operations. Succeeds with probability $O(1)$
- Steps:
	0. $|0\rangle|1\rangle$
		- initial state of $t$ and $L$ qubits
	1. $\rightarrow \frac{1}{\sqrt{2^t}}\sum_{j=0}^{2^t-1} |j\rangle |1\rangle$
		- superposition through Hadamards
	2. $\rightarrow \frac{1}{\sqrt{2^t}}\sum_{j=0}^{2^t-1} |j\rangle |x^j \mod N\rangle$
		$\approx \frac{1}{\sqrt{r2^t}} \sum_{s=0}^{r-1} \sum_{j=0}^{2^t-1} \exp\left(\frac{2 \pi i s}{r}\right)|j\rangle |u_s\rangle$  
		- apply $U$ operations
	3. $\rightarrow \frac{1}{\sqrt{r}} \sum_{s=0}^{r-1} |\tilde{s/r}\rangle |u_s\rangle$
		- apply inverse [[Quantum Fourier Transform|FT]] to 1st register
	4. $\rightarrow \tilde{\varphi}=\tilde{s/r}$
		- measure 1st register
	5. $\rightarrow r$
		- apply continued fraction algorithm
### Circuit Implementation


### Next step
Factoring can be reduced to Order finding which is the most important ingredient in [[Shor‘s algorithm]]