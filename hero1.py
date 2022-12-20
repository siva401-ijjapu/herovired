import pandas as pd
o=open('hi.txt','a')
a=int(input("elements in a list:"))
b=list(map(int,input("\nEnter the numbers : ").split()))
c=[]
for j in b:
    c.append(j**2)
x=pd.Series(c,index=b)
print(x)
print(x,file=o)
