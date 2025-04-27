# circumference of a circle/keliling lingkaran
# C = 2.pi.r

import math

# exercise1
radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is {round(circumference, 2)} cm")
# input: 4
# output: The circumference is 25.132741228718345

# to truncate the number, we can use round, maka:
# input: 4
# output: The circumference is 25.13

