class Shoppingcart:
    def __init__(self):
        self.items=[]

    def add_item(self,item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return repr(self.items)

cart=Shoppingcart()
print(len(cart))
cart.add_item('mobile')
cart.add_item('Pen')
cart.add_item('Books')
print(cart)
print(len(cart))
