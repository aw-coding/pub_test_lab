class Pub():
    def __init__(self, name , till, stock):
        self.name = name
        self.till = till
        self.stock = stock


    def check_stock(self, drink):
        for item in self.stock:
            if item == drink and self.stock[drink] > 0:
                return True
            else:
                return False    



    def add_stock(self, drink):
        self.stock.append(drink)

    def approve_entry(self, customer):
        if customer.age >= 18 and customer.drunkenness <= 20:
            return True
        else:
            return False

    def add_money_to_till(self, drink_sold):
        self.till += drink_sold.price