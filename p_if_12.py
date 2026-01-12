x=int(input("Enter x "))
y=int(input("Enter y "))
x1=int(input("Enter x1 "))
y1=int(input("Enter y1 "))
r=int(input("Enter r "))

if pow(x1-x,2)+pow(y1-y,2)<pow(r,2):
    print("Point is inside circle.")
elif pow(x1-x,2)+pow(y1-y,2)>pow(r,2):
    print("Point is outside circle.")
else:
    print("Point is on the circle.")
