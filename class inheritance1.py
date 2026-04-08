#class a and b
class a():

    def __init__(self):
        print("A")

    def display():
        print("class a is A")
        
class b():
    def __init__(self):
        print("B")

    def display():
        print("class b is B")

obj1=b()

#class a and b inherit without constructor
class a():

    def __init__(self):
        print("A")

    def display():
        print("class a is A")
        
class b(a):
    
    def display():
        print("class b is B")

obj1=b()

#class a and b inherit with constructor
class a():

    def __init__(self):
        print("A")

    def display():
        print("class a is A")
        
class b(a):
    def __init__(self):
        print("B")

    def display():
        print("class b is B")

obj1=b()
        


        


        

