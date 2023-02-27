time_taken = float(input("Enter the time taken: "))
print(f"You completed your job in {time_taken} hours")

if 2 <= time_taken <= 3:
    print("Well done!You are a highly efficient worker!")

if 3 <= time_taken <= 4:
    print("""You are slightly slow in completing your job,
            you need to improve your speed.""")

if 4 <= time_taken <= 5:
    print("""You are very slow in completing your job,
you need to have training to improve your speed.""")

if 5 < time_taken:
    print("""Sorry you have to leave the company, 
because your working speed is below the minimum working speed
required for our company.""")


