class a():
    def __init__(self):
        print("A")
    def display(self):
        print("class is a")

class b(a):
    def __init__(self):
        super().__init__()
        print("B")
    def display(self):
        print("class is b")

class c(b):
    def __init__(self):
        super().__init__()
        print("C")
    def display(self):
        print("class is C")

class d(c,b):
    def __init__(self):
        super().__init__()
        print("D")
    def display(self):
        print("class is d")


obj1=b()
obj2=c()
obj3=d()  
