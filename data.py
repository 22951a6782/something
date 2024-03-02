class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class ll:
    def __init__(self):
        self.head=None
    def add(self):
        data=int(input("enter:"))
        new=node(data)
        if self.head is None:
            self.head=new
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new
    def display(self):
        if self.head is None:
            print("empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
s=ll()
s.add()
s.add()
s.add()
s.display()






                
