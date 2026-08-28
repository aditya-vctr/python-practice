# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals ={
    "USA": "washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}
# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("India"))
# capitals.update({"Germany":"berlin"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()
# keys = capitals.keys()
# values = capitals.values()
# for key in capitals.keys():
#     print(key)

# for value in capitals.values():
#     print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key} : {value}")