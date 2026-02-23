d1={"Milk":20,"Egg":100,"Paneer":200}
d2={"Milk":2,"Egg":1,"Paneer":2}
total=0
for k,v in d1.items():
    for l,m in d2.items():
        if k==l:
            total+=(v*m)
print("Total = ",total)