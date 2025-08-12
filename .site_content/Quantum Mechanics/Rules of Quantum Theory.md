 
### Definitions
#### Set of Rules

| System | Set of Rules | Elements  | Probability Generation     | Events             | Experiment | Information loss |
| -----: | ------------ | --------- | -------------------------- | ------------------ | ---------- | ---------------- |
| Closed | Broad        | Vectors   | Indirectly from amplitudes | pure               | Special    | None             |
|   Open | Different    | Operators | Directly                   | Generally non-pure | General    | Some             |
In quantum theory switching between systems is always possible.through purifying and coarse graining respectively.

![[Images/Pasted image 20250729131634.png]]

Open quantum systems are obtained from closed quantum systems by discarding information.

#### Operational Circuit
An **Operational Circuit** is directed from right to left and contain **no** loops. It is drawn as equations are written. It represents the **joint probability** of outcomes of an experiment as function of the events. All events jointly combine the probability of one possible set of outcomes (zyx) of the experiment. Orthogonal (co)vectors are denoted by the symbol $\varphi$.

Rounded boxes $\equiv$ Events
Single wires $\equiv$ Quantum Systems
Double Wires $\equiv$ Classical information about outcomes in the lab frame

Boxes in time (in series) are connected by single wires (same lab frame) and boxes in space (in parallel) are not connected by single wires (different lab frames)
#### Experiment
A complete process involving the composition of quantum events that produce outcomes across multiple spatially separated laboratories, where each lab is accessible to agents who can communicate and condition or control their future choice of quantum operations or measurement devices based on prior information.
$\Rightarrow$ Devices (or events they produce) are distinguished by their number of input and output quantum systems
![[Images/Pasted image 20250729130522.png]]
#### Event
An **event** is a specific outcome resulting from one use of a device (like a measurement or operation), chosen among several possible alternatives, and fully described in terms of what happened in the lab during that operation. Preparations are also called states collected into ensembles, are also called Effects collected into positive-operator-valued-measures, POVMs)

![[Images/Pasted image 20250729132150.png]]

### General
Quantum Theory is operationally defined by assigning mathematical objects $m$ to the systems Operational Quantity $Q$ by a set rules ($Q=m$) together with a rule to compute probabilities in the lab frame directly from these objects $p_m=f(m)$.
There are three probabilistic concepts important for these rules (not specific to quantum theory):
- Probabilistic $\leftrightarrow$ Deterministic: Number of outcomes (outgoing $\Downarrow$)
- Conditioning outcome $\rightarrow$ Conditioned choice: Outcomes $\rightarrow$ Incomes (outgoing $\Uparrow$)
- Non-pure $\leftrightarrow$ Mixed: Probabilistic simulation with/out conditioning?
These concepts are all effected by coarse graining.

#### Probabilistic $\leftrightarrow$ Deterministic
The devices are distinguished by the number of possible set of events (outcomes) that they produce in the lab. A deterministic device only produces **one** event (thus $\Downarrow$ is omitted) while a probabilistic device have at least **two** possible events (thus $\Downarrow$ is needed to specify). The deterministic device is not providing new information to the system. Those devices are indicated by a hat (e.g. $\hat{\psi}$)
![[Images/Pasted image 20250729135334.png]]

**Coarse Graining** (denoted by the „garbage bin“ at the end of the double arrow) over all possible events of a probabilistic device produces (or simulates) a deterministic device. The coarse grained device generates the probabilities of the probabilistic device summed over the discarded outcomes. Discarding a system means discarding all outcomes  of any observation test performed on it
![[Images/Pasted image 20250729140112.png]]

#### Conditioning of choices
Agents in the lab frame can choose which devices to use in a circuit during a experiment. Once a possible outcome has been chosen and run it collapses into that path. Conditioned choices are noted by an up arrow $\Uparrow$ and a conditioning bar $|$ for probabilistic devices. For deterministic devices the conditioning bar is not necessary and only the device label is noted.
![[Images/Pasted image 20250729140952.png]]

