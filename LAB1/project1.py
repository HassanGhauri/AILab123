
def swap(num1, num2, num3, num4):
    print(f'a = {num1}', f'b = {num2}', f'c = {num3}', f'd = {num4}')
    temp1 = num1
    num1 = num4
    num4 = temp1
    temp2 = num2
    num2 = num3
    num3 = temp2

    print(f'a = {num1}', f'b = {num2}', f'c = {num3}', f'd = {num4}')


swap(2, 56, 78, 9)


