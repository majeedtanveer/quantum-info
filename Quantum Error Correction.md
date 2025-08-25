### Basics
The error rates of Quantum computation applications for guaranteed quantum advantage in the fault taulerant regime needed are $10^{-14}/10^{-15}$. This is why Quantum Error Correction is very important in the [[Route to large-scale fault tolerant quantum computing.canvas|Route to large-scale fault tolerant quantum computing]]. The coupling to the environment causes decoherence, for example magnetic field fluctuations.  Dephasing can happen in a mixed state in an open system simulated by pure coherent superposition states, which leads to the loss of phase information. Other than that [[X Gate|X-errors]], [[Y Gate|Y-errors]] and [[Z Gate|Z-errors]] could happen as well as leakage and qubit loss.

### Classical
In classical error correction redundancies are introduced, for example n-bit repetition code, with majority vote as correction strategy. The repetition code fails if more than half of the bits suffer errors (bit flips).

### Quantum
#### Caveats
Redundancy can **not** work in the quantum case due to the [[No-Cloning Theorem]]. Also we can't directly measure quantum states to find out about the errors that occurred. This leads to a collapse of the wave function.

$\alpha | 0 \rangle + \beta | 1 \rangle \rightarrow | 0 \rangle \; \text{or}\;  | 1 \rangle$, information about $\alpha$ and $\beta$ lost ($M_z$).
even worse for entangled states
$\alpha | 000 \rangle + \beta | 111 \rangle \rightarrow | 000 \rangle \; \text{or}\;  | 111 \rangle$ by measuring one of the qubits only ($M_{z_1}$).
$\Rightarrow$ Measuring a single qubit collapses the state!

#### Error types
|     Error type | Example                                                                                     | Error operator |
| -------------: | ------------------------------------------------------------------------------------------- | -------------- |
|       Bit flip | $\|0\rangle\rightarrow\|1\rangle$                                                           | X              |
|     Phase flip | $\alpha \| 0 \rangle+ \beta \| 1 \rangle\rightarrow\alpha \| 0 \rangle- \beta \| 1 \rangle$ | Z              |
| Bit+Phase flip | $\alpha \| 0 \rangle+ \beta \| 1 \rangle\rightarrow\alpha \| 1 \rangle- \beta \| 0 \rangle$ | Y              |
Errors in quantum information are intrinsically continuous (rather than discrete):
Example: Undesired perturbation Hamiltonian $H \propto X$
$U(t)= \exp(-iHt)=e^{-i\phi X}=\cos \phi \mathbb{I} - i \sin \phi X$
$\Rightarrow U(t) |\psi\rangle=\cos \phi |\psi\rangle - i \sin \phi X |\psi\rangle$
$\Rightarrow p_e = \sin^2 \phi, 1-p_{e} = \cos^2 \phi$

The effective error model we use in the following are stochastic, independently distributed (uncorrelated) X,Y,Z errors with probability $p$.

### Codes
By constructing [[logical qubits]] a quantum repetition code can be constructed such as the [[3-qubit code]]. The code can detect $d-1$ errors and correct $(d-1)/2$ errors.

#### Stabilizer formalism
Stabilizer states are a set of commuting observables which allow to describe a large class of multi-qubit states including all QEC codes considered here.
Example: Bell states are stabilizer states, e.g.:
$|\Phi^+\rangle=\frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$
Stabilizers $S_1=Z_1Z_2$ and $S_2=X_1X_2$
$|\Phi^+\rangle$ is a unique 2-qubit state $|\psi\rangle$ for which
$S_1 |\psi\rangle=+|\psi\rangle, \quad S_2 |\psi\rangle=+|\psi\rangle$
All stabilizers commute $[S_i,S_k]=0$ and span a $2^{n}$ dimensional Abelian group. The Stabilizer state is uniquely fixed to $|\psi\rangle$ by imposing $S_i|\psi\rangle=+|\psi\rangle$ for $i=1,…,n$. The stabilizers span the n-dimensional subspace which is called the codespace. Also logical operators $Z_L$ and $X_L$ can be defined which fulfill the following:
$Z_L|0\rangle_L=|0\rangle_L$
$Z_L|1\rangle_L=-|1\rangle_L$
$X_L|0\rangle_L=|1\rangle_L$
$X_L|1\rangle_L=|0\rangle_L$
Logical operators need to commute with the stabilizers, $[O_L,S_i]=0$, and mutually anticommute, $\{X_L,Z_L\}=0$. Essentially one counts the number of anticommutes $\{X_i,Z_i\}=0$ and if its even, hen it commutes otherwise it anticommutes.

- A distance-$d$ QEC code can correct $\lfloor{\frac{d-1}{2}}\rfloor$ errors.
- A distance-$d$ QEC code can detect $d-1$ errors.
- There exist weight-$d$ errors that directly induce an (undetectable) logical error
Generally QEC doesn‘t account for every single qubit error which is bound by the [[Quantum Hamming Bound]]
#### Improvements
These codes can concatenated, the advantage is that the failure probability of logical qubits gets exponentially suppressed as the system size increases. Assuming the gate error probability is $p<1/3$ the failure probability for the $L$'th layer is $p_\text{fail}= \frac{1}{3}(3p)^{2^L}$. One example of such concatenation of the 3-qubit code is the [[9-qubit Shor code]]. Other than that larger codes have a higher success probability. For an n-code with [[distance]] $d$ which is the minimal [[weight]] the error probability scales with $p_\text{fail}\approx\binom{n}{(d-1)/2}p^{(d+1)/2}$ for small $p$. The [[Quantum Threshold Theorem]] assumes that every component can fail and guarantees an error probability where arbitrary quantum computations can be performed efficiently. In practice the error threshold are very demanding ($10^{-5}…10^{-6}$).

#### Topological QEC codes
Idea:
-  topology = robust global features which are invariant under local changes or perturbations
- assumption: noise and errors act locally
- Store quantum information spread out globally to protect it against noise
The error thresholds are about $10^{-2}…10^{-3}$ and fault tolerant QC might be possible in practice! To what topological QEC codes are can be seen in .
Examples are the [[Kitaev‘s toric code]] and the [[Surface Code]]. The smallest 2D topological color code is the [[Steane Code]]