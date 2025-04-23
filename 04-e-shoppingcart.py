# disini kita akan latihan membuat program shopping cart

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many whould you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")

# truncate total ke 2 desimal dibelakang koma
# dengan fungsi round()
# (function) def round(
#     number: variabel dengan tipe data number,
#     ndigits: banyak digit setelah koma
# ) -> _T@round

# jika inputnya:
# What item would you like to buy?: Pizza
# What is the price?: 4.99
# How many whould you like?: 3

# output:
# You have bought 3 x Pizza/s
# Your total is: $14.97