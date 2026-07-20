from abc import ABC, abstractmethod # abc module

class Base(ABC):
    @abstractmethod
    def additon(self, No1, No2): # Abstract Method (Without body)
        pass

class Derived(Base):
    def additon(self, No1, No2): # Concrete Method (With body)
        return No1 + No2

dobj = Derived()
Ret = dobj.additon(10, 11)

print("Addition is: ", Ret)