# disini kita akan membuat program untuk menghitugn luas area

# ingat, input selalu bernilai string,
# jadi perlu typecasting ke tipe data number (int, float)
# length = float(input("Enter a length of a rectangle: "))
# width = float(input("Enter a width of a rectangle: "))

# area = length * width
# print(f"The area is {area} cm^2")

# jika inputnya: 
# Enter a length of a rectangle: 21  
# Enter a width of a rectangle: 4

# output:
# The area is 84.0cm^2

# dan jika ini adalah bangun ruang, kita bisa menambahkan lagi variabelnya,
# jadi panjang, lebar, dan tinggi
length = float(input("Enter a length of a cube: "))
width = float(input("Enter a width of a cube: "))
height = float(input("Enter a height of a cube: "))

volume = length * width * height
print(f"The area is {volume} cm^3")

# jadi jika inputnya:
# Enter a length of a cube: 3
# Enter a width of a cube: 4
# Enter a height of a cube: 6
# yap ini hanya contoh, kalo cube pastinya tiap sisi sama

# output
# The area is 72.0 cm^3