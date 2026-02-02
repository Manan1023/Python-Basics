s=input("Enter String = ")
t=len(s)-1
for i in range(0,len(s)):
    print(s[i]*2,end="")
print()
for i in range(0,t):
    if s[i]==s[i+1]:
        continue
    else:
        print(s[i],end="")
print(s[t])
