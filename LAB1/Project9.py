def percent_calc(no_courses):
    courses = []
    i = 0

    while i < (no_courses + 1):
        course = int(input(f"enter marks of course({i}) : "))
        courses.append(course)
        i += 1

    total_marks = 0
    for x in courses:
        total_marks += x

    percentage = float((total_marks * 100)/600)

    for x in range(len(courses)):
        print(f"Your marks in course({x}): {courses[x]}")

    print(f"Your percentage is :{percentage} %")

    if 90 < percentage < 100:
        print(f"Congratulations! you got A+")
    elif 80 < percentage < 90:
        print(f"Congratulations! you got A")
    elif 70 < percentage < 80:
        print(f"You got B+")
    elif 60 < percentage < 70:
        print(f"You got B")
    elif 50 < percentage < 60:
        print(f"You got C+")
    else:
        print(f"Unfortunately you are failed!")


percent_calc(6)
