a=[]
for i in range(5):
    num=int(input("num"+str(i+1)))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)

avg=sum/5
print(avg)
