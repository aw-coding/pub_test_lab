import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", 50, 25, 0)
        self.customer_2 = Customer("Tony", 20, 15, 0)
        self.customer_3 = Customer("Martin", 30, 25, 25)

    def test_customer_has_name(self):
        self.assertEqual("John", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)

    def test_customer_buys_drink(self):
        drink = Drink("Beer", 5, 5)
        the_prancing_pony = Pub("The Prancing Pony", 100, drink)
        self.customer.buy_drink(drink, the_prancing_pony)
        self.assertEqual(45, self.customer.wallet)
        self.assertEqual(105, the_prancing_pony.till)

    def test_customer_denied_service_age(self):
        drink = Drink("Beer", 5, 5)
        the_prancing_pony = Pub("The Prancing Pony", 100, drink)
        self.customer_2.buy_drink(drink, the_prancing_pony)
        self.assertEqual(20, self.customer_2.wallet)
        self.assertEqual(100, the_prancing_pony.till)
        

    def test_customer_denied_service_drunk(self):
        drink = Drink("Beer", 5, 5)
        the_prancing_pony = Pub("The Prancing Pony", 100, drink)
        self.customer_3.buy_drink(drink, the_prancing_pony)
        self.assertEqual(30, self.customer_3.wallet)
        self.assertEqual(100, the_prancing_pony.till)

        
        