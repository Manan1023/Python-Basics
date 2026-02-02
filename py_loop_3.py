s=input("Enter Number = ")
n=0
t=0
for i in range(0,10):
    n=n+s.count(str(i))
print("No. of Digits = ",n)
for i in range(65,91):
    t=t+s.count(chr(i))
for i in range(97,123):
    t=t+s.count(chr(i))
print("No. of Alphabets = ",t)
