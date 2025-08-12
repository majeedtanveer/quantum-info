### Problem
- The problem of factoring: Given a positive **composite** integer number $N$, what are the prime factors multiplied together equaling $N$?
- A fast algorithm for order finding can be converted into a fast algorithm for factoring
- Factoring is believed to be hard on classical computers: For an $L$-bit integer $N$, the best classical algorithms known to date (number field sieve) require roughly $\exp(O(L^{1/3}))$ operations. This is exponential in the number of bits describing the number $N$
### Reduction
We can find a factor of $N$ if we find a non-trivial solution of $y^2= 1 \mod N$. There are always two trivial solutions:
$y=1$ and $y=-1 \equiv (N-1) \mod N$
However if N is divisible by two distinct odd primes, these are at least two more non-trivial square roots in $\mathbb{Z}^*_N$ (i.e. among the set of numbers between 1 and $N-1$, which are coprime with N):
$$
\begin{aligned}
&y^2-1= (y+1)(y-1)= 0 \mod N \\
&\rightarrow (y+1)(y-1)= k \cdot N \quad \text{for some k}
\end{aligned}
$$
If $y \neq \pm 1 \mod N$, then neither $y+1$ nor $y-1$ is a multiple of $N$.
$\Rightarrow$ In that case, the greatest common divisors $\gcd(y+1,N)$ and $\gcd(y-1,N)$ must each be proper divisors of $N$, i.e. prime factors we are looking for.
How can we find a non-trivial square root $y$?
$\Rightarrow$ Choose a random integer $x$, $1 < x \leq N-1$, check whether $x$ is coprime of $N$. If it‘s not coprime, $N$ and $x$ share a prime factor, which we can easily find and we are done. If $x$ is coprime $x$ of $N$, then run the [[Quantum Order Finding]] algorithm to find $r$:
$$
\begin{aligned}
& \quad \quad x^r= 1 \mod N \\
&\Leftrightarrow (x^{r/2})^2 = 1 \mod N\\
&\Leftrightarrow (x^{r/2}+1)(x^{r/2}-1) = 0 \mod N\\
&\Leftrightarrow (x^{r/2}+1)(x^{r/2}-1) = k \cdot N \quad \text{for some k}
\end{aligned}
$$
In other words if we are lucky and the order $r$ is even, then $y=x^{r/2}$ is a square root of 1.
We know for sure that $x^{r/2} \neq 1 \mod N$, since $r$ is the smallest integer for which this is true. If we are again lucky and $x^{r/2} \neq -1 \mod N$ too, then $x^{r/2}$ is a **non-trivial** root.
We then can calculate $\gcd(x^{r/2}+1,N)$ and $\gcd(x^{r/2}-1,N)$ to find non-trivial prime factors. Calculating gcd is efficient (Euclid‘s algorithm).

### Example
$N=21$
Choose e.g. $x=2$ $\Rightarrow x^6=64 \mod 21=1$
$\Rightarrow$ order $r=6$
Check: $x^{r/2}=2^3 = 8 \neq -1 \mod 21$
$\Rightarrow$ 8 is a non-trivial square root of 1 in $\mathbb{Z}^*_{21}$.
$\Rightarrow \gcd(9,21)=3$ and $\gcd(7,21)=7$
### Success Probability
The number of elements of good coprimes where their order $r$ is even and $x^{r/2} \neq -1 \mod N$ can be determined in the following:
#### Theorem (without proof)
If $N$ us divisible by $l$ distinct odd primes, then at least a fraction $1-\frac{1}{2^{l-1}}$ of the elements in $\mathbb{Z}^*_N$ are good.
$\Rightarrow$ Thus, for $l\geq2$, the probability to pick a good coprime $x$ is at least $1/2$.
$\Rightarrow$ We need only $O(1)$ trials.
### Resource Discussion
Shor‘s quantum algorithm for factoring requires $O(1)$ runs of the quantum algorithm for order finding.
$\Rightarrow$ Overall $O(L^3)$ runtime
$\Rightarrow$ Compared to classical runtime $\exp(O(L^{1/3}))$ 
$\Rightarrow$ Exponential speedup