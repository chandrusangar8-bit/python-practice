class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print(self.name)
        print(self.regno)
        
        
t1=teacher("kavitha","014")
t2=teacher("laksmi","036")

t1.display()
t2.display()
