class laptop:

    chargertype="c-type"

    def __init__(self):
        self.brand=""
        self.price=30000

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)
        
    @classmethod
    def changechargertype(cls):
        chargertype="b-type"
        print("chargertype change to b")

hp=laptop()
hp.setprice(23400)
hp.getprice()

laptop.changechargertype()
