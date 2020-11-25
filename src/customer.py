class Customer():
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness


    def buy_drink(self, drink_to_buy, current_pub):
        if self.age >= 18 and self.drunkenness <= 20:
            self.wallet -= drink_to_buy.price
            current_pub.till += drink_to_buy.price
        else:
            return False
    

    


    

# beer = Drink("Beer", 5)
# the_prancing_pony = Pub("The Prancing Pony", 100, ["Beer"])