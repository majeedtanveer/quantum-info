The Bloch sphere is a three dimensional representation of a two-level quantum mechanical system. The [[Hilbert Space]] is two dimensional and the representation is a sphere. Each point of outside and inside the sphere represents a valid state. The Sphere has a radius of 1.
For qubits the North Pole of the sphere is the $| 0 \rangle$ state, the South Pole the $| 1 \rangle$ state. Those are the eigenstates of the [[Z Gate]]. On the positive end of the x-axis the state is the $| + \rangle$- state, on the negative end the $|- \rangle$- state. Those are the eigenstates of the [[X Gate]]. For the y-axis those are $| + \rangle_i$- state, on the negative end the $|- \rangle_i$- state. Those are the eigenstates of the [[Y Gate]]. States on the surface of the Bloch sphere are [[Pure states]]. States inside the Bloch sphere are [[Mixed States]]. The state in the origin of the Bloch sphere is a [[Maximally mixed state]]. 
A pure state in the Bloch sphere can be represented as follows:
$| \Psi \rangle = e^{i \gamma} \left(\cos{\frac{\theta}{2}} | 0 \rangle + e^{i \phi} \sin{\frac{\theta}{2}} | 1 \rangle \right)$ 
 $\theta \in [0, \pi]$ 
 $\phi \in [0,2 \pi)$
### Rotations
Rotations on the Bloch sphere are realized by the [[Rotation Gates]], which can transform any pure state into another states on the Bloch sphere. An arbitrary rotation can be described as $R_\vec{n}(\alpha) = \exp\left(\frac{i \alpha}{2} \vec{n} \cdot \vec{\sigma}\right)=\cos{\frac{\alpha}{2}}\mathbb{I}-i \sin{\frac{\alpha}{2}}(\vec{n} \cdot \vec{\sigma})$ with $\vec{n} \cdot \vec{\sigma} = n_x X + n_y Y + n_z Z$.  


![[Bloch sphere.png]]