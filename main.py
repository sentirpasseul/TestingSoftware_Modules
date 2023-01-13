import unittest
from test import return_test

class TestArea(unittest.TestCase):
    def test1(self):
        self.assertEqual(return_test(1), 1)