Outcomes produced probabilistically can be used to condition other devices, this is a simulation of a new device which jointly produces all the outcomes.
![[Images/Pasted image 20250729141731.png]]

#### Pure events/devices
A pure event is an elementary event which has no underlying non-trivial probabilistic explanation. A pure event can not be simulated non-trivially. The purity of devices is the only operational assumption distinguishing the closed and open system quantum rules. Thus for pure events we use the notation for closed systems in the open system picture to indicate that. All pure events are Rank 1 projectors ($P=P^\dagger, P=P^2$ or Number of non-zero eigenvalues=1). Operators can only describe **pure** transformations!
E.g. for preparation (This is similar for transformations and observations): $\sum_{x’}\rho’_{Ax’,x}=\sum_{x’}p_{x’|x}\psi_{Ax’}=\psi_{Ax}$  

![[Images/Pasted image 20250729150634.png]]

Example:
	$\psi_x=|0\rangle \langle 0 |$ can not be written as a probabilistic composition other than itself ($\sum_{x’=0}p_{x’|x}\psi_{x} =1 \cdot |0\rangle \langle 0 |=\psi_x$) and has a rank of 1 and is thus pure but $\rho’_x=\frac{1}{2}(|0\rangle \langle 0 |+|1\rangle \langle 1 |)$ can be written as a probabilistic composition of other preparations ($\sum_{x’=0,1}p_{x’|x}\rho_{x} =\frac{1}{2} \cdot |0\rangle \langle 0 | + \frac{1}{2} \cdot |1\rangle \langle 1 | =\rho’_x$) and is thus non-pure. The rank is also 2.

#### Mixed $\neq$ Non-pure
Devices that are mixed are always also non-pure, but not all non-pure events are mixed (except for preperations)! A mixed device can be simulated by coarse graining of device choices conditioned on a random variable. Thus the event is not mixed if the probabilities adding up are greater than one ($\sum_{i}p_i \geq 1$).
$\sum_{x’}\rho_{Ax|x’}p_{x’}=\rho_{Ax}$  
Example:
- $\sum_{x=0,1}\rho_{Ax|x’}p_{x’} =\frac{1}{2} \cdot |0\rangle \langle 0 | + \frac{1}{2} \cdot |1\rangle \langle 1 | =\rho_x$ is a mixed preperation. And as shown before on-pure.
- $\mathbb{I}=|0\rangle \langle 0 | + |1\rangle \langle 1 |$ is not mixed because 1+1=2. This is also non-pure because the rank is 2. Thus this observation is neither pure nor mixed.
![[Images/Pasted image 20250730173216.png]]
### Causality

