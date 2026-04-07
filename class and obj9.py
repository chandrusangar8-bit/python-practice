class laptop:
    chargertype="c-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("brand:",self.price)
        print("chargertype:",self.chargertype)

    chargertype="b-type"

hp=laptop("hp","45000")
hp.display()

lenovo=laptop("lenovo","50000")
lenovo.display()
