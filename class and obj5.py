class fruit:
    def __init__(self):
        self.color="yellow"

banana=fruit()
banana.color="red"
print(banana.color)



class fruit:
    def __init__(self,co1,co2):
        self.color="yellow"
        self.color1=co1
        self.color2=co2

banana=fruit("green","blue")
print(banana.color)
print(banana.color1)
print(banana.color2)

