cities = [["Mumbai", 5500000],["Pune", 1000000],["Bengaluru", 1500000]]
# print(cities[0][0])

cities.append(["Nagput", 15000000])

# cities.append(100)    >We can't append like this cause It will not be iterable

for row in cities:
    for val in row:
        print(val)