class calc:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add:",self.num1+self.num2)
    def sub(self):
        print("sub:",self.num1-self.num2)
    def mul(self):
        print("mul:",self.num1*self.num2)
    def div(self):
        print("div:",self.num1/self.num2)

obj1=calc(10,5)

obj1.add()
obj1.sub()
obj1.mul()
obj1.div()
