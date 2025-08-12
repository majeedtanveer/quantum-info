> [!IMPORTANT] There exists no physical procedure to copy any **arbitrary** quantum state $|\psi \rangle$

Proof:
Imagine that such an operation $U$ exists, which performs the following map:

Consider two input states $|\psi \rangle$ and $|\phi \rangle$:
$|\psi \rangle | s \rangle \xrightarrow{U} |\psi \rangle |\psi \rangle$
$|\phi \rangle | s \rangle \xrightarrow{U} |\phi \rangle |\phi \rangle$

$|\psi \rangle |\psi \rangle = U |\psi \rangle | s \rangle$
$|\phi \rangle |\phi \rangle = U |\phi \rangle | s \rangle$

Take the inner product:
$(\langle \psi|\langle \psi|)(|\phi \rangle |\phi \rangle) =\langle \psi|\langle s|U^\dagger U|\phi \rangle |s \rangle$
$\Rightarrow \langle \psi | \phi \rangle^2 = \langle \psi | \phi \rangle \langle s | s \rangle$
$\Rightarrow \langle \psi | \phi \rangle^2 = \langle \psi | \phi \rangle$
which is only true, if $|\psi \rangle$ and $|\phi \rangle$ are either equal or orthogonal
$\Rightarrow$ We can't copy states $|\psi \rangle$ and $|\phi \rangle$ that are not orthogonal.