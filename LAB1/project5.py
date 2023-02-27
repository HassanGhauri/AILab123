empire = {
  "name": "Mughal Empire",
  "capital": "Delhi",
  "founded_in": 1526
}

empire.clear()
x = empire.copy()
y = empire.get("founded_in")
z = empire.items()
m = empire.keys()
n = empire.values()
empire.pop("name")
empire.popitem()
empire.update({"founder": "Babar"})

print(empire)
