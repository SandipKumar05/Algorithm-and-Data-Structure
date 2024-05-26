from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self,user_name, password, person, status):
        self.__user_name = user_name
        self.__password = password
        self.__person = person
        self.__status = status
    
    @abstractmethod
    def reset_password(self):
        pass

class Admin(Account):
    def __init__(self, user_name, password, person, status):
        super().__init__(user_name, password, person, status)
    
    def add_parking_lot(self, spot):
        pass

    def add_display_board(self, display_board):
        pass

    def add_entrance(self, entrance):
        pass

    def add_exit(self, exit):
        pass

    def reset_password(self):
        pass

class User(Account):
    def __init__(self, user_name, password, person, status):
        super().__init__(user_name, password, person, status)

    def reset_password(self):
        return super().reset_password()
    
    def process_ticket(self, ticket):
        pass
    