# variable, sebuah kontainer/wadah untuk menyimpan nilai (string, integer, float, boolean)
# variable berperilaku sebagai nilai yang di simpannya

# to create variable:
# harus menggunakan nama yg unik,
# menggunakan tanda operator assign (=)
# untuk teks, itu merupakan susunan (series) dari karakter, jadi bisa pakai double " atau single quote '

# contoh pembuatan variabel:
first_name = "Paskal"
# variabel first_name ini akan berperilaku sebagai "Paskal"

# untuk melihat demonstrasinya, kita akan print variabel ini
print(first_name)

# output: Paskal

# kita juga bisa menampilkan variabel bersama dengan teks, yg digunakan adalah formatting
# caranya, letakkan karakter f depan "", dan untuk variabel, berikan placeholder {} untuk memanggil nama variabel di dalamnya:
print(f"Hello {first_name}")

# ----variable string:
first_name = "Paskal"
food = "Pizza"
email = "paskal123@fake.com"

# variable string, merupakan susunan(series) dari suatu karakter, mereka bisa saja berupa angka, ataupun simbol, tapi tetap dianggap sebagai satu karakter

print(f"Hello, {first_name}!")
print(f"You like {food}")
print(f"Your email is: {email}")

# ----variable integer:
# merupakan angka bulat, seperti kuantitas barang, jumlah kucing, umur, dll
# integer tidak perlu ada dalam "", '' karena yg pakai ini hanya karakter (string)
# integer tidak menggunakan tanda . karena misal jika 3.5, ini berarti float bukan integer
age = 25
quantity = 3
num_of_students = 32

# dan jika kita memakai variabel ini maka:
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

# integer ini bisa digunakan pada arithmetic expression, kalau string tidak

# ----variable float:
# merupakan floating point number, (3.2, 3.6666, ...), contoh: harga, berat, tinggi, jarak, dll

price = 10.99
gpa = 3.2
distance = 5.52

print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"Your ran {distance}km")

# ----variable boolean:
# menggambarkan 2 nilai, entah itu True (1) dan False (0)
# karakter pertama selalu kapital, True, False

is_student = True
for_sale = True
is_online = True

print(f"Are you a student?: {is_student}")

# jarang digunakan sebagai output, tetapi lebih banyak digunakan internally dalam proses perhitungan/kalkulasi program
# contoh:

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

if is_online:
    print("You are online")
else:
    print("You are offline")