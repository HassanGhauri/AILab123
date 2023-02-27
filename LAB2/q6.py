number = int(input("Enter the number whose table you want: "))

table = []
for x in range(0, 11):
    table.append(number * x)
    print(f" {number} x {x} = {table[x]}")

