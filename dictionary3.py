a={
    "name":"chand",
    "dpt":"IT",
    "year":3,
    "learning":["python","sql","APIs"]
    }
a["year"]=2
print(a)
a["dist"]="salem"
print(a)
a.update({"dpt":"cse"})
print(a)
a.pop("dpt")
print(a)
del a["learning"]
print(a)
