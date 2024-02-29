# WumpusWorld
# A simulated representation of a real Wumpus World, aligned with the specified
# characteristics in the AIMA text.
# Note: This is not a state model. It _is_ the real world / environment within
# which the agent operates. Think of it as actual, physical, reality.
# Note 2: This simulation will not include the modeling of time, for the sake of
# simplicity. This only affects the 'Bump' and 'Scream' percepts. In the case of
# 'Bump', we assume that when an agent is in a room facing a wall, it should receive
# the 'Bump' percept. For 'Scream', when the wumpus is killed we let the scream
# linger throughout the cave indefinitely.
# YOUR NAME

class WumpusWorld:

    EXIT_LOCATION = (1, 1)

    def __init__(self, agent_location = None, agent_direction = None,
                       agent_alive = None, wumpus_alive = None,
                       wumpus_location = None, gold_location = None,
                       pit_locations = None):
        pass

    def percept(self, location):
        """
        The current five-element percept in the `location`. Returns a tuple in the
        form of ('Stench', 'Breeze', 'Glitter', 'Bump', 'Scream'). Any of the elements
        within the returned percept tuple can be None.
        """
        pass

    """
    Physical side effects of agent actions
    """

    def turned_left(self):
        """
        Turn the agent counter-clockwise, to the left, resulting in a new
        `agent_direction`.
        """
        pass

    def turned_right(self):
        """
        Turn the agent clockwise, to the right, resulting in a new `agent_direction`.
        """
        pass

    def moved_forward(self):
        """
        Attempt to move forward. When successful, update the agent location.
        Moving into a pit location kills the agent.
        Moving into a living wumpus location kills the agent.
        """
        pass

    def grabbed(self):
        """
        Attempt to grab the gold. Successful when executed in `gold_location`, in
        which case the gold location should be set to None.
        """
        pass

    def climbed(self):
        """
        Attempt to climb out of the cave. Successful when executed in location
        (1, 1), in which case the agent location should be set to None.
        """
        pass

    def shot(self):
        """
        Shoot the arrow. If the arrow strikes the wumpus, then the wumpus should
        no longer be alive.
        """
        pass

    """
    Helper methods
    """

    def adjacent(self, location, target):
        """
        Is `location` immediately north, south, east or west of `target`?
        """
        pass

    def agent_can_move_east(self):
        """
        Can the agent move east?
        """
        pass

    def agent_can_move_west(self):
        """
        Can the agent move west?
        """
        pass

    def agent_can_move_north(self):
        """
        Can the agent move north?
        """
        pass

    def agent_can_move_south(self):
        """
        Can the agent move south?
        """
        pass

    def agent_bumped_wall(self):
        """
        Did the agent bump into a wall? (Or, is the agent facing a wall?)
        """
        pass

    def wumpus_east_of_agent(self):
        """
        Is the wumpus somewhere to the east of the agent?
        """
        pass

    def wumpus_west_of_agent(self):
        """
        Is the wumpus somewhere to the west of the agent?
        """
        pass

    def wumpus_north_of_agent(self):
        """
        Is the wumpus somewhere to the north of the agent?
        """
        pass

    def wumpus_south_of_agent(self):
        """
        Is the wumpus somewhere to the south of the agent?
        """
        pass
