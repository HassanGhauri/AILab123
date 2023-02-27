name = input("Enter name of city: ")
population = input("Enter population of city: ")
mayor = input("Enter name of mayor of city: ")

with open("CityRecords.txt","a") as f:
    f.write(f"\n{name}\t{population}\t{mayor}")





