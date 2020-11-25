import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        drinks_in_stock = {"Beer": 3, "Wine": 5, "Vodka": 4}
        self.pub = Pub("The Prancing Pony", 100, drinks_in_stock)


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100, self.pub.till)   


    def test_pub_has_drink_in_stock(self):
        result = self.pub.check_stock("Beer")
        self.assertEqual(True, result)

    def test_approve_entry_age(self):
        customer = Customer("John", 50, 25, 0)
        customer_2 = Customer("Tony", 20, 15, 0)
        customer_3 = Customer("Martin", 30, 25, 25)
        result = self.pub.approve_entry(customer_2)
        self.assertEqual(False, result)


    def test_approve_entry_drunkenness(self):
        customer = Customer("John", 50, 25, 0)
        customer_2 = Customer("Tony", 20, 15, 0)
        customer_3 = Customer("Martin", 30, 25, 25)
        result = self.pub.approve_entry(customer_3)
        self.assertEqual(False, result)

        
    def test_add_money_to_till(self):
        drink = Drink("Beer", 5, 5)
        self.pub.add_money_to_till(drink)
        self.assertEqual(105, self.pub.till)

    
