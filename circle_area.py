# Desing a program to calcule a circle area
# Área = PI x r2

# Import PI number
from math import pi

# Indicate radius of the circle
r = float(input ("Input the radius of the circle : "))

# Result
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
