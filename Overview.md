### Lectures
**BLOCK 1** (tentative list of topics covered)

1 - Overview and Introduction

2 - Quantum Gates and Circuits

3-A - Deutsch Algorithm

3-B - Deutsch-Jozsa Algorithm and Bernstein-Vazirani Problem

4 - Classical Computation  
5 - Universality of Quantum Gates  
6 - Computational Complexity  
7 - Grover Quantum Search Algorithm  
8 - Quantum Fourier Transform  
9 - Quantum Phase Estimation  
10 - Quantum Order Finding  
11-A - Shor Algorithm for Factoring  

**BLOCK 2**

Lecture 1 : Rules of Quantum Theory We formulate rules of quantum theory characterizing what is possible and what is not, making the role of information explicit.

• For open quantum ”systems” some information got lost : Non-pure events / circuits require a mathematically more complicated description which is, however, closer to an operational understanding of what goes on in the physics lab and to classical theory

• For closed quantum ”systems” there is no information that can get lost : Pure events allow a mathematically simpler description which is, however, not directly related to the physics in the lab or classical theory

We explore several ways these two formalisms are related. The goal is to master both and to be able switch between them at will.

The quantum rules mathematically contruct probabilities from Hilbert-space vectors/operators subject to a physical contraint of causality. But other than this, the rules of quantum theory are simply mathematically postulated without any deeper physical motivation beyond “experiments conﬁrm their predictions”. This leaves us to “discover the physics” by solving operational tasks of information processing. This is what Lecture 2-5 do systematically.

Terminology State vectors, density operators, ensembles, POVMs, channels, operations, instruments, isometries, non-orthogonal sets

Lecture 2 : Observations on Preparations With the quantum rules in hand we ﬁrst study the simplest quantum circuit where a single system A is prepared and then observations are performed to extract information contained in their joint probabilities :

1. We verify that the closed-system rules indeed only describe pure preparations based on the simulatability of the probability distributions that they can generate, and likewise for observations.

2. We then analyze non-pure preparations of open systems by bringing these into a standard simulation form, identifying what is “quantum” about them, and likewise for observations :

• Non-pure preparations are always mixtures with information encoded in the probabilities of mixing (like classically) but also in the freedom of choice of the pure states that are being mixed (unlike classically)

• Non-pure observation are always coarse-grainings involving pure observations (like classically) but the freedom of choosing these prohibits the simulation of any measurement by post-processing of a single pure observation device (unlike classically)

This “Non-uniqueness of prepation reﬁnement” and “No post-processings of ideal measurement” turn out to be the same thing.

3. We then analyze 2 basic tasks of information extraction :

• In tomography, we extract complete information characterizing an unknown preparation by a D-outcome observation on the quantum system

• In perfectly distinguishing, a known set of preparations is identiﬁed by a d-outcome observation device without extracting complete information about these states

(“Which one is it?”)

(“Which of these is it)

These task are related by D=d 2 expressing an “information gap” : Tomography is quadratically harder than perfectly distinguishing This is the operational signiﬁcance of the quantum rule “States are d×d positive matrices on a Hilbert space”

Terminology Measurement in orthogonal basis, IC-POVMs Lecture 3 : Steering a pure preparation

We next consider a quantum circuit where two systems are jointly prepared. A local measurement is performed to extract information from one system B and we investigate what classical communication B→A implies for the description of the other remote system A

1. With communication, this results in remote steering.

steering

The solution of this operational task leads to a characterization of all pure, correlated states These correlations are not simulatable by coarse-graining of coordinated local preparations (unlike classically)

2. Without communication there is no remote eﬀect as dictated by causality.

The solution of the inverse operational task, puriﬁcation, leads to a pure, correlated simulation of any remote non-pure state of an open system (classically impossible). The “non-uniqueness of mixture reﬁnement of preparation” of Lecture 2 is fully characterized.

3. The non-locality of entanglement is shown to limited by the locality of quantum tomography, the ability to characterize any quantum state by local observations (like classically): Entanglement is monogamous correlation, non-shareable by more than 2 parties

Terminology Entanglement, Schmidt decomposition of bipartite vectors, SVD, partial trace

**BLOCK 3** (tentative list of topics covered)  
12-A - Basic Concepts of Quantum Error Correction  
12-B - Stabiliser Formalism and Complete Codes  
13-A - Introduction to Topological QEC Codes  
13-B - Fault-Tolerant Universal Gates and Scalable Architectures

**BLOCK 4**

Lecture 4-5 systematically performs the analogous steps of Lecture 2-3 for transformations (measurements, evolutions) thereby completing the framework of essential results of quantum information theory :

Lecture 4 : Transformations

The next level of complexity is a quantum circuit involving transformations of the preparation of a single system. These can extract information about input state A before a further, ﬁnal observation is made on the disturbed output state B :

