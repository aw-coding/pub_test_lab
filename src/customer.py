class Customer():
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness


    def buy_drink(self, drink_to_buy):
        self.wallet -= drink_to_buy.price

    def food_rejuvenate(self, food):
        self.drunkenness -= food.rejuvenation_level

    

    


    

# beer = Drink("Beer", 5)
# the_prancing_pony = Pub("The Prancing Pony", 100, ["Beer"])