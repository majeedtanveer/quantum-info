The trace of any operator is the sum of diagonal elements in any orthonormal basis.
$\mathrm{tr}=\sum_{y=1}^d \langle \varphi_y | \rho | \varphi_y \rangle, \langle \varphi_y | \varphi_{y’} \rangle = \delta_{yy’} \Rightarrow \sum_y | \varphi_y \rangle \langle \varphi_y | = \mathbb{I}$

The trace has cyclic properties:
$\mathrm{tr}(AB)=\mathrm{tr}(BA)$
$\mathrm{tr}(|a\rangle \langle b |)=\langle b | a \rangle$
$\mathrm{tr}(|a\rangle \langle b |A)=\langle b |A| a \rangle=\mathrm{tr}(A|a\rangle \langle b |)$

The trace equals the sum of diagonal elements in any complete set of $n\geq d$ vectors
$\mathrm{tr}=\sum_{y=1}^n \langle \pi_y | \rho | \pi_y \rangle, \sum_y | \pi_y \rangle \langle \pi_y | = \mathbb{I}$

The partial trace is calculated as follows:
$\mathrm{tr}_B(\rho_{AB})=\sum_j(\mathbb{I}_A\otimes\langle j |)\rho_{AB}(\mathbb{I}_A\otimes| j\rangle)=\rho_A$