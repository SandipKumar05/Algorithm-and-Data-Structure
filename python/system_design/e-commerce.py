user, items, cartservice, paymentservice

class user:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name 
        self.email = email
        self.phone = phone

class userService:
    def add_user(self, name, email, phone):
        pass
    def get_user(self, id):
        pass

