from Interface import Beverage, AbstractFactory


class IcedTea(Beverage):
    def make(self):
        print("Making iced tea!")

    def sip(self):
        print("Sip iced tea!")


class HotTea(Beverage):
    def make(self):
        print("Making hot tea!")

    def sip(self):
        print("Sip hot tea!")


class TeaFactory(AbstractFactory):

    def getBeverage(self, type='hot'):
        if type.lower() == 'hot':
            return HotTea()
        elif type.lower() == 'cold':
            return IcedTea()
