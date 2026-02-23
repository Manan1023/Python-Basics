d1={}
n=str(input("Enter String = "))
w=n.split()
for k in w:
    if k in n:
        if k in d1:
            d1[k]+=1
        else:
            d1[k]=1
print(d1)