# singleton class

class __ParkingLot(object):
    __instances = None
    def __new__(cls):
        if cls.__instances is None:
            cls.__instances = super(__ParkingLot, cls).__new__(cls)
        return cls.__instances

class ParkingLot(metaclass=__ParkingLot):
    def __init__(self, id, name, address, parking_rate) -> None:
        pass

    