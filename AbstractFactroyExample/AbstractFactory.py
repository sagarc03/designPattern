from Coffee import CoffeeFactory
from Tea import TeaFactory


class AbstractFactory:
    @staticmethod
    def getFactory(type='tea'):
        if type.lower() == 'tea':
            return TeaFactory()
        elif type.lower() == 'coffee':
            return CoffeeFactory()


beverageFactory = AbstractFactory.getFactory('coffee')
beverage = beverageFactory.getBeverage('cold')
beverage.make()
beverage.sip()
