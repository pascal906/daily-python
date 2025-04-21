# type casting, is process to convert a value of a one data type to another
# data type (string, integer, float, boolean)

# why typecasting?
# mungkin kita akan menerima input dari user, input user selalu bernilai string.
# bagaimana jika kita menerima angka, lalu akan digunakan untuk perhitungan?
# disinilah fungsi typecasting

# ada 2 penggunaannya, secara explicit and implicit

# explicit
name = "Paskalis"
age = 21
gpa = 1.9
student = True

# memeriksa tipe data dari variabel: pakai type()
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# convert data type, reassigning
age = float(age)
print(age)
print(type(age))
# output: 21.0, dari int 21, menjadi float, dan float akan menunjukkan .0 dibelakangnya

# float -> int
gpa = int(gpa)
print(gpa)
print(type(gpa))
# output: 1, karena nilai sebelumnya 1.9, di truncate, dibulatkan ke bawah, jadi 1

# bool -> str
student = str(student)
print(student)
print(type(student))
# output: True, tapi bukan lagi boolean, melainkan series of character "True"

# converting number ke boolean,
# tipe data boolean hanya bisa diperoleh convertnya dari angka,
age = bool(age)
print(age)
print(type(age))
# output: True, selain angka 0, saat casting ke boolean semuanya jadi True,
# jadi hanya angka 0 yang jadi False

# casting ke boolean juga bisa digunakan untuk pengecekan, apakah user
# memasukkan data atau tidak, misal:

name = ""
name = bool(name)
print(name)
# jika kosong, keluarannya adalah False, tapi jika diisi, walau hanya karakter " ",
# ini akan jadi True.

# inilah explicit type casting, secara manual convert tipe data ke tipe data berbeda


# implicit
# ini adalah saat kita convert tipe data ke tipe data lain secara otomatis

x = 2
y = 2.0

x = x / y
print(x)
# output: 1.0, ini menunjukkan bahwa variabel x, yg awalnya int, telah berubah
# perubahan ini terjadi karena perbedaan angka operand yang dilakukan pada operasi
# perhitungan, dan secara otomatis, tipe datanya diconvert