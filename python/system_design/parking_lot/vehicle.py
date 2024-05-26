from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_no):
        self.__license_no = license_no

    @abstractmethod
    def assign_ticket(self, ticket):
        pass

class Big(Vehicle):
    def __init__(self, license_no):
        super().__init__(self, license_no)
    
    def assign_ticket(self, ticket):
        pass