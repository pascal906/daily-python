# we will learn how to accept user input,
# and we will have some exercises: mad libs, area calc, and shopping cart

# to accept some user input, we can use input() function
# input(prompt: object = "", /) -> str

# input("Enter your name: ")
# kode ini akan menerima input, akan tetapi,
# kita perlu variabel untuk menampung input yang masuk

name = input("Enter your name: ")

# age = input("Enter your age: ")
# age = int(age)

# with one line, casting to int:
age = int(input("Enter your age: "))

# casting to float
# age = float(input("Enter your age: "))

# kita coba jumlahkan age
age = age + 1

print(f"Hello, {name}")
print(f"You are {age} years old.")

# perlu diingat, setiap kita menerima input dari user,
# input itu selalu bertipe string,
# jadi saat input yang dimasukkan user akan digunakan untuk keperluan perhitungan,
# perlu dilakukan typecasting

