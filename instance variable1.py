class mobile:
    def __init__(self,brand,price,chargetype):
        self.brand=brand
        self.price=price
        self.chargetype=chargetype
    def display(self):
        print("brad:",self.brand)
        print("price:",self.price)
        print("chargetype:",self.chargetype)

samsung = mobile("samsung","20000","B")
samsung.display()

vivo=mobile("vivo","15000","C")
vivo.display()
