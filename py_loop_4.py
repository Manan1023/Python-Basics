s=int(input("Enter Number = "))
n=0
for i in range(2,s//2):
    if i%i==0:
        n=1;
if n==0:
    print(s," is prime.")
else:
    print(s," is not prime.")
       
