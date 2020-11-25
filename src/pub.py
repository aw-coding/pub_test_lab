class Pub():
    def __init__(self, name , till, stock):
        self.name = name
        self.till = till
        self.stock = stock



    def add_stock(self, drink):
        self.stock.append(drink)