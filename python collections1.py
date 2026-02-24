a=[1,2,3,4,5]
print(type(a))
a.append(7)
a.append(6)
a.append(True)
b=int(input("b:"))
a.append(b)
print(a)

b=[1,2,3,4,5]
print(b)
b.insert(1,9)
print(b[1])
print(b)

c=[5,3,2,1]
c[0]=11
c.insert(0,11)
print(c)
