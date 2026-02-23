d1={}
n=str(input("Enter String = "))
for char in n:
    if char in d1:
        d1[char]+=1
    else:
        d1[char]=1
print(d1)