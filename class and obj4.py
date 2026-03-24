class student:
    def __init__(self):
        self.name="chand"
        self.regno="013"

    def display(self):
        print("name:",self.name)
        print("regno:",self.regno)

s1=student()
s2=student()


s1.name="praveen"
s1.regno="40"
s2.name="kathir"
s2.regno="20"

s1.display()
s2.display()
