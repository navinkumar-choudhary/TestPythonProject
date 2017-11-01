# dictionary = {}
dict = {
    1: "Ramu",
    2: "Shamu",
    3: "Manju",
    4: "Sanju"
}
for items in dict:
    print(dict[items])

dict1 = {
    "Paris":"France",
    "Tokyo":"Japan",
    "Budapest":"Hungary",
    "London":"England",
    "Delhi":"India"
}
for items in dict1:
    print(dict1[items])

for items in dict1.keys():
    print(items+ " is capital of " +dict1[items])

for items in dict1.values():
    print(items)

print("Size of Dict1 is: ",len(dict1))

print(dict1.keys()) # Retrieving Keys
print(dict1.values()) # Retrieving Values
print(dict1.items()) # Retrieves keys and
print(dict1.get("Paris"))

# deleting Element from the Dictionary
del dict1["London"]
print(dict1)

# Adding Element in the Dictionary
dict1["Beijing"] = "China"
print(dict1)

# Removing the Element from the Dictionary
if dict1.pop("Tokyo"):
    print(dict1)

# Truncating the Data from Dictionary Same as the Lists
print(len(dict1))
dict1.clear()
print(len(dict1))