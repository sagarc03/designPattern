import abc


class Beverage(abc.ABC):

    @abc.abstractmethod
    def make(self):
        raise NotImplementedError

    @abc.abstractmethod
    def sip(self):
        raise NotImplementedError


class AbstractFactory(abc.ABC):

    @abc.abstractmethod
    def getBeverage(self, type):
        raise NotImplementedError
