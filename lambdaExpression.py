"""
def add(n1,n2):
    sum = n1+n2
    return sum
print(add(12,12))
"""

# we can write above function in one line as below
result = lambda n1,n2:n1+n2
print(result(10,20))


square = lambda n3:n3**2
print(square(10))

cube = lambda n4:n4**3
print(cube(2))

upperAndLower = lambda s : s.upper() + s.lower()
print(upperAndLower("navin"))
