from chef (inheritance method) import Cafe,Server

class Customer:
    def __init__(self,name):
        self.name=name

    def order(self,Server):
        print(self.name,'order from',Server)

    def pay(self,Server):
        print(self.name,'pay for item to',Server)

class Oven:
    def bake(Self):
        print('oven bkes')

class Cafe:
    def __init__(self):
        self.server=Server('Makrand')
        self.chef=Cafe('Rashi')
        self.oven=Oven()
        


    
