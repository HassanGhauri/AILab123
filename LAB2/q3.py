Known_Password = "ABC$123"
Password = str(input("Enter Password: "))

if Password.upper() == Known_Password:
    print("Welcome!")
else:
    print("I don't know you.")

