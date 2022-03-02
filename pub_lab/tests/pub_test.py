from ast import excepthandler
import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    
    def test_increase_till(self):
        self.pub.increase_till(2.50)
        excepted = 102.50
        actual = self.pub.till
        self.assertEqual(excepted, actual)


    # def test_increase_till(self):
    #     self.pub.increase_till(2.50)
    #     self.assertEqual(102.5, self.pub.till)