from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def additon(self, No1, No2):
        pass

class Derived(Base):
    pass


dobj = Derived() # Error