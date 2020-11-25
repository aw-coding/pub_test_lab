import unittest
from src.pub import Pub
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100, "Beer")

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)   


    # def test_add_stock(self):
    #     drink = Drink("Beer", 5)
    #     add_stock(drink)
    #     self.assertEqual(1, len(pub.stock))

    # def test_add_drink(self):
    #     beer = Drink("Beer", 5)
    #     self.stock.append(beer)
    #     self.assertEqual(beer, self.pub.stock)

    def test_pub_has_drink_in_stock(self):
        self.assertEqual("Beer", self.pub.stock)
    
    # def test_pub(self):
    #     #ARRANGE
    #     person = person()
    #     self.pub.add_guest()
    #     #ACT
    #     actual = pub.get_till_total()
    #     pub.kick_out_guest()
    #     #ASSERT
    #     slef.assertEqual(expected, actual)