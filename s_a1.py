s1=set(input() for i in range(2))
s2=set(input() for i in range(2))
if s1==s2:
    print("Both are equal.")
else:
    if s1<=s2:
        print("s1 is subset of s2")
    elif s2<=s1:
        print("s2 is subset of s1")
