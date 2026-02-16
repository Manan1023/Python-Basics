t1=(19,3,2008)
t2=(16,2,2026)
y=0
for t in range(t1[2],t2[2],1):
    if t % 4 == 0:
        y+=366
    else:
        y+=365
y=y+(t2[1]-t1[1])*31
y=y+(t2[0]-t1[0])
print("Days = ",y)