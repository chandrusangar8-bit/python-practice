a=[]
print("enter 10 number:")
for i in range(4):
    b=int(input("enter num"+str(i+1)))
    a.append(b)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)

