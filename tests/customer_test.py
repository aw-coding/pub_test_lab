import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("John", 50, 25, 0)
        self.customer_2 = Customer("Tony", 20, 15, 0)
        self.customer_3 = Customer("Martin", 30, 25, 25)

    def test_customer_has_name(self):
        self.assertEqual("John", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50, self.customer.wallet)


    def test_food_rejuvenates(self):
        food = Food("chips", 6, 3)
        self.customer_3.food_rejuvenate(food)
        self.assertEqual(22, self.customer_3.drunkenness)




  

        
        