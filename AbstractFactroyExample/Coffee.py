from Interface import Beverage, AbstractFactory


class ColdCoffee(Beverage):
    def __init__(self):
        self.made = False

    def make(self):
        self.made = True
        print("Making cold coffee!")

    def sip(self):
        if self.made:
            print("Sip cold Coffee!")
        else:
            print("Please make the coffee first")


class HotCoffee(Beverage):
    def __init__(self):
        self.made = False

    def make(self):
        self.made = True
        print("Making hot coffee!")

    def sip(self):
        if self.made:
            print("Sip hot Coffee!")
        else:
            print("Please make the coffee first")


class CoffeeFactory(AbstractFactory):

    def getBeverage(self, type='hot'):
        if type.lower() == 'hot':
            return HotCoffee()
        elif type.lower() == 'cold':
            return ColdCoffee()
