car={}
n=int(input("numbers of feature in car:"))
for i in range(n):
    key=input("key:")
    value=input("value:")
    car[key]=value
print(car)
with open("data2.txt","w") as data:
    data.write("cars \n")
    for keys,values in car.items():
        data.write('%s:%s\n' % (keys,values))
    data.close()