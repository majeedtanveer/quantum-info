This makes use of [[Quantum Fourier Transform|QFT]].
### Setting
Suppose that a unitary $U$ has an eigenvector $|u \rangle$ with eigenvalue $e^{2 \pi \varphi}$, where $\varphi$ is unknown.
The goal is to estimate $\varphi$ (Note that $0 \le \varphi < 1$).
Assumptions: We have black boxes that prepare $| u \rangle$ and peform controlled-$U^{2^j}$ operations, for suitable non-negative integers $j$
### The algorithm
#### Functionality
- We will have two qubit registers:
	- The first register contains $t$ qubits intitially in $|0\rangle$
	- The choice of $t$ will depend on
		- The desired number of digits of accuracy of the estimate of $\varphi$
		- The desired success probability with which we wish the phase estimation procedure to be successful
	- The second register begins in $|u\rangle$, containing as many qubits as are necessary to store $|u\rangle$
- First we create an unbiased superposition by putting [[Hadamard-Gate|H-Gates]] for all $t$ qubits for the first register. Then we do $n$ controlled-$U^{2^j}$ operations on the second register which is controlled by the $j$th qubit on the first register. Consider one qubit of the first register, and $|u\rangle$
	$$
	\begin{align}
	|0\rangle | u \rangle &\xrightarrow{H}\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|u\rangle \\
	&\xrightarrow{C-U^{2^j}} \frac{1}{\sqrt{2}}(|0\rangle|u\rangle + |1\rangle U^{2^j} |u\rangle \\
	&= \frac{1}{\sqrt{2}}\left(|0\rangle + e^{2 \pi i \left(2^j \varphi\right)} |1\rangle\right)|u\rangle \\
	\rightarrow \text{Output states:} \\
	&\frac{1}{\sqrt{2^t}} \sum_{k=0}^{2^t-1} e^{2 \pi i \varphi k} |k\rangle |u\rangle\\
	&=\frac{1}{\sqrt{2^t}}\left(|0\rangle + e^{2 \pi i 0.\varphi_t} |1\rangle\right)\left(|0\rangle + e^{2 \pi i 0.\varphi_{t-1}\varphi_{t}} |1\rangle\right)\left(|0\rangle + e^{2 \pi i 0.\varphi_{t_1}…\varphi_{t}} |1\rangle\right) |u\rangle \\
	&\xrightarrow{\text{FT}^\dagger} |\varphi \rangle|u\rangle = |\varphi_1\rangle |\varphi_2\rangle…|\varphi_t\rangle |u\rangle
	\end{align}
	$$
All computational basis states are encoded in binary representation $|k\rangle$. Example: so the output state for t=4 k=3 is $\frac{1}{4}|0\rangle|0\rangle e^{2 \pi i \left(2^1 \varphi\right)}|1\rangle e^{2 \pi i \left(2^0 \varphi\right)}|1\rangle=\frac{1}{4}|0\rangle|0\rangle|1\rangle|1\rangle e^{2 \pi i \varphi\cdot3}=\frac{1}{4}|3\rangle e^{2 \pi i \varphi\cdot3}$. The measurement of the qubits on the first register provides us $\varphi$ exactly.
#### Algorithm steps summary
1. Hadamard gates on all qubits of register 1
2. Controlled-$U$ operations on the second register, with $U$ raised to successive power of 2, controlled by the qubits of the first register
3. Apply the inverse QFT 
4. Measure the qubits of the first register in the computational basis

### Circuit implementation

### Discussion of performance and requirements
- In general $\varphi$ can‘t be written exactly as binary $t$-bit expansion
- One can show that if one wants to get an approximate estimate for $\varphi$ to an accuracy $2^{-n}$, and one wants the probability to obtain an estimate of this precision to be at least $1-\varepsilon$, one needs to choose the number of qubits in the first register as  $$ 
t= n + \left[\log{\left(1+\frac{1}{2 \varepsilon}\right)}\right]
$$
$\Rightarrow$ This is a small additional increase only (linear in $n$)
What if we can‘t prepare $|u\rangle$?
Let’s start in some other state $|\psi\rangle$ instead, which can be written as $|\psi\rangle=\sum_u c_u |u\rangle$ with eigenstates $|u\rangle$ of $U$, with eigenvalues $e^{2 \pi \varphi_u}$. The output of the quantum phase approximation circuit will be $\sum_u c_u |\tilde{\varphi}_u \rangle |u \rangle$, where  $\tilde{\varphi}_u$ is a good approximation to the eigenvalue $\varphi_u$.
Measurement of the first register will then yield with probability $|c_u|^2$ the approximate value $\tilde{\varphi}_u$.
$\Rightarrow$ We can avoid preparing $|u\rangle$ at the expense of introducing some additional randomness into the algorithm

### Iterative Quantum Phase Estimation
It is also possible to estimate the phase in an iterative process. First the following circuit with controlled $U_{n-j}$ by the ancillas is being applied with a measurement in the [[X Gate|X]]-basis, for qubits 2,…,n additional unitaries controlled by the $(j-1)$th classical bit given by the X-measurement $R_{j}^{\dagger}R_{j-1}^{\dagger}…R_2^{\dagger}$ are added before the measurement.

#### Circuit Implementation