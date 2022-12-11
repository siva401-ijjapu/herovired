a=int(input("input 1:"))
b=int(input("input 2:"))
c=int(input("input 3:"))
d=int(input("input 4:"))
e=int(input("input 5:"))
data1=open("data.txt","w")
if(a>0 and b>0 and c>0 and d>0 and e>0):
    print(a+b+c+d+e)
    total=a+b+c+d+e
    data1.write("total: %d"%total)
else:
    print("should provide positive number")
    data1.write("should provide positive number")
data1.close()