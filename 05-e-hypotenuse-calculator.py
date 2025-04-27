# membuat program calculator menghitung hypotenuse dari segitiga
# c = sqrt(a^2 + b^2)

# excercise3
import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse of the triangle is {hypotenuse}")

# input: 3, 4
# The hypotenuse of the triangle is 5.0