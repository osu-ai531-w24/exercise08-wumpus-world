# DO NOT MODIFY THE CODE IN THE TESTS
# Run me via: python3 -m unittest test_knowledge_base

import unittest
import time
from knowledge_base import KnowledgeBase
from wumpus_world_agent import WumpusWorldAgent

class TestKnowledgeBase(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A KnowledgeBase exists.
        """
        try:
            KnowledgeBase()
        except NameError:
            self.fail("Could not instantiate KnowledgeBase")

    """
    tell
    """

    # def test_tell(self):
    #     """
    #     A KnowledgeBase has a `tell` method.
    #     """
    #     kb = KnowledgeBase()
    #     kb.tell(None)

    """
    ask
    """

    # def test_ask(self):
    #     """
    #     A KnowledgeBase has an `ask` method.
    #     """
    #     kb = KnowledgeBase()
    #     kb.ask(None)

    # def test_ask_default_action(self):
    #     """
    #     The default action returned by ask is `WumpusWorldAgent.climb`
    #     """
    #     kb = KnowledgeBase()
    #     self.assertEqual(WumpusWorldAgent.climb, kb.ask(None))


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
