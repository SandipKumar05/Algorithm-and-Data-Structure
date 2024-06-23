class singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class MenuService(singleton):
    def __init__(self):
        pass

a1 = MenuService()
a2 = MenuService()

print(a1 is a2)