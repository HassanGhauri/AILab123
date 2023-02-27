dic1 = {
    1: 10,
    2: 20
}

dic2 = {
    3: 30,
    4: 40
}

dic3 = {
    5: 50,
    6: 60
}

dic4 = {}
for x, y in dic1.items():
    dic4.update({x: y})

for x, y in dic2.items():
    dic4.update({x: y})

for x, y in dic3.items():
    dic4.update({x: y})

print(dic4)
