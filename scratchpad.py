# Wumpus World Scratchpad
# Use this as a "scratchpad" to tinker with your code.
# There are no rules here, and this code will not be evaluated. This file is a
# place for you to experiment.


from wumpus_world import WumpusWorld
from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase

wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    agent_alive = True,
    wumpus_alive = True,
    wumpus_location = (1, 3),
    gold_location = (2, 3),
    pit_locations = [ (3, 1), (3, 3), (4, 3) ]
    )

kb = KnowledgeBase()

agent = WumpusWorldAgent(kb)

action = agent.action(wumpus_world.percept((1, 1)))
action(agent, wumpus_world)
