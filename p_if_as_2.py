a=int(input("Enter marks of sub1 : "))
b=int(input("Enter marks of sub2 : "))
c=int(input("Enter marks of sub3 : "))

t=a+b+c
avg=t/3

print("Total=",t)
print("Avrage=",avg)

if a<=39 or b<=39 or c<=39:
    print("Student is Fail.")
else:
    print("Student is Pass.")

if a>=0 and a<=39:
    print("Grade in sub1 = F")
elif a<=44:
    print("Grade in sub1 = P")
elif a<=49:
    print("Grade in sub1 = C")
elif a<=54:
    print("Grade in sub1 = B")
elif a<=59:
    print("Grade in sub1 = B+")
elif a<=69:
    print("Grade in sub1 = A")
elif a<=79:
    print("Grade in sub1 = A+")
elif a<=100:
    print("Grade in sub1 = O")

if b>=0 and b<=39:
    print("Grade in sub2 = F")
elif b<=44:
    print("Grade in sub2 = P")
elif b<=49:
    print("Grade in sub2 = C")
elif b<=54:
    print("Grade in sub2 = B")
elif b<=59:
    print("Grade in sub2 = B+")
elif b<=69:
    print("Grade in sub2 = A")
elif b<=79:
    print("Grade in sub2 = A+")
elif b<=100:
    print("Grade in sub2 = O")

if c>=0 and c<=39:
    print("Grade in sub3 = F")
elif c<=44:
    print("Grade in sub3 = P")
elif c<=49:
    print("Grade in sub3 = C")
elif c<=54:
    print("Grade in sub3 = B")
elif c<=59:
    print("Grade in sub3 = B+")
elif c<=69:
    print("Grade in sub3 = A")
elif c<=79:
    print("Grade in sub3 = A+")
elif c<=100:
    print("Grade in sub3 = O")
