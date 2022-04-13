#FranklinP1
#Programmer: Anthony Franklin
#Email: afranklin18@cnm.edu
#Purpose: provides user capability to calculate
#Volume of a pyramid

from math import*


print ("Hello, I am here to help you calculate the surface area and volume of a square pyramid")

a = float(input ("Length of the pyramid's base in ft.: "))
h = float(input ("Height of the pyramid in ft.: "))
s = sqrt((h*h)+((a/2)*(a/2)))
Area = (4*((s*a)/2))
Volume = (((a*a)*h)/3)

print("If the length of your pyramid's base is: ", a, "ft.")
print("And the height of your pyramid is: ", h, "ft.")
print("Then the surface area of the pyramid is : ", round (Area, 3),"ft.", "and the Volume is :", round (Volume, 3), "ft.")
                                        
     
input()


            