1. We verify that the closed-system rules indeed only describe pure transformations by the simulatability of the probability distributions that they generate. The purity of the identity transformation (“trivially doing nothing”) implies that nontrivial result that information-extraction implies disturbance of a quantum system, starting from clear-cut deﬁnitions based on probabilities in the lab.

2. We analyze non-pure transformations of open systems by again bringing them into a standard simulation form and we identify what is “quantum” about them :

• A non-pure transformation is always a coarse-grainings of some pure “transition” processes (like in classical theory) but there is freedom of choice in which “transitions” are coarse-grained (unlike classical theory)

• A non-pure transformation need not be a mixture (like classical theory)

This “non-uniqueness of reﬁnement” of transformations is remiscent of that of for states. This is no coincidence :

3. We again analyze 2 basic tasks of information extraction :

• Tomography, extracting complete information characterizing an unknown transformation, turns out to be possible by “encoding” the transformation in its modiﬁcation of pure entangled state and “decoding” it by using the corresponding state as resource for teleportation of input to output

• Perfectly distinguishing a known set of transformations likewise turns out to be possible by perfectly distinguishing these corresponding states

(“Which one is it?”)

(“Which of these is it?”)

The uncovered preparation-transformation correspondence is a key trick that allows to convert any result about preparations into a result about transformations and vice versa. This is systematically exploited in the ﬁnal lecture.

Terminology Kraus operators, (Sudarshan-)Kraus theorem, (de Pillis-)Choi-Jamiolkowski correpondence, HEWJ theorem Lecture 5 : Steering a pure transformation

Finally, the most complex quantum circuit we need to consider involves transformations jointly preparing two output systems AB taking input from one system C. A local measurement is applied to extract information from one output B and we investigate what classical communication B→A implies for the transformation outputting to the remote system A :

steering

1. With communication, this results in remote transformation steering.

The solution of this operational task leads to characterization of pure entanglement generating transformations

2. Without communication there is no remote eﬀect as dictated by causality.

The solution of the inverse operational task, transformation puriﬁcation, leads to a pure simulation of any non-pure transformation with remote output (classically impossible). The “nonuniqueness of transformation reﬁnement” in Lecture 4 is fully characterized.

3. The non-locality of entanglement generation is likewise shown to limited by the locality of quantum tomography : Entanglement is monogamous correlation, non-shareable by more than 2 parties.

Terminology Schmidt decomposition of isometries, Stinespring dilation, channels, operations, instruments

What will we learn ?

By systematically analyzing very basic operational tasks allowed by the rules of quantum theory and switching back and fort between closed- and open-system formalisms, we will derive all essential results in quantum information theory. In doing so, we illustrate :

Quantum theory is all about information. Quantum circuits are the calculations.

We stress that all the results can be –and often are– derived in mathematical style and discussed in purely mathematical language. This is not wrong, but it does leave the reader interested in physics to ﬁgure out what it is all about.

However, we will see time and again that the mathematics naturally follows from the operational physics. This is not a coincidence : All of the mathematics of quantum theory (ﬁnite dimension, without superselection) can be derived by solving the information processing tasks discussed in this lecture, starting from a few operational deﬁnitions and manipulating quantum circuits.

### Exercises

**BLOCK 1**

1.1 Circuit identities (few simple identities/rules)
1.2 SWAP gates (proof of swap gates and implementation from cnot, does swap gate create entanglement)
1.3 Deutsch algorithm (implementation)
1.4 Deutsch Josza algorithm (implementation)
2.1 Bernstein Vazirani (implementation)
2.3 Controlled-U gates )(controlled U Gate construction from single qubit unitaries)
3.1 n-controlled U gates (Implementation via controlled Vs, logical expression equivalent)
3.2 Grover 2-bit (Implementation)
3.3 Grover 3-bit (Implementation and optimal k)
4.1 Phase estimation (Alternative iterative approach)
4.2 Single qubit measurements on multipartite states (creation of GHZ and W-state with circuits)
4.3 Decomposition of multi qubit unitaries (Implementation of grey code)
5.1 Magic state and T-state injection
5.2 Shor‘s algorithm (Doing algorithm per hand)
5.3 Universal gate sets (alternative gate sets)

**BLOCK 2**

6.1 Physical validity of mathematical expressions  
6.2 Ensemble tomography with orthogonal measurements  

7.1 Conclusively distinguishing distinct states    
7.3 Tomographic preparation device

8.1 Conclusively distinguishing – Implementations

10.1 Basic qubit “noise” channels  

**BLOCK 3**

10.2 Quantum Error Correction (QEC) with a 7-Qubit Steane Code (How $[[7,1,3]]$ works and constructing other logical gates (e.g. $H_L$))

11.1 Quantum error correction of qubit loss (How it works and implementation)

**Block 4**

12.1 Correspondence Bell states ↔ Pauli transformations  
12.2 Teleportation and communication
