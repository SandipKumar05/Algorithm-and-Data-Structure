class node:
    def __init__(self,v):
        self.value=v
        self.next=None

a=node(5)
a.next=node(10)

while a!= None:
    print(a.value)
    a=a.next