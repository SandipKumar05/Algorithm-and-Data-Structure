from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, status, timestamp):
        self.amount = amount
        self.status = status
        self.timestamp = timestamp

    @abstractmethod
    def init_transaction(self):
        pass

class Cash(Payment):
    def __init__(self, amount, status, timestamp):
        super().__init__(amount, status, timestamp)

    def init_transaction(self):
        print("cash")

class CreditCard(Payment):
    def __init__(self, amount, status, timestamp):
        super().__init__(amount, status, timestamp)

    def init_transaction(self):
        print("credit card")

# a = Payment(1,2,3)
b = Cash(1,2,3)
c= CreditCard(1,2,3)

# print(a.init_transaction())
print(b.init_transaction())
print(c.init_transaction())
