# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_wumpus_world_agent

import unittest
from unittest.mock import MagicMock
import time
from wumpus_world_agent import WumpusWorldAgent

class TestWumpusWorldAgent(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A WumpusWorldAgent exists.
        """
        try:
            WumpusWorldAgent(None)
        except NameError:
            self.fail("Could not instantiate WumpusWorldAgent")

    """
    Properties
    """

    # def test_kb(self):
    #     """
    #     A WumpusWorldAgent has a `kb` property.
    #     """
    #     agent = WumpusWorldAgent("Fake knowledge base")
    #     self.assertEqual("Fake knowledge base", agent.kb)

    # def test_time(self):
    #     """
    #     A WumpusWorldAgent has a `time` property, initally 0.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     self.assertEqual(0, agent.time)

    """
    Actuators
    """

    # def test_turn_left(self):
    #     """
    #     A WumpusWorldAgent can turn_left.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.turn_left(fake_world)

    # def test_turn_left_affects_world(self):
    #     """
    #     Turning left should have a side effect in the world, communicated by
    #     informing the world that the agent has `turned_left`.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.turn_left(fake_world)
    #     fake_world.turned_left.assert_called()

    # def test_turn_right(self):
    #     """
    #     A WumpusWorldAgent can turn_right.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.turn_right(fake_world)

    # def test_turn_right_affects_world(self):
    #     """
    #     Turning right should have a side effect in the world, communicated by
    #     informing the world that the agent has `turned_right`.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.turn_right(fake_world)
    #     fake_world.turned_right.assert_called()

    # def test_move_forward(self):
    #     """
    #     A WumpusWorldAgent can move_forward.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.move_forward(fake_world)

    # def test_move_forward_affects_world(self):
    #     """
    #     Turning right should have a side effect in the world, communicated by
    #     informing the world that the agent has `moved_forward`.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.move_forward(fake_world)
    #     fake_world.moved_forward.assert_called()

    # def test_shoot(self):
    #     """
    #     A WumpusWorldAgent can shoot.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.shoot(fake_world)

    # def test_shoot_affects_world(self):
    #     """
    #     Shooting the arrow should have a side effect in the world, communicated by
    #     informing the world that the agent has `shot`.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.shoot(fake_world)
    #     fake_world.shot.assert_called()

    # def test_grab(self):
    #     """
    #     A WumpusWorldAgent can grab.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.grab(fake_world)

    # def test_grab_affects_world(self):
    #     """
    #     Grabbing should have a side effect in the world, communicated by
    #     informing the world that the agent has `grabbed`.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.grab(fake_world)
    #     fake_world.grabbed.assert_called()

    # def test_climb(self):
    #     """
    #     A WumpusWorldAgent can climb.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.climb(fake_world)

    # def test_climb_affects_world(self):
    #     """
    #     Climbing should have a side effect in the world, communicated by
    #     informing the world that the agent has `climbed`.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     fake_world = MagicMock()
    #     agent.climb(fake_world)
    #     fake_world.climbed.assert_called()

    """
    make_percept_sequence
    """

    # def test_make_percept_sentence(self):
    #     """
    #     A WumpusWorldAgent has a `make_percept_sentence` method.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     agent.make_percept_sentence(None)

    """
    make_action_query
    """

    # def test_make_action_query(self):
    #     """
    #     A WumpusWorldAgent has a `make_action_query` method.
    #     """
    #     agent = WumpusWorldAgent(None)
    #     agent.make_action_query()

    """
    make_action_sentence
    """

    # def make_action_sentence(self):
    #     """
    #     A WumpusWorldAgent has a `make_action_sentence` method
    #     """
    #     agent = WumpusWorldAgent(None)
    #     agent.make_action_sentence(None)

    """
    Agent function
    """

    # def test_action(self):
    #     """
    #     A WumpusWorldAgent has an agent function named `action`.
    #     """
    #     fake_kb = MagicMock()
    #     agent = WumpusWorldAgent(fake_kb)
    #     action = agent.action(None)

    # def test_action_tells_kb_percept_sentence(self):
    #     """
    #     The agent function `tell`s the KnowledgeBase what it perceives.
    #     """
    #     fake_kb = MagicMock()
    #     agent = WumpusWorldAgent(fake_kb)
    #     action = agent.action(None)
    #     fake_kb.tell.assert_called()

    # def test_action_asks_kb_for_action(self):
    #     """
    #     The agent function `ask`s the KnowledgeBase for an action.
    #     """
    #     fake_kb = MagicMock()
    #     agent = WumpusWorldAgent(fake_kb)
    #     action = agent.action(None)
    #     fake_kb.ask.assert_called_once()

    # def test_action_tells_kb_action_sentence(self):
    #     """
    #     The agent function `tell`s the KnowledgeBase that it performed an action.
    #     """
    #     fake_kb = MagicMock()
    #     agent = WumpusWorldAgent(fake_kb)
    #     action = agent.action(None)
    #     self.assertEqual(2, fake_kb.tell.call_count)

    # def test_action_increments_time(self):
    #     """
    #     Time is incremented when the agent function is invoked.
    #     """
    #     fake_kb = MagicMock()
    #     agent = WumpusWorldAgent(fake_kb)
    #     self.assertEqual(0, agent.time)
    #     action = agent.action(None)
    #     self.assertEqual(1, agent.time)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
