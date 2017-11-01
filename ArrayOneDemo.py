arr = [1,2,3,4,5]

arr.append(5)
arr.append(6)
arr.append("Naveen")
arr.append(12.5)
arr.append(True)

for i in arr:
    print(i)
# print(arr.count())

# arr.clear()
# print("Data has been erased")
# for i in arr:
#     print(i)

print(arr.count("Naveen"))

print(arr.index("Naveen")) # to retrieve index of element
print(arr[7])

arr.insert(2, 100)
for i in arr:
    print(i)
print(arr.index(100))

arr.pop(arr.index("Naveen"))
for i in arr:
    print(i)


arr.reverse()
for i in arr:
    print(i)

arr.remove(100)
for i in arr:
    print(i)