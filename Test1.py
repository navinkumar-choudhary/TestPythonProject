arr = [10,20,30,40,50]
key = int (input("Enter the key to be searched: "))
found = False

for i in arr:
    if i == key:
        found = True
        break
if found == True:
    print("Key Found")
else:
    print("Key not found")


"""
if key in arr:
    if True:
        print("Key is found")
else:
    print("Key not Found")
"""