import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("chips", 6, 3)

    def test_food_has_name(self):
        self.assertEqual("chips", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(6, self.food.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(3, self.food.rejuvenation_level)

    