| **Open Systems**   | Any event can be non-pure                                                         |                                                                         |                                                               |
| ------------------ | --------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------- |
|                    | **Observation**                                                                   | **Transformation**                                                      | **Preperation**                                               |
| **Deterministic**  | $\hat{e}_B=\mathbb{I}_B$                                                          | $\hat{\mathcal{T}}_{B,A}$                                               | $\hat{\rho}_A$                                                |
| Test=Event         | $\mathrm{tr}_B(\hat{e}_B\bullet)=\mathrm{tr}_B(\bullet)$                          | $\mathrm{tr}_B(\hat{\mathcal{T}}_{B,A}\bullet)=\mathrm{tr}_A(\bullet)$  | $\mathrm{tr}_A(\hat{\rho}_A)=1$                               |
|                    | $\uparrow$ coarse grain                                                           | $\uparrow$ coarse grain                                                 | $\uparrow$ coarse grain                                       |
| **Probabilistic**  | $\{\varepsilon_{Bz}\}$                                                            | $\{\mathcal{T}_{B,Ay}\}$                                                | $\{\rho_{Ax}\}$                                               |
| Test               | $\mathrm{tr}_B(\sum_z\varepsilon_{Bz}\bullet)=\mathrm{tr}_B(\mathbb{I}_B\bullet)$ | $\sum_y\mathrm{tr}_B(\mathcal{T}_{B,Ay}\bullet)=\mathrm{tr}_A(\bullet)$ | $\sum_x \mathrm{tr}_A(\rho_{Ax})=1$                           |
| Events             | $\mathrm{tr}_B(\varepsilon_{Bz}\bullet)\leq\mathrm{tr}_B(\mathbb{I}_B\bullet)$    | $\mathrm{tr}_B(\mathcal{T}_{B,Ay}\bullet)\leq\mathrm{tr}_A(\bullet)$    | $\mathrm{tr}_A(\rho_{Ax})\leq1$                               |
|                    | $\uparrow$ coarse grain                                                           | $\uparrow$ coarse grain                                                 | $\uparrow$ coarse grain                                       |
| **Relations**      | $\varepsilon_{Bz}=\sum_{z’}\|\pi_{Bzz’}\rangle\langle\pi_{Bzz’}\|$                | $\mathcal{T}_{B,Ay}=\sum_{y’}T_{B,Ayy’}\bullet T^{\dagger}_{B,Ayy’}$    | $\rho_{Ax}=\sum_{x’}\|\psi_{Axx’}\rangle\langle\psi_{Axx’}\|$ |
|                    | $\downarrow$ pure case                                                            | $\downarrow$ pure case                                                  | $\downarrow$ pure case                                        |
| **Closed Systems** | **Every event is pure**                                                           |                                                                         |                                                               |
|                    | **Observation**                                                                   | **Transformation**                                                      | **Preperation**                                               |
| **Deterministic**  | (none)                                                                            | $\hat{T}_{B,A}$                                                         | $\|\hat{\psi}_A\rangle$                                       |
| Test=Event         | (none)                                                                            | $\hat{T}^{\dagger}_{B,A}\hat{T}_{B,A}=\mathbb{I}_A$                     | $\langle\hat{\psi}_A\|\hat{\psi}_A\rangle=1$                  |
| **Probabilistic**  | $\langle\pi_{Bz}\|$                                                               | $T_{B,Ay}$                                                              | $\|\psi_{Ax}\rangle$                                          |
| Test               | $\sum_{z}\|\pi_{Bz}\rangle\langle\pi_{Bz}\|=1$                                    | $\sum_yT^{\dagger}_{B,Ay}T_{B,Ay}=\mathbb{I}_A$                         | $\sum_{x}\|\psi_{Ax}\rangle\langle\psi_{Ax}\|=1$              |
| Events             | $\|\pi_{Bz}\rangle\langle\pi_{Bz}\|\leq1$                                         | $T^{\dagger}_{B,Ay}T_{B,Ay}\leq\mathbb{I}_A$                            | $\|\psi_{Ax}\rangle\langle\psi_{Ax}\|\leq1$                   |
Note: To check operators against other operators (e.g. $\varepsilon_{Bz}\leq\mathbb{I}_B$) you check the eigenvalues against each other(e.g. $\lambda_{\varepsilon1} \leq 1, \lambda_{\varepsilon2} \leq 1$). There is no deterministic observation in the closed system. 

