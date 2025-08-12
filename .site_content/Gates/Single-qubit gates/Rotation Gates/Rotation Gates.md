Rotation Gates can be built from [[Pauli Gates]] like this:

$R_\sigma (\alpha) = \exp(-\frac{i \alpha}{2} \sigma)$
With deconstructing the Pauli matrices in the Taylor representation the following holds:
$R_\sigma (\alpha) = \cos\left(\frac{\alpha}{2}\right) \mathbb{1} - i \sin\left(\frac{\alpha}{2}\right) \sigma$
An arbitrary rotation on the [[Bloch sphere]] can be described as $R_\vec{n}(\alpha) = \exp\left(\frac{i \alpha}{2} \vec{n} \cdot \vec{\sigma}\right)=\cos{\frac{\alpha}{2}}\mathbb{I}-i \sin{\frac{\alpha}{2}}(\vec{n} \cdot \vec{\sigma})$ with $\vec{n} \cdot \vec{\sigma} = n_x X + n_y Y + n_z Z$.  
Arbitrary single-qubit rotations can be built up from rotations about two axes as:
$U=e^{i \alpha}R_\vec{n}(\beta)R_\vec{m}(\gamma)R_\vec{n}(\delta)$