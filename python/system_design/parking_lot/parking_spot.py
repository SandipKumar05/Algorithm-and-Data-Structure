from abc import ABC, abstractmethod

class ParkingSpot(ABC):
    def __init__(self, id, isFree, vehicle) -> None:
        self.__id = id
        self.__isFree = isFree
        self.__vehicle = vehicle
    
    @abstractmethod
    def assign_vehicle(self):
        pass

    def remove_vehicle(self):
        pass

class Handicapped(ParkingSpot):
    def __init__(self, id, isFree, vehicle) -> None:
        super().__init__(id, isFree, vehicle)
    
    def assign_vehicle(self):
        pass

class Large(ParkingSpot):
    def __init__(self, id, isFree, vehicle) -> None:
        super().__init__(id, isFree, vehicle)
    
    def assign_vehicle(self):
        pass

class Compact(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)
    
    def assign_vehicle(self):
        pass

class Motorbike(ParkingSpot):
    def __init__(self, id, isFree, vehicle):
        super().__init__(id, isFree, vehicle)
    
    def assign_vehicle(self):
        pass
    