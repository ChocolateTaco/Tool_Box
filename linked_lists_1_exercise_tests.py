import unittest
from LinkedList import LinkedList

class UnitTests(unittest.TestCase):
    def test_contains_True(self):
        ll = LinkedList()
        ll.add("side")
        ll.add("head")
        ll.add("node")
        self.assertTrue(ll.contains("head"))
        # self.assertFalse(ll.contains("tails"))

    def test_contains_False(self):
        ll = LinkedList()
        ll.add("head")
        ll.add("taco")
        ll.add("node")
        # self.assertTrue(ll.contains("head"))
        self.assertFalse(ll.contains("tails"))

if __name__ == '__main__':
    unittest.main()