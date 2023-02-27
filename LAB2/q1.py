height = int(input("Enter height: "))
width = int(input("Enter width: "))
depth = int(input("Enter depth: "))

volume = height * width * depth
print(f"The volume of cube is:{volume}")

if 1 <= volume <= 10:
    print("Volume of Cube is Extra small")

if 11 <= volume <= 25:
    print("Volume of Cube is Small")

if 26 <= volume <= 75:
    print("Volume of Cube is Medium")

if 76 <= volume <= 100:
    print("Volume of Cube is Large")

if 101 <= volume <= 250:
    print("Volume of Cube is Extra large")

if 251 <= volume:
    print("Volume of Cube is Extra-Extra large")
