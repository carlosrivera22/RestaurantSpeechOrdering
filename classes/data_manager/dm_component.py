from ..stack import Stack
import pandas as pd
class DataManager:

    def __init__(self):
        #stack to manage actions in this system
        self.stack = Stack()

        #Dictionary of order
        self.items = []


    def get_menu_stack(self):
        return self.stack


    def get_items(self):
        return self.items


    def display_order(self):
        order = pd.DataFrame(columns=['item','price','qty'])
        values = list(map(lambda x: x.get_name(),self.items))
        prices = list(map(lambda x: x.get_price(),self.items))
        quantities = []
        for v in values:
            quantities.append(1)
        order['item'] = values
        order['price'] = prices
        order['qty'] = quantities
        if len(values) != 0: 
            print('---------------------------------------')
            print(order.groupby('item', as_index=False)[['price','qty']].sum().to_string(index=False))
            print("\n\n Total: $" + str(sum(prices)))
            print('---------------------------------------')
        else:
            print('-------------------------')
            print("Nothing has been ordered!")
            print('-------------------------')

    