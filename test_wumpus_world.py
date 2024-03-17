# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_wumpus_world

import unittest
import time
from wumpus_world import WumpusWorld


class TestWumpusWorld(unittest.TestCase):

    """
    Default Instantiation
    """

    def test_instantiation(self):
        """
        A WumpusWorld exists.
        """
        try:
            WumpusWorld()
        except NameError:
            self.fail("Could not instantiate WumpusWorld")

    """
    Properties
    """

    # def test_agent_location(self):
    #     """
    #     A WumpusWorld has an `agent_location`.
    #     """
    #     world = WumpusWorld(agent_location = (1, 2))
    #     self.assertEqual((1, 2), world.agent_location)

    # def test_agent_direction(self):
    #     """
    #     A WumpusWorld has an `agent_direction`.
    #     """
    #     world = WumpusWorld(agent_direction = 'North')
    #     self.assertEqual('North', world.agent_direction)

    # def test_agent_alive(self):
    #     """
    #     A WumpusWorld has an `agent_alive` property.
    #     """
    #     world = WumpusWorld(agent_alive = False)
    #     self.assertFalse(world.agent_alive)

    # def test_wumpus_alive(self):
    #     """
    #     A WumpusWorld has an `wumpus_alive` property.
    #     """
    #     world = WumpusWorld(wumpus_alive = False)
    #     self.assertFalse(world.wumpus_alive)

    # def test_wumpus_location(self):
    #     """
    #     A WumpusWorld has a `wumpus_location`.
    #     """
    #     world = WumpusWorld(wumpus_location = (1, 1))
    #     self.assertEqual((1, 1), world.wumpus_location)

    # def test_gold_location(self):
    #     """
    #     A WumpusWorld has a `gold_location`.
    #     """
    #     world = WumpusWorld(gold_location = (1, 1))
    #     self.assertEqual((1, 1), world.gold_location)

    # def test_pit_locations(self):
    #     """
    #     A WumpusWorld has `pit_locations`.
    #     """
    #     world = WumpusWorld(pit_locations = [ (1, 1) ])
    #     self.assertEqual([ (1, 1) ], world.pit_locations)

    """
    Initialization
    """

    # def test_default_initialization(self):
    #     """
    #     A default WumpusWorld has the following properties:
    #     - agent_location is (1, 1)
    #     - agent_direction is 'East'
    #     - agent_alive is True
    #     - wumpus_alive is None
    #     - wumpus_location is None
    #     - gold_location is None
    #     - pit_location is an empty list
    #     """
    #     world = WumpusWorld()
    #     self.assertEqual((1, 1), world.agent_location)
    #     self.assertEqual('East', world.agent_direction)
    #     self.assertTrue(world.agent_alive)
    #     self.assertIsNone(world.wumpus_alive)
    #     self.assertIsNone(world.wumpus_location)
    #     self.assertIsNone(world.gold_location)
    #     self.assertEqual([], world.pit_locations)

    # def test_initialization_with_properties(self):
    #     """
    #     A WumpusWorld can be initialized with an agent_location, agent_direction,
    #     agent_alive, wumpus_alive, wumpus_location, gold_location and pit_locations.
    #     """
    #     try:
    #         WumpusWorld(
    #             agent_location = (1, 1),
    #             agent_direction = 'East',
    #             agent_alive = True,
    #             wumpus_alive = True,
    #             wumpus_location = (1, 3),
    #             gold_location = (2, 3),
    #             pit_locations = [ (3, 1), (3, 3), (4, 4) ]
    #         )
    #     except TypeError:
    #         self.fail("Could not instantiate WumpusWorld with all initial properties")

    """
    Helper methods
    """

    """
    agent_can_move_east
    """

    # def test_agent_can_move_east(self):
    #     """
    #     agent_can_move_east is True when the agent can move east
    #     """
    #     world = WumpusWorld(agent_location = (2, 2))
    #     self.assertTrue(world.agent_can_move_east())

    # def test_agent_cannot_move_east(self):
    #     """
    #     agent_can_move_east is False when the agent cannot move east
    #     """
    #     world = WumpusWorld(agent_location = (4, 1))
    #     self.assertFalse(world.agent_can_move_east())

    """
    agent_can_move_west
    """

    # def test_agent_can_move_west(self):
    #     """
    #     agent_can_move_west is True when the agent can move west
    #     """
    #     world = WumpusWorld(agent_location = (2, 2))
    #     self.assertTrue(world.agent_can_move_west())

    # def test_agent_cannot_move_west(self):
    #     """
    #     agent_can_move_west is False when the agent cannot move west
    #     """
    #     world = WumpusWorld(agent_location = (1, 2))
    #     self.assertFalse(world.agent_can_move_west())

    """
    agent_can_move_north
    """

    # def test_agent_can_move_north(self):
    #     """
    #     agent_can_move_north is True when the agent can move north
    #     """
    #     world = WumpusWorld(agent_location = (2, 2))
    #     self.assertTrue(world.agent_can_move_north())

    # def test_agent_cannot_move_north(self):
    #     """
    #     agent_can_move_north is False when the agent cannot move north
    #     """
    #     world = WumpusWorld(agent_location = (2, 4))
    #     self.assertFalse(world.agent_can_move_north())

    """
    agent_can_move_south
    """

    # def test_agent_can_move_south(self):
    #     """
    #     agent_can_move_south is True when the agent can move south
    #     """
    #     world = WumpusWorld(agent_location = (2, 2))
    #     self.assertTrue(world.agent_can_move_south())

    # def test_agent_cannot_move_south(self):
    #     """
    #     agent_can_move_south is False when the agent cannot move south
    #     """
    #     world = WumpusWorld(agent_location = (2, 1))
    #     self.assertFalse(world.agent_can_move_south())

    """
    wumpus_east_of_agent
    """

    # def test_wumpus_east_of_agent(self):
    #     """
    #     wumpus_east_of_agent is True when the wumpus is east of the agent
    #     """
    #     world = WumpusWorld(agent_location = (2, 2), wumpus_location = (4, 2))
    #     self.assertTrue(world.wumpus_east_of_agent())

    # def test_wumpus_not_east_of_agent(self):
    #     """
    #     wumpus_east_of_agent is False when the wumpus is not east of the agent
    #     """
    #     world = WumpusWorld(agent_location = (2, 2), wumpus_location = (1, 1))
    #     self.assertFalse(world.wumpus_east_of_agent())

    """
    wumpus_west_of_agent
    """

    # def test_wumpus_west_of_agent(self):
    #     """
    #     wumpus_west_of_agent is True when the wumpus is west of the agent
    #     """
    #     world = WumpusWorld(agent_location = (3, 2), wumpus_location = (1, 2))
    #     self.assertTrue(world.wumpus_west_of_agent())

    # def test_wumpus_not_west_of_agent(self):
    #     """
    #     wumpus_west_of_agent is False when the wumpus is not west of the agent
    #     """
    #     world = WumpusWorld(agent_location = (3, 2), wumpus_location = (1, 1))
    #     self.assertFalse(world.wumpus_west_of_agent())

    """
    wumpus_north_of_agent
    """

    # def test_wumpus_north_of_agent(self):
    #     """
    #     wumpus_north_of_agent is True when the wumpus is north of the agent
    #     """
    #     world = WumpusWorld(agent_location = (2, 2), wumpus_location = (2, 4))
    #     self.assertTrue(world.wumpus_north_of_agent())

    # def test_wumpus_not_north_of_agent(self):
    #     """
    #     wumpus_north_of_agent is False when the wumpus is not north of the agent
    #     """
    #     world = WumpusWorld(agent_location = (2, 2), wumpus_location = (1, 1))
    #     self.assertFalse(world.wumpus_north_of_agent())

    """
    wumpus_south_of_agent
    """

    # def test_wumpus_south_of_agent(self):
    #     """
    #     wumpus_south_of_agent is True when the wumpus is south of the agent
    #     """
    #     world = WumpusWorld(agent_location = (2, 3), wumpus_location = (2, 1))
    #     self.assertTrue(world.wumpus_south_of_agent())

    # def test_wumpus_not_south_of_agent(self):
    #     """
    #     wumpus_south_of_agent is False when the wumpus is not south of the agent
    #     """
    #     world = WumpusWorld(agent_location = (2, 3), wumpus_location = (1, 1))
    #     self.assertFalse(world.wumpus_south_of_agent())

    """
    adjacent
    """

    # def test_adjacent(self):
    #     """
    #     A location is adjacent to a target location when it is immediately to the
    #     north, south, east or west of the target location.
    #     """
    #     world = WumpusWorld()
    #     target_location = (2, 2)
    #     self.assertTrue(world.adjacent((2, 3), target_location))
    #     self.assertTrue(world.adjacent((3, 2), target_location))
    #     self.assertTrue(world.adjacent((1, 2), target_location))
    #     self.assertTrue(world.adjacent((2, 1), target_location))
    #     self.assertTrue(world.adjacent(target_location, (2, 1)))

    # def test_not_adjacent(self):
    #     """
    #     A location is not adjacent to a target location when it is not immediately
    #     to the north, south, east or west of the target location.
    #     """
    #     world = WumpusWorld()
    #     target_location = (2, 2)
    #     self.assertFalse(world.adjacent((2, 2), target_location))
    #     self.assertFalse(world.adjacent((1, 1), target_location))
    #     self.assertFalse(world.adjacent((1, 3), target_location))
    #     self.assertFalse(world.adjacent((3, 1), target_location))
    #     self.assertFalse(world.adjacent((3, 3), target_location))
    #     self.assertFalse(world.adjacent(target_location, (3, 3)))
    #     self.assertFalse(world.adjacent((1, 3), (4, 4)))
    #     self.assertFalse(world.adjacent((1, 4), (4, 2)))

    # def test_not_adjacent_none(self):
    #     """
    #     A None location is not adjacent to a target location, and vice-versa.
    #     """
    #     world = WumpusWorld()
    #     self.assertFalse(world.adjacent((1, 1), None))
    #     self.assertFalse(world.adjacent(None, (1, 1)))

    """
    agent_bumped_wall
    """

    # def test_agent_has_not_bumped_wall(self):
    #     """
    #     An agent not adjacent to a wall has not bumped into a wall, no matter the
    #     direction the agent is facing.
    #     """
    #     world = WumpusWorld(agent_location = (2, 2), agent_direction = 'East')
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'West'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'North'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'South'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_1_1(self):
    #     """
    #     An agent facing west or south in (1, 1) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1))
    #     world.agent_direction = 'West'
    #     self.assertTrue(world.agent_bumped_wall())
    #     world.agent_direction = 'South'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_1_1(self):
    #     """
    #     An agent facing north or east in (1, 1) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1))
    #     world.agent_direction = 'North'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'East'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_1_2(self):
    #     """
    #     An agent facing west (1, 2) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (1, 2))
    #     world.agent_direction = 'West'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_1_2(self):
    #     """
    #     An agent not facing west in (1, 2) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (1, 2))
    #     world.agent_direction = 'North'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'East'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'South'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_1_3(self):
    #     """
    #     An agent facing west (1, 3) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (1, 3))
    #     world.agent_direction = 'West'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_1_3(self):
    #     """
    #     An agent not facing west in (1, 3) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (1, 3))
    #     world.agent_direction = 'North'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'East'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'South'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_1_4(self):
    #     """
    #     An agent facing west or north in (1, 4) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (1, 4))
    #     world.agent_direction = 'West'
    #     self.assertTrue(world.agent_bumped_wall())
    #     world.agent_direction = 'North'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_1_4(self):
    #     """
    #     An agent not facing west or north in (1, 4) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (1, 4))
    #     world.agent_direction = 'East'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'South'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_2_1(self):
    #     """
    #     An agent facing south in (2, 1) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (2, 1))
    #     world.agent_direction = 'South'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_2_1(self):
    #     """
    #     An agent not facing south in (2, 1) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (2, 1))
    #     world.agent_direction = 'North'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'East'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'West'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_2_4(self):
    #     """
    #     An agent facing north in (2, 4) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (2, 4))
    #     world.agent_direction = 'North'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_2_4(self):
    #     """
    #     An agent not facing north in (2, 4) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (2, 4))
    #     world.agent_direction = 'South'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'East'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'West'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_3_1(self):
    #     """
    #     An agent facing south in (3, 1) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (3, 1))
    #     world.agent_direction = 'South'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_3_1(self):
    #     """
    #     An agent not facing south in (3, 1) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (3, 1))
    #     world.agent_direction = 'North'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'East'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'West'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_3_4(self):
    #     """
    #     An agent facing north in (3, 4) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (3, 4))
    #     world.agent_direction = 'North'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_3_4(self):
    #     """
    #     An agent not facing north in (3, 4) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (3, 4))
    #     world.agent_direction = 'South'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'East'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'West'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_4_1(self):
    #     """
    #     An agent facing east or south in (4, 1) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (4, 1))
    #     world.agent_direction = 'East'
    #     self.assertTrue(world.agent_bumped_wall())
    #     world.agent_direction = 'South'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_4_1(self):
    #     """
    #     An agent facing north or west in (4, 1) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (4, 1))
    #     world.agent_direction = 'North'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'West'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_4_2(self):
    #     """
    #     An agent facing east (4, 2) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (4, 2))
    #     world.agent_direction = 'East'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_4_2(self):
    #     """
    #     An agent not facing east in (4, 2) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (4, 2))
    #     world.agent_direction = 'North'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'West'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'South'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_4_3(self):
    #     """
    #     An agent facing east (4, 3) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (4, 3))
    #     world.agent_direction = 'East'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_4_3(self):
    #     """
    #     An agent not facing east in (4, 3) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (4, 3))
    #     world.agent_direction = 'North'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'West'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'South'
    #     self.assertFalse(world.agent_bumped_wall())

    # def test_agent_bumped_4_4(self):
    #     """
    #     An agent facing east or north in (4, 4) has bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (4, 4))
    #     world.agent_direction = 'East'
    #     self.assertTrue(world.agent_bumped_wall())
    #     world.agent_direction = 'North'
    #     self.assertTrue(world.agent_bumped_wall())

    # def test_agent_not_bumped_4_4(self):
    #     """
    #     An agent not facing east or north in (4, 4) has not bumped a wall.
    #     """
    #     world = WumpusWorld(agent_location = (4, 4))
    #     world.agent_direction = 'West'
    #     self.assertFalse(world.agent_bumped_wall())
    #     world.agent_direction = 'South'
    #     self.assertFalse(world.agent_bumped_wall())

    """
    END of helper method tests
    """

    """
    percept
    """

    # def test_percept_none_location(self):
    #     """
    #     The percept of a None location is (None, None, None, None, None)
    #     """
    #     world = WumpusWorld()
    #     self.assertEqual((None, None, None, None, None), world.percept(None))

    # def test_percept_glitter(self):
    #     """
    #     The percept in a location with gold matches (_, _, 'Glitter', _, _)
    #     """
    #     world = WumpusWorld(gold_location = (1, 1))
    #     self.assertEqual('Glitter', world.percept((1, 1))[2])

    # def test_percept_no_glitter(self):
    #     """
    #     The percept in a location without gold matches (_, _, None, _, _)
    #     """
    #     world = WumpusWorld(gold_location = (1, 1))
    #     self.assertEqual(None, world.percept((1, 2))[2])

    # def test_percept_stench(self):
    #     """
    #     The percept in a location with wumpus matches ('Stench', _, _, _, _)
    #     """
    #     world = WumpusWorld(wumpus_location = (2, 2))
    #     self.assertEqual('Stench', world.percept((2, 2))[0])

    # def test_percept_stench_north(self):
    #     """
    #     The percept in a location north of the wumpus matches ('Stench', _, _, _, _)
    #     """
    #     world = WumpusWorld(wumpus_location = (2, 2))
    #     self.assertEqual('Stench', world.percept((2, 3))[0])

    # def test_percept_stench_south(self):
    #     """
    #     The percept in a location south of the wumpus matches ('Stench', _, _, _, _)
    #     """
    #     world = WumpusWorld(wumpus_location = (2, 2))
    #     self.assertEqual('Stench', world.percept((2, 1))[0])

    # def test_percept_stench_east(self):
    #     """
    #     The percept in a location east of the wumpus matches ('Stench', _, _, _, _)
    #     """
    #     world = WumpusWorld(wumpus_location = (2, 2))
    #     self.assertEqual('Stench', world.percept((3, 2))[0])

    # def test_percept_stench_west(self):
    #     """
    #     The percept in a location west of the wumpus matches ('Stench', _, _, _, _)
    #     """
    #     world = WumpusWorld(wumpus_location = (2, 2))
    #     self.assertEqual('Stench', world.percept((1, 2))[0])

    # def test_no_stench(self):
    #     """
    #     The percept in a location not adjacent to the wumpus matches (None, _, _, _, _)
    #     """
    #     world = WumpusWorld(wumpus_location = (2, 2))
    #     self.assertEqual(None, world.percept((1, 1))[0])
    #     self.assertEqual(None, world.percept((1, 3))[0])
    #     self.assertEqual(None, world.percept((3, 3))[0])
    #     self.assertEqual(None, world.percept((3, 1))[0])

    # def test_stench_dead_wumpus(self):
    #     """
    #     A dead wumpus still emits a stench.
    #     """
    #     world = WumpusWorld(wumpus_location = (2, 2), wumpus_alive = False)
    #     self.assertEqual('Stench', world.percept((2, 2))[0])
    #     self.assertEqual('Stench', world.percept((3, 2))[0])
    #     self.assertEqual('Stench', world.percept((2, 3))[0])
    #     self.assertEqual('Stench', world.percept((2, 1))[0])
    #     self.assertEqual('Stench', world.percept((1, 2))[0])

    # def test_percept_breeze(self):
    #     """
    #     The percept in a location adjacent to a pit matches (_, 'Breeze', _, _, _)
    #     """
    #     world = WumpusWorld(pit_locations = [(2, 2)])
    #     self.assertEqual('Breeze', world.percept((3, 2))[1])
    #     self.assertEqual('Breeze', world.percept((2, 3))[1])
    #     self.assertEqual('Breeze', world.percept((2, 1))[1])
    #     self.assertEqual('Breeze', world.percept((1, 2))[1])

    # def test_percept_no_breeze(self):
    #     """
    #     The percept in a location not adjacent to a pit matches (_, None, _, _, _)
    #     """
    #     world = WumpusWorld(pit_locations = [(2, 2)])
    #     self.assertEqual(None, world.percept((1, 1))[1])
    #     self.assertEqual(None, world.percept((1, 3))[1])
    #     self.assertEqual(None, world.percept((3, 3))[1])
    #     self.assertEqual(None, world.percept((3, 1))[1])

    # def test_percept_multiple_breezes(self):
    #     """
    #     Multiple pits emit 'Breeze' percepts in adjacent rooms.
    #     """
    #     world = WumpusWorld(pit_locations = [(1, 1), (2, 1), (4, 1)])
    #     self.assertEqual('Breeze', world.percept((3, 1))[1])
    #     self.assertEqual('Breeze', world.percept((1, 2))[1])
    #     self.assertEqual('Breeze', world.percept((2, 2))[1])
    #     self.assertEqual(None, world.percept((3, 2))[1])
    #     self.assertEqual('Breeze', world.percept((4, 2))[1])

    # def test_percept_bump(self):
    #     """
    #     A location with a wall in which the agent is facing the wall emits a
    #     'Bump' percept.
    #     """
    #     world = WumpusWorld(agent_location = (2, 1), agent_direction = 'South')
    #     self.assertEqual('Bump', world.percept((2, 1))[3])

    # def test_percept_no_bump(self):
    #     """
    #     A location with a wall in which the agent is not facing the wall does
    #     not emit a 'Bump' percept.
    #     """
    #     world = WumpusWorld(agent_location = (2, 1), agent_direction = 'East')
    #     self.assertEqual(None, world.percept((2, 1))[3])

    # def test_percept_scream(self):
    #     """
    #     If the wumpus is dead, the percept in every location matches (_, _, _, _, 'Scream')
    #     """
    #     world = WumpusWorld(wumpus_alive = False)
    #     for x in range(1, 5):
    #         for y in range(1, 5):
    #             self.assertEqual('Scream', world.percept((x, y))[4])

    # def test_percept_no_scream(self):
    #     """
    #     If the wumpus is alive, the percept in every location matches (_, _, _, _, None)
    #     """
    #     world = WumpusWorld(wumpus_alive = True)
    #     for x in range(1, 5):
    #         for y in range(1, 5):
    #             self.assertEqual(None, world.percept((x, y))[4])

    """
    percept system tests with example wumpus world
    """

    # def test_percept_1_1(self):
    #     """
    #     The percept of location (1, 1) is (None, None, None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual((None, None, None, None, None), world.percept((1, 1)))

    # def test_percept_1_2(self):
    #     """
    #     The percept of location (1, 2) is ('Stench', None, None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual(('Stench', None, None, None, None), world.percept((1, 2)))

    # def test_percept_1_3(self):
    #     """
    #     The percept of location (1, 3) is ('Stench', None, None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual(('Stench', None, None, None, None), world.percept((1, 3)))

    # def test_percept_1_4(self):
    #     """
    #     The percept of location (1, 4) is ('Stench', None, None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual(('Stench', None, None, None, None), world.percept((1, 4)))

    # def test_percept_2_1(self):
    #     """
    #     The percept of location (2, 1) is (None, 'Breeze', None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual((None, 'Breeze', None, None, None), world.percept((2, 1)))

    # def test_percept_2_2(self):
    #     """
    #     The percept of location (2, 2) is (None, None, None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual((None, None, None, None, None), world.percept((2, 2)))

    # def test_percept_2_3(self):
    #     """
    #     The percept of location 2, 3 is ('Stench', 'Breeze', 'Glitter', None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual(('Stench', 'Breeze', 'Glitter', None, None), world.percept((2, 3)))

    # def test_percept_2_4(self):
    #     """
    #     The percept of location (2, 4) is (None, None, None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual((None, None, None, None, None), world.percept((2, 4)))

    # def test_percept_3_2(self):
    #     """
    #     The percept of location (3, 2) is (None, 'Breeze', None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual((None, 'Breeze', None, None, None), world.percept((3, 2)))

    # def test_percept_3_4(self):
    #     """
    #     The percept of location (3, 4) is (None, 'Breeze', None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual((None, 'Breeze', None, None, None), world.percept((3, 4)))

    # def test_percept_4_1(self):
    #     """
    #     The percept of location (4, 1) is (None, 'Breeze', None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual((None, 'Breeze', None, None, None), world.percept((4, 1)))

    # def test_percept_4_2(self):
    #     """
    #     The percept of location (4, 2) is (None, None, None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual((None, None, None, None, None), world.percept((4, 2)))

    # def test_percept_4_3(self):
    #     """
    #     The percept of location (4, 3) is (None, 'Breeze', None, None, None)
    #     """
    #     world = example_wumpus_world()
    #     self.assertEqual((None, 'Breeze', None, None, None), world.percept((4, 3)))

    """
    Side Effects
    """

    """
    turned_left
    """

    # def test_turned_left(self):
    #     """
    #     Turning left results in a new agent direction.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), agent_direction = 'East')
    #     self.assertEqual('East', world.agent_direction)
    #     world.turned_left()
    #     self.assertEqual('North', world.agent_direction)
    #     world.turned_left()
    #     self.assertEqual('West', world.agent_direction)
    #     world.turned_left()
    #     self.assertEqual('South', world.agent_direction)
    #     world.turned_left()
    #     self.assertEqual('East', world.agent_direction)

    """
    turned_right
    """

    # def test_turned_right(self):
    #     """
    #     Turning right results in a new agent direction.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), agent_direction = 'East')
    #     self.assertEqual('East', world.agent_direction)
    #     world.turned_right()
    #     self.assertEqual('South', world.agent_direction)
    #     world.turned_right()
    #     self.assertEqual('West', world.agent_direction)
    #     world.turned_right()
    #     self.assertEqual('North', world.agent_direction)
    #     world.turned_right()
    #     self.assertEqual('East', world.agent_direction)

    """
    moved_forward
    """

    # def test_moved_forward_east(self):
    #     """
    #     Facing east, moving forward changes the agent location.
    #     """
    #     world = WumpusWorld(agent_location = (2, 2), agent_direction = 'East')
    #     world.moved_forward()
    #     self.assertEqual((3, 2), world.agent_location)

    # def test_moved_forward_east_bump(self):
    #     """
    #     Facing east, moving into a wall does not change the agent location.
    #     """
    #     world = WumpusWorld(agent_location = (4, 2), agent_direction = 'East')
    #     world.moved_forward()
    #     self.assertEqual((4, 2), world.agent_location)

    # def test_moved_forward_west(self):
    #     """
    #     Facing west, moving forward changes the agent location.
    #     """
    #     world = WumpusWorld(agent_location = (2, 2), agent_direction = 'West')
    #     world.moved_forward()
    #     self.assertEqual((1, 2), world.agent_location)

    # def test_moved_forward_west_bump(self):
    #     """
    #     Facing west, moving into a wall does not change the agent location.
    #     """
    #     world = WumpusWorld(agent_location = (1, 2), agent_direction = 'West')
    #     world.moved_forward()
    #     self.assertEqual((1, 2), world.agent_location)

    # def test_moved_forward_north(self):
    #     """
    #     Facing north, moving forward changes the agent location.
    #     """
    #     world = WumpusWorld(agent_location = (2, 2), agent_direction = 'North')
    #     world.moved_forward()
    #     self.assertEqual((2, 3), world.agent_location)

    # def test_moved_forward_north_bump(self):
    #     """
    #     Facing north, moving into a wall does not change the agent location.
    #     """
    #     world = WumpusWorld(agent_location = (2, 4), agent_direction = 'North')
    #     world.moved_forward()
    #     self.assertEqual((2, 4), world.agent_location)

    # def test_moved_forward_south(self):
    #     """
    #     Facing south, moving forward changes the agent location.
    #     """
    #     world = WumpusWorld(agent_location = (2, 2), agent_direction = 'South')
    #     world.moved_forward()
    #     self.assertEqual((2, 1), world.agent_location)

    # def test_moved_forward_south_bump(self):
    #     """
    #     Facing south, moving into a wall does not change the agent location.
    #     """
    #     world = WumpusWorld(agent_location = (2, 1), agent_direction = 'South')
    #     world.moved_forward()
    #     self.assertEqual((2, 1), world.agent_location)

    # def test_moved_forward_into_pit(self):
    #     """
    #     Moving forward into a pit results in the 'miserable death' of the agent.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), agent_direction = 'East',
    #         pit_locations = [(2, 1)])
    #     world.moved_forward()
    #     self.assertEqual((2, 1), world.agent_location)
    #     self.assertFalse(world.agent_alive)

    # def test_moved_forward_into_living_wumpus(self):
    #     """
    #     Moving forward into a living wumpus results in the 'miserable death' of the agent.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), agent_direction = 'East',
    #         wumpus_location = (2, 1), wumpus_alive = True)
    #     world.moved_forward()
    #     self.assertEqual((2, 1), world.agent_location)
    #     self.assertFalse(world.agent_alive)

    # def test_moved_forward_into_dead_wumpus(self):
    #     """
    #     Moving forward into a dead wumpus is just a smelly experience.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), agent_direction = 'East',
    #         wumpus_location = (2, 1), wumpus_alive = False)
    #     world.moved_forward()
    #     self.assertEqual((2, 1), world.agent_location)
    #     self.assertTrue(world.agent_alive)

    """
    grabbed
    """

    # def test_grabbed_without_gold(self):
    #     """
    #     Grabbing in a location without gold does nothing.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), gold_location = (2, 2))
    #     self.assertNotEqual(world.agent_location, world.gold_location)
    #     world.grabbed()
    #     self.assertEqual((2, 2), world.gold_location)
    #     self.assertEqual('Glitter', world.percept(world.gold_location)[2])

    # def test_grabbed_gold(self):
    #     """
    #     Grabbing in a location with gold removes the gold from the world, thereby
    #     setting `gold_location` to None.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), gold_location = (1, 1))
    #     self.assertEqual(world.agent_location, world.gold_location)
    #     world.grabbed()
    #     self.assertIsNone(world.gold_location)

    # def test_grabbed_gold_removes_glitter(self):
    #     """
    #     Grabbing the gold results in the absence of the 'Glitter' percept.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), gold_location = (1, 1))
    #     self.assertEqual(world.agent_location, world.gold_location)
    #     self.assertIn('Glitter', world.percept(world.agent_location))
    #     world.grabbed()
    #     self.assertNotIn('Glitter', world.percept(world.agent_location))

    """
    climbed
    """

    # def test_climbed_without_exit(self):
    #     """
    #     Climbing in any location other than (1, 1) does nothing.
    #     """
    #     world = WumpusWorld(agent_location = (1, 2))
    #     self.assertNotEqual((1, 1), world.agent_location)
    #     world.climbed()
    #     self.assertEqual((1, 2), world.agent_location)

    # def test_climbed_with_exit(self):
    #     """
    #     Climbing in location (1, 1) exits the cave, removing the agent from the
    #     world, thereby setting `agent_location` to None.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1))
    #     self.assertEqual((1, 1), world.agent_location)
    #     world.climbed()
    #     self.assertIsNone(world.agent_location)

    """
    shot
    """

    # def test_shot_missed(self):
    #     """
    #     Shooting when the wumpus is outside the arrow trajectory does nothing.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), agent_direction = 'North',
    #         wumpus_location = (3, 1), wumpus_alive = True)
    #     world.shot()
    #     self.assertEqual((3, 1), world.wumpus_location)
    #     self.assertTrue(world.wumpus_alive)
    #     self.assertIsNone(world.percept(world.agent_location)[4]) # No scream

    # def test_shot_east(self):
    #     """
    #     Shooting east when the wumpus is east of the agent kills the wumpus.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), agent_direction = 'East',
    #         wumpus_location = (4, 1), wumpus_alive = True)
    #     world.shot()
    #     self.assertFalse(world.wumpus_alive)
    #     self.assertEqual('Scream', world.percept((1, 1))[4])

    # def test_shot_west(self):
    #     """
    #     Shooting west when the wumpus is west of the agent kills the wumpus.
    #     """
    #     world = WumpusWorld(agent_location = (4, 1), agent_direction = 'West',
    #         wumpus_location = (1, 1), wumpus_alive = True)
    #     world.shot()
    #     self.assertFalse(world.wumpus_alive)
    #     self.assertEqual('Scream', world.percept((4, 1))[4])

    # def test_shot_north(self):
    #     """
    #     Shooting north when the wumpus is north of the agent kills the wumpus.
    #     """
    #     world = WumpusWorld(agent_location = (1, 1), agent_direction = 'North',
    #         wumpus_location = (1, 4), wumpus_alive = True)
    #     world.shot()
    #     self.assertFalse(world.wumpus_alive)
    #     self.assertEqual('Scream', world.percept((1, 1))[4])

    # def test_shot_south(self):
    #     """
    #     Shooting south when the wumpus is south of the agent kills the wumpus.
    #     """
    #     world = WumpusWorld(agent_location = (1, 4), agent_direction = 'South',
    #         wumpus_location = (1, 1), wumpus_alive = True)
    #     world.shot()
    #     self.assertFalse(world.wumpus_alive)
    #     self.assertEqual('Scream', world.percept((1, 4))[4])

    # def test_shot_wumpus_dead_but_present(self):
    #     """
    #     Shooting the wumpus kills it, but does not remove it from the cave.
    #     """
    #     world = WumpusWorld(agent_location = (1, 4), agent_direction = 'South',
    #         wumpus_location = (1, 1), wumpus_alive = True)
    #     world.shot()
    #     self.assertFalse(world.wumpus_alive)
    #     self.assertEqual((1, 1), world.wumpus_location)


def example_wumpus_world():
    """
    . . . P
    W G P .
    . . . .
    . . P .
    """
    return WumpusWorld(
        agent_location = (1, 1),
        agent_direction = 'East',
        agent_alive = True,
        wumpus_alive = True,
        wumpus_location = (1, 3),
        gold_location = (2, 3),
        pit_locations = [ (3, 1), (3, 3), (4, 4) ]
    )

def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
