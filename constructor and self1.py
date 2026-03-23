class laptop:
    def __init__(self):
        self.ram=""
        self.processor=""
    def display(self):
        print("ram:",self.ram)
        print("processor:",self.processor)


hp=laptop()
dell=laptop()

hp.ram="8gb"
hp.processor="i5"
print(hp.ram)

dell.ram="12gb"
dell.processor="i6"
dell.display()
        

        
