l1=[("Burger",200),("VadaPav",30),("VadaPav",50),("VadaPav",10)]
print(l1)
n=len(l1)
for i in range(n):
    for j in range(0,n-i-1):
        if l1[j][1]<l1[j+1][1]:
            l1[j],l1[j+1]=l1[j+1],l1[j]

print(l1)