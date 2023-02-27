sample_List = ['abc', 'xyz', 'aba', '1221']

length = 0
for x in sample_List:
    if x[0] == x[-1]:
        length += 1

print(length)
