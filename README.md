# Exercise 7: Wumpus World

Demonstrate your comprehension of the knowledge-based agent design, and the rules
of the wumpus world problem.

## What to Do

Implement a WumpusWorldAgent that is a goal-based, knowledge-based agent, and
implement an agent function that uses a knowledge base to produce an action.
Your implementation should honor the specficiations of the KB-AGENT in the AIMA
book. Implement a WumpusWorld simulation within which your agent can operate. The
WumpusWorld represents the "real" physical WumpusWorld and its "physics" or rules,
and your implementation should honor the PEAS description of the wumpus world
found in the AIMA book.

## Instructions

Your agent needs help! Open and read `scratchpad.py`, and then run it.

`python 3 scratchpad.py`

You will find that the program has an error, because the WumpusWorld, KnowledgeBase,
and WumpusWorldAgent lack a complete implementation.

Complete the implementations of WumpusWorldAgent found in *wumpus_world_agent.py*,
KnowledgeBase found in *knowledge_base.py*, and the WumpusWorld found in
*wumpus_world.py*. Each class has an accompanying unit test suite. The tests should
all pass when your implementations are complete.

When complete, you should be able to run the code in `scratchpad.py` again and see
that the agent immediately climbs out of the cave.

We suggest the following steps.

### Step 1: WumpusWorldAgent

If you take a look at *scratchpad.py*, you will find an example of instantiating
a WumpusWorld, a KnowledgeBase and a WumpusWorldAgent. After analyzing the KB-AGENT
agent function specification, take a look at *wumpus_world_agent.py* to find a
WumpusWorldAgent class that has been stubbed for you.

Next, open the relevant test suite, *test_wumpus_world_agent.py* and notice that
all but the first test have been commented out. Run the test,

`python3 -m unittest test_wumpus_world_agent`

and notice that the first test is failing. Implement the necessary parameterized
constructor and ensure that the first test passes.

Then, uncomment the next test, run the test suite, notice the failure, and implement
what is necessary in order to get the test to pass. Repeat this procedure until
your agent passes all the tests.

When implementing the 'actuator' methods, we recommend that each actuator
method first `print`s a short message for convenience and visibility. For example,
in the implementation of `climb`, be sure to `print("Climbing out")`. In addition,
note that each actuator method will receive a WumpusWorld as an argument, representing
the real world in which the agent physically operates. As such, each actuator
method should exhibit a side effect in the world, by calling an appropriate method.
The tests inform you about these methods that should be called.

Note that, in this Exercise, we will not yet implement the *details* of the three
methods `make_percept_sentence`, `make_action_query`, or `make_action_sentence`.
These methods should be callable with the appropriate arguments, but they should
each just `pass` for now.

### Step 2: KnowledgeBase

If you take a look at *scratchpad.py*, you will notice that a KnowledgeBase is
instantiated and provided to the agent. And, you should have found that your
WumpusWorldAgent `action` method relies on this KnowledgeBase, per the KB-AGENT
specification. After analyzing the KB-AGENT agent function specification, take a
look at *knowledge_base.py* to find a KnowledgeBase class that has been stubbed
for you.

Next, open the relevant test suite, *test_knowledge_base.py* and notice that
all but the first test have been commented out. Run the test,

`python3 -m unittest test_knowledge_base`

and notice that the first test is passing. Uncomment the next test, run the test
suite, notice the failure, and implement what is necessary in order to get the
test to pass. Repeat this procedure until your knowledge base passes all the tests.

There are only two methods to implement, and we will not fully complete them
in this Exercise. For convenience, you will temporarily "stub" the implementation
of `ask` such that it returns the `climb` action.

When your agent and knowledge base are complete, try running *scratchpad.py* again,
and you should find that the agent's first action is to, very intentionally,
climb out of the cave.

### Step 3: WumpusWorld

If you take a look at *scratchpad.py*, you will notice that a WumpusWorld is
instantiated, that resembles the canonical example wumpus world found in the AIMA
book. The WumpusWorld represents a simulation of the *real physical environment*
within which the agent operates - not a state representation of the world. It
represents reality - not our agent's model of the state of the world nor its beliefs
of the state of the world. As such, it will emit the smells, sounds and other percepts
available to the agent, and it simulates the physical side effects resulting from
the agent's actions in the world. In *scratchpad.py*, you will find that the percepts
provided to the agent `action` method are obtained from the world; and you will
find that the world is passed as an argument to the agent actuator methods (the
actual action) so that they can produce their side effects in the world.

Take a look at *wumpus_world.py* to find a WumpusWorld class with each method
already stubbed for you. Next, open the relevant test suite, *test_wumpus_world.py*
and notice that all but the first test have been commented out. Run the test,

`python3 -m unittest test_wumpus_world`

and notice that the first test is passing. Uncomment the next test, run the test
suite, notice the failure, and implement what is necessary in order to get the
test to pass. Repeat this procedure until your wumpus world passes all the tests.

### Step 4: Demonstrate

Create a demonstration of creating an agent, knowledge base and wumpus world
simulation in *main.py*. You can lean _heavily_ upon what is provided in
*scratchpad.py*. But resist merely copying and pasting. Try typing your
demonstration from scratch in *main.py*.

### Conclusion

The first goal of this exercise is to implement the knowledge-based agent, its
agent function, and to design the API between the agent and the knowledge base.
The second goal of this exercise, is to bring us intimately familiar with the
physics and rules of wumpus world, and to provide us an opportunity of designing
and implementing a simulation within which we can test our agent (rather than,
say, a real cave inhabited by a smelly wumpus).

Our next goal will be focused on the knowledge base, and how the agent can `tell`
what it perceives and what actions have been taken, and how the agent can `ask`
the knowledge base for what rational action to take.

## Notes and Hints

Be sure that all WumpusWorldAgent and KnowledgeBase methods have appropriate
docstring comments.

Be sure to review the KB-AGENT agent function specification, the PEAS of wumpus
world, and the detailed description of the physics and rules of wumpus world
(sections 7.1 and 7.2 in the AIMA book).

The simulated WumpusWorld relies on two concessions from reality. First, the
notion of bumping into a wall may be a momentary sensation to an agent. However,
the world should assume that if an agent enters a room facing a wall, that it
has bumped into that wall, and therefore should sense the `'Bump'` percept.
Second, when a wumpus dies, it emits a really horriffic scream. In reality,
a wumpus scream only lasts for about six seconds, and then we are greeted with
silence again. However, in our simulated WumpusWorld, once a wumpus is killed,
the `'Scream'` percept shall forever be sensed by the agent. We can imagine that
the scream echoes throughout the cave for eternity. But we do this only as a
convenience to avoid the need to model time within our WumpusWorld.

Be sure to run *scratchpad.py* without making any changes to it, to verify that
your agent, knowledge base, and wumpus world are all sound.

Rerun the entire test suite to verify that all of your implementations are sound
and that all tests are passing:

`python3 -m unittest`

Don't forget to have your agent actuator methods `print` a short message about
what they are doing (eg `print("Shooting the arrow")`).

&copy; 2023 Yong Joseph Bakos. All rights reserved.
