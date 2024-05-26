from enum import Enum
class PaymentStatus(Enum):
    COMPLETE = 1
    FAILED = 2
    PENDING = 3
    UNPAID = 4
    REFUNDED = 5

class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2

class Person():
    def __init__(self, name, email, phone) -> None:
        self.__name = name
        self.__phone = phone
        self.__email = email
    
    

