class laptop:

    def __init__(self):
        self.brand=""
        self.price=30000

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

hp=laptop()
hp.setprice(23400)
hp.getprice()
