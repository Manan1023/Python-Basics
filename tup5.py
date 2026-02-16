l1=[1,(),2]
l2=[]
print(l1)
for i in l1:
    if isinstance(i,tuple):
        if not i:
            print()
        else:
            l2.append(i)
    else:
        l2.append(i)
print(l2)