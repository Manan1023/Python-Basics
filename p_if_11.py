x1=int(input("Enter x1"))
y1=int(input("Enter y1"))
x2=int(input("Enter x2"))
y2=int(input("Enter y2"))
x3=int(input("Enter x3"))
y3=int(input("Enter y3"))

if x1*(y2-y3)-x2*(y1-y3)+x3*(y1-y2)==0:
    print("Given points are on straight line.")
else:
    print("Given points are not on straight line.")
    

