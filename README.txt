# Description

I observed a complex phenomenon as I
entered the escalator down to the trains
today in Penn Station.
There was a large mass of people all congregated
by the entrance, pushing forward, trying to enter
the escalator doors. The problem is that the esacaltor
doors were small so there was congestion.

How do we model this situation mathematically
and computationally? What do the trajectories look
like for each starting location? What is the optimal
starting location.

We"ll start the simulation as a cellular automaton
and then build from there

-----

# Technical
Our V1 situation is going to be a 2D dimensional
cellular automata. It assumes the following

- Agents can only move one block per turn (i.e. cannot speed up if they wanted to)
- The board is discrete, and hence agents cannot squeeze between eachother.
- There is only one destination cluster. More advanced simulations can user more than one cluster.
I'll start with production rules for a stupid
system, i.e. one that does not learn.
After I analyze the results from that simulation,
I'll go for more complexity, but I'd like to start
simple.

P_t is the environment matrix for each agent at timestep t,
depicting environment cell inhabitances around the agent's
own cell.

Now we are assuming there is only one limit attractor,
so the agent moves to the P_ij closest to DESTINATION.

Which metrics to analyze for?

- Flow rate
- Size of destination
- Derivative of closeness to destination as a function of starting location.

We start with a queue of N people and start dispatching them
with a probability drawn from a poisson distribution each timestep.

I===@@@===@@@===@@@===@@@I
I         Notes          I
I===@@@===@@@===@@@===@@@I
- Last year I was wondering how mazes could be characterized.
  Now I have the poser of statistics on my side and can deploy it
  anywhere data needs to be understood. The robot can
  learn the distribution of passageway direction switching,
  passageway lengths, etc. which could factor into his decision making.
  This approach would only produce meaningful benefits when the distributions
  are irregular, and hence not random.
