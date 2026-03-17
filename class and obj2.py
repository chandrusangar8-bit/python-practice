class goa:
    name=""
    drink=""
    def party(self):
        print("attending drinks party")
    def beach(self):
        print("enjoying the beach!")

ramesh=goa()
suresh=goa()

ramesh.name="ramesh"
suresh.name="suresh"

ramesh.drink="yes"
suresh.drink="no"

print(ramesh.name)
print("drink:",ramesh.drink)
ramesh.party()
print(suresh.name)
print("drink:",suresh.drink)
suresh.beach()


