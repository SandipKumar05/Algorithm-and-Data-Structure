class classExample:
    def __init__(self, name):
        self.name = name
    def name(self):
        print(self.name)

class parent_class:
    def __init__(self):
        self.parent_name = "parent"
    def name(self):
        print(self.parent_name)

class child_class(parent_class):
    def __init__(self):
        self.child_name = "child"
        parent_class.parent_name = "------------"
        # parent_class.__init__(self)
    
    def name(self):
        print(self.parent_name)

obj = child_class()
obj.name()