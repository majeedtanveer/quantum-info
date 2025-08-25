How large must a Hilbert space be, so that one can accommodate a QEC code that fulfills the following conditions?
- n qubits, $k$ encoded qubits, error correction works for up to $t$ errors.
Reasoning: For $j \leq t$ errors, there are $\binom{n}{j}$ possible locations, 3 types of errors ($X,Y,Z$), thus a total number of possible errors $\sum_{j=0}^t\binom{n}{j}3^j$
The code space is $2^k$-dimensional and each error is required to map the codespace to an $2^k$-dim. Orthogonal subspace. All these subspace need to fit in the $2^n$-dim. Hilbert space:

$$
\sum_{j=0}^t\binom{n}{j}3^j\cdot2^k \leq 2^n
$$

For 1 logical qubit ($k=1$), 1 arbitrary correctable error ([[distance]] $d=3$) ($t=1$), this particularizes to:
$2(1+3n)\leq 2^n$
$\Rightarrow n \geq 5$ qubits needed for smallest complete code, with stabilizers and logical operators ($S_i$ are cyclic permuations)
$S_1=X_1Z_2Z_3X_4\mathbb{I}_5$
$S_2=\mathbb{I}_1X_2Z_3Z_4X_5$
$S_3=X_1\mathbb{I}_2X_3Z_4Z_5$
$S_4=Z_1X_2\mathbb{I}_3X_4Z_5$
$Z_L=Z_1Z_2Z_3Z_4Z_5$
$X_L=X_1X_2X_3X_4X_5$