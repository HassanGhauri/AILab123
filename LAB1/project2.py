
def tempconverter(temp, unit):
    if unit == 'F':
        temperature = int((temp * (9/5)) + 32)
        return temperature
    elif unit == 'C':
        temperature = int((temp * (5/9)) - 32)
        return temperature
    else:
        print("invalid unit entered!")


print(tempconverter(60, 'F'))


