class MenuItem:
    def __init__(self,name,price):
        # self.amount = 1
        self.price = price
        self.name = name

    def get_price(self):
        return self.price
    
    # def get_amount(self):
    #     return self.amount

    def get_name(self):
        return self.name
