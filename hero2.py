import pandas as pd
h=open('hi.txt','a')
def Add(a,b):                                          
    return(int(a+b))
def Sub(a,b):                                      
    return(int(a-b))
def Multiple(a,b):                                   
    return(int(a*b))
def Div(a,b):                                         
    return(int(a/b))
def Mod(a,b):                                          
    return(int(a%b))
m = int(input(" Enter the first number :"))              
n = int(input(" Enter the second number :"))            
l1 = [f'{m} + {n}',f'{m} - {n}',f'{m} * {n}',f'{m} / {n}',f'{m} % {n}']
l2 = []                                                  
l2.append(Add(m,n))                           
l2.append(Sub(m,n))                       
l2.append(Multiple(m,n))                     
l2.append(Div(m,n))                           
l2.append(Mod(m,n))                            
r = pd.Series(l2,index=l1)                         
print(r)
print(r,file=h)  