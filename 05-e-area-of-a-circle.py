# membuat program menghitung luas area lingkaran
# A = pi.r^2

# exercise2
# import library
import math

radius = float(input(f"Enter the radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of circle is: {round(area, 2)} cm^2")
# input: 5
# output: The area of circle is: 78.54 cm