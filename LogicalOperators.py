x = 10
y = 20
z = 20

print("#"*50+"\n")
print(x>y and x>z)
print(x>y and z>x)
print(z>x and x>y)
print(z>x and y>x)
print("\n")

print("#"*50+"\n")
print(x>y or x>z)
print(x>y or z>x)
print(z>x or x>y)
print(z>x or y>x)
print("\n")

print("#"*50+"\n")
print(not(x>y))
print(not y>x)
print("\n")