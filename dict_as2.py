d1={'P1':100,'P2':50,'P3':60}
d2={'P5':130,'P2':20,'P4':60}
d3={}
p=0

for k,v in d1.items():
    for l,m in d2.items():
        if k==l:
            d3.update({k:v+m})
        else:
            for i in range(len(d1)+len(d2)):
                if d3[i] != l:
                    d3.update({l:m})
            d3.update({k:v})

            
print(d3)

for k,v in d3.items():
    if v>p:
        p=v
print("Max value=",p)    
