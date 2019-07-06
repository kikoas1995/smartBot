from abc import ABCMeta, abstractmethod

class Bot(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def signup(self): pass

    @abstractmethod
    def login(self): pass
