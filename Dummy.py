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