class grandpa():
    def phone(self):
        print("grandpa's phone")

class dad(grandpa):
    def money(self):
        print("dad's money")
class son(dad):
    def laptop(self):
        print("son's laptop")

ram=son()
ram.phone()