#### Pretty Good Constructions
Pretty good constructions reversing the causal order ($\rho_{Ax} \rightarrow \mathrm{tr}(\bar{\varepsilon}_{Ax} \bullet)$, $\mathrm{tr}(\varepsilon_{Ay} \bullet) \rightarrow \bar{\rho}_{Ay}$) are indicated by overbar $\bar{x}$. The probabilities for the pretty good experiments are the same as for the original experiment. Mind that the order of devices don‘t change and use that the [[Trace]] is cyclic and the rules for complex conjugate in the braket formalism. In the open system the probabilities and in the closed system the amplitudes stay the same for $\dagger \rightarrow T$.
**Open systems**:
$\bar{\varepsilon}_{Ax}=\left(\sqrt{\frac{1}{\hat{\rho}_A}}\rho_{Ax}\sqrt{\frac{1}{\hat{\rho}_A}}\right)^{\dagger} \geq 0 \Rightarrow \sum_x\bar{\varepsilon}_{Ax}=\mathbb{I}_A$ 
With $\hat{\rho}_{A}=\sum_x\rho_{Ax}$ assumed invertible
$\bar{\rho}_{Ay}=\left(\sqrt{\hat{\rho}_A}\varepsilon_{Ay}\sqrt{\hat{\rho}_A}\right)^{\dagger} \geq 0 \Rightarrow \sum_y\bar{\rho}_{Ay}=\mathrm{tr}_A(\hat{\rho}_{Ay})=1$
$\Rightarrow p_{yx}=\mathrm{tr}_A(\varepsilon_{Ay}\rho_{Ax})=\mathrm{tr}_A(\bar{\rho}_{Ay}\bar{\varepsilon}_{Ax})=\mathrm{tr}_A(\bar{\varepsilon}_{Ax}\bar{\rho}_{Ay})=\bar{p}_{xy}$
**Closed systems:**
$\langle \bar{\pi}_{Ax} | = \langle \psi_{Ax} | \sqrt{\frac{1}{\hat{\rho}_A}}=\left(\sqrt{\frac{1}{\hat{\rho}_A}} | \psi_{Ax} \rangle\right)^{\dagger} \Rightarrow \sum_x | \bar{\pi}_{Ax} \rangle \langle \bar{\pi}_{Ax}| =\sqrt{\frac{1}{\hat{\rho}_A}} \sum_x | \psi_{Ax} \rangle \langle \psi_{Ax}| \sqrt{\frac{1}{\hat{\rho}_A}}=\mathbb{I}_A$
With $\hat{\rho}_{A}=\sum_x|\psi_{Ax}\rangle\langle\psi_{Ax}|$ assumed invertible
$|\bar{\psi}_{Ay} \rangle = \sqrt{\hat{\rho}_A} | \pi_{Ay} \rangle = \left(\langle \pi_{Ay} | \sqrt{\hat{\rho}_A} \right)^\dagger \Rightarrow \sum_y \langle \bar{\psi}_{Ay} | \bar{\psi}_{Ay}\rangle =\sum_y \langle \pi_{Ay} |\hat{\rho}_A|\pi_{Ay}\rangle=\mathrm{tr}_A(\hat{\rho}_A)=1$
$\Rightarrow a_{yx}=\langle\pi_{Ay}|\psi_{Ax}\rangle=\langle\bar{\psi}_{Ay}|\bar{\pi}_{Ax}\rangle=(\langle\bar{\pi}_{Ax}|\bar{\psi}_{Ay}\rangle)^*=(\bar{a}_{xy})^*$
![[Images/Pasted image 20250804144140.png]]

#### Perfect Distinguishability
Perfectly distingushable preparations and observations are the **only ones** equal to their adjoint pretty good construction. So preparations and observations seem only the same if one assumes perfect distinguishability
$$
\langle \check{\varphi}_{Ax}| \hat{\varphi}_{A|x} \rangle = \delta_{yx} \iff
\begin{cases}
\langle \overline{\hat{\varphi}_{A|x}}| = \left[ \sqrt{p_x} \langle\hat{\varphi}_{A|x}| \right] \left[ \frac{1}{\sqrt{\hat{\rho}_A}} \right] = \langle \hat{\varphi}_{A|x}| = \left( | \hat{\varphi}_{A|x}|\rangle \right)^{\dagger} \\
|\overline{\check{\varphi}_{Ax}} \rangle = \left[ \frac{1}{\sqrt{p_x}} \right] \left[ \sqrt{\hat{\rho}_A} |\check{\varphi}_{Ax} \rangle \right] = |\check{\varphi}_{Ax} \rangle = \left( \langle\check{\varphi}_{Ax} | \right)^{\dagger}
\end{cases}
$$
$$\text{with} \quad \hat{\rho}_A := \sum_x p_x |\hat{\varphi}_{Ax} \rangle \langle \hat{\varphi}_{Ax}|$$