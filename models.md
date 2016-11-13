Let's have a discussion here about various models for crowd simulation. 

**Naiive Automata Model**:

I initially tested a naiive automata model where each agent moves to it's adjacent cell closest to the goal. I observed a number of problems with this. 

- Not invariant under the order of node updates. 
- No memory, nodes can continually revisit the same location
- No velocity, nodes can get stuck

**Discretized Space Model**:

The second model I conceptualized but haven't yet implemented is a discretized space model. It should be extensible to modelling any number of agents – so it will be markovian. Models the evolution of probability densities for n agents to be in the (i,j)th bin. 

There is a 

**Probabalistic Model:**

**Agent Based Model:**
