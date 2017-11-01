# list = []
"""
x = [10,"navin",20, True,50]
x[1] = 1000
for i in x:
    print(i)
print("First Element is: ",x[0])
"""

list1 = [10,20]
list2 = ["Navin","Appu"]
list3 = list1+list2
for i in list3:
    print(i)

# list[:4] - Takes as Begining of the List till 4th element,
# list[2:] - Takes as starting from 2 and till end of the list

list4 = list3[0:3] # list3[startIndex : endIndex] note: Ending Index will be taken as End-1 **IMP**
print("Values in List4")
for j in list4:
    print(j)

# self concatenation
list5 = [100,200]
list6 = list5+list5
print("Elements in List6: ")
for n in list6:
    print(n)
# Multiplying the Elements of the list and assigning to the other list
list5 = [100,200]
list7 = list5*6
print("Elements in List7: ")
for m in list7:
    print(m)

list8 = [1,2,3,4,5]
print("Is 2 in the List8? : ",2 in list8)
print("Is 12 in the List8? : ",12 in list8)

print("Is 2 not in the List8? : ",2 not in list8)
print("Is 12 not in the List8? : ",12 not in list8)

print("*"*35,"List Methods","*"*35)
list9 = [10,20,10,30]
print(list9.count(10))
list9.append(70)
print(list9)
list9.extend(list8)
print(list9)
list9.insert(0,"Navin")
print(list9)
list9.remove("Navin")  # Will take the Value to be removed from
print(list9)
list9.pop(3)  # Will take the index to remove the value on that Index
print(list9)
list9.pop()  # Will take the max index to remove the value on that Index
print(list9)

list9.sort()  # Sorts the Element of the List in Ascending order
print(list9)

list9.sort(reverse=True) # Sorts the Element of the List in descending order
print(list9)

list9.reverse() # just reverses the Element of the List
print(list9)

list10 = [x for x in list9 if x%5 == 0]
print(list10)

list11 = [y for y in range (1,11)]
print(list11)

list12 = [z for z in range(1,11) if z%2 == 0]
print(list12)

list13 = [z**2 for z in range(1,11) if z%2 == 0]
print(list13)

cities = ["Pune","Mumbai","Delhi","Chennai"]
cities = [x.upper() for x in cities]
print(cities)

cities = ["Pune","Mumbai","Delhi","Chennai"]
cities = [x.upper() for x in cities if len(x)<=4]
print(cities)

list14 = [10,2,30,20,1,100]
print("Length of the List14 is: ",len(list14))

print("Maximum number in the list is: ", max(list14))
print("Minimum number in the list is: ", min(list14))
print("Sum of the numbers in the list is: ", sum(list14))


list22 = [2,4,6,8, 40, 50]
list33 = [10,20,40,30]
list44 = []

# Adding the the elements with respective elements of the Lists
l1 = len(list22)
l2 = len(list33)
itr = 0
if l1>l2:
    itr = l1
else:
    itr = l2

for i in range(0,itr):
    if(i < l1 and i < l2):
        list44.append(list22[i]+list33[i])
    elif l1 > l2:
        list44.append(list22[i])
    else:
        list44.append(list33[i])

print("Final Output")
print(list44